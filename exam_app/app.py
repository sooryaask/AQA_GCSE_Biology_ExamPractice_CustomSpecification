"""
AQA Combined Science Trilogy (8464) Biology Higher — AI Exam Practice App
Flask backend with Claude-powered marking.
"""

import os
import json
from flask import Flask, render_template, request, jsonify, Response, stream_with_context
import anthropic
from questions import get_all_questions, get_question_by_id, TOPICS_PAPER1, TOPICS_PAPER2

app = Flask(__name__)
client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

MARKING_SYSTEM_PROMPT = """You are an experienced AQA GCSE Biology examiner marking student answers for the Combined Science: Trilogy (8464) Higher tier paper.

Your job is to mark student answers strictly but fairly, exactly as AQA examiners do.

When marking, follow these rules:
1. Apply the mark scheme provided — award marks point by point.
2. Use the principle of "own consequential error": if a student makes one error but correctly applies their (wrong) value in subsequent steps, they can still earn method marks.
3. Credit answers that convey the correct scientific meaning even if worded differently to the mark scheme.
4. Do NOT award marks for vague, incomplete, or scientifically incorrect statements.
5. Be specific about EXACTLY which points scored and which were missed.
6. Keep your response structured and clear.

Your response MUST follow this exact format:

**MARKS AWARDED: X / Y**

**What you got right:**
[List each point that earned a mark with ✓]

**What you missed or got wrong:**
[List each point that was missing or incorrect with ✗]

**Examiner feedback:**
[2-4 sentences of specific, actionable advice to improve this type of answer]

**Model answer:**
[A concise model answer that would score full marks]
"""

@app.route("/")
def index():
    questions = get_all_questions()
    return render_template("index.html",
                           questions=questions,
                           topics_p1=TOPICS_PAPER1,
                           topics_p2=TOPICS_PAPER2)

@app.route("/api/questions")
def api_questions():
    paper = request.args.get("paper", type=int)
    topic = request.args.get("topic", "")
    questions = get_all_questions()
    if paper:
        questions = [q for q in questions if q["paper"] == paper]
    if topic:
        questions = [q for q in questions if q["topic"] == topic]
    # Don't send mark scheme to frontend
    safe = [{k: v for k, v in q.items() if k != "mark_scheme"} for q in questions]
    return jsonify(safe)

@app.route("/api/mark", methods=["POST"])
def api_mark():
    data = request.get_json()
    question_id = data.get("question_id")
    student_answer = data.get("answer", "").strip()

    if not question_id or not student_answer:
        return jsonify({"error": "Missing question_id or answer"}), 400

    question = get_question_by_id(question_id)
    if not question:
        return jsonify({"error": "Question not found"}), 404

    user_message = f"""Please mark this student answer.

QUESTION ({question['marks']} marks):
{question['question']}

MARK SCHEME:
{question['mark_scheme']}

STUDENT'S ANSWER:
{student_answer}

Mark the answer out of {question['marks']} marks."""

    def generate():
        with client.messages.stream(
            model="claude-opus-4-6",
            max_tokens=1500,
            system=MARKING_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_message}],
            thinking={"type": "adaptive"},
        ) as stream:
            for text in stream.text_stream:
                yield f"data: {json.dumps({'text': text})}\n\n"
        yield "data: [DONE]\n\n"

    return Response(stream_with_context(generate()),
                    mimetype="text/event-stream",
                    headers={"Cache-Control": "no-cache",
                             "X-Accel-Buffering": "no"})

@app.route("/api/question/<qid>")
def api_single_question(qid):
    q = get_question_by_id(qid)
    if not q:
        return jsonify({"error": "Not found"}), 404
    safe = {k: v for k, v in q.items() if k != "mark_scheme"}
    return jsonify(safe)

if __name__ == "__main__":
    app.run(debug=True, port=5050, threaded=True)
