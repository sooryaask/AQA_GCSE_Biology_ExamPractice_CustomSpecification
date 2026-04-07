"""
AQA Combined Science Trilogy (8464) Biology Higher — Question Bank
Built from custom specification analysis of Specimen + 2018–2024 papers.
Topics ordered by frequency (highest priority first).
"""

QUESTIONS = [

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 1 — CELL BIOLOGY
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "CB001",
        "paper": 1,
        "topic": "Cell Biology",
        "subtopic": "Microscopy & Magnification",
        "question": (
            "A student observes a cell using a light microscope. "
            "The image of the cell measures 36 mm on the screen. "
            "The actual length of the cell is 0.045 mm.\n\n"
            "Calculate the magnification of the image. Show your working."
        ),
        "marks": 3,
        "command_word": "Calculate",
        "mark_scheme": (
            "• Correct formula stated or implied: magnification = image size ÷ real size [1]\n"
            "• Correct substitution: 36 ÷ 0.045 [1]\n"
            "• Correct answer: ×800 [1]\n"
            "Award 2 marks if correct answer given without working. "
            "Award 1 mark if formula is correct but arithmetic error leads to wrong answer with working shown. "
            "Note: both values must be in the same units; 36 mm ÷ 0.045 mm = 800 (dimensionless). "
            "Do NOT penalise omission of × symbol."
        ),
        "priority": "⭐ High — appears in every Paper 1 (8/8)",
        "hint": "Magnification = image size ÷ real size. Both must be in the same units."
    },
    {
        "id": "CB002",
        "paper": 1,
        "topic": "Cell Biology",
        "subtopic": "Prokaryotic vs Eukaryotic Cells",
        "question": (
            "Give four differences between a bacterial (prokaryotic) cell "
            "and a plant (eukaryotic) cell."
        ),
        "marks": 4,
        "command_word": "Give",
        "mark_scheme": (
            "Award 1 mark each for any four of:\n"
            "• Bacterial cell has no nucleus / DNA is not enclosed in a membrane-bound nucleus; "
            "plant cell has a nucleus [1]\n"
            "• Bacterial cell has no membrane-bound organelles; plant cell has membrane-bound organelles "
            "(e.g. mitochondria, chloroplasts) [1]\n"
            "• Bacterial cell is smaller / has smaller ribosomes [1]\n"
            "• Bacterial cell has a cell wall made of peptidoglycan / murein; "
            "plant cell wall is made of cellulose [1]\n"
            "• Bacterial cell has circular DNA / plasmids; plant cell has linear chromosomes [1]\n"
            "• Plant cell has a permanent vacuole; bacterial cell does not [1]\n"
            "• Plant cell has chloroplasts; bacterial cell does not [1]\n"
            "Accept converse statements. Do NOT accept 'bacterial cell has no nucleus' alone "
            "without clarification that it has a plasmid / circular DNA instead."
        ),
        "priority": "⭐ High — appears 6/8 Paper 1 papers",
        "hint": "Think about: nucleus, organelles, cell wall material, DNA type, vacuole, chloroplasts."
    },
    {
        "id": "CB003",
        "paper": 1,
        "topic": "Cell Biology",
        "subtopic": "Cell Division — Mitosis",
        "question": (
            "Describe what happens during each of the three stages of the cell cycle.\n\n"
            "Stage 1 — Cell growth\n"
            "Stage 2 — DNA replication\n"
            "Stage 3 — Mitosis and cell division"
        ),
        "marks": 3,
        "command_word": "Describe",
        "mark_scheme": (
            "Award 1 mark per stage:\n"
            "Stage 1: Cell grows / increases in size; new proteins and organelles are made / cytoplasm increases [1]\n"
            "Stage 2: DNA is copied / replicated / each chromosome is duplicated / "
            "number of chromosomes doubles (so each new cell gets a full set) [1]\n"
            "Stage 3: Chromosomes separate / nucleus divides; "
            "then the cytoplasm divides to produce two genetically identical daughter cells [1]\n"
            "Accept any answer that correctly describes each stage. "
            "Stage 3 mark requires reference to both nucleus division AND cell division."
        ),
        "priority": "⭐ High — appears 6/8 Paper 1 papers",
        "hint": "For each stage, describe what specifically happens (not just name it)."
    },
    {
        "id": "CB004",
        "paper": 1,
        "topic": "Cell Biology",
        "subtopic": "Osmosis — Required Practical",
        "question": (
            "A student investigated osmosis using potato cylinders. "
            "They placed cylinders in solutions of different sucrose concentrations. "
            "One cylinder had a starting mass of 4.50 g and a final mass of 3.87 g.\n\n"
            "(a) Calculate the percentage change in mass. Give your answer to one decimal place. [2]\n\n"
            "(b) Explain why percentage change in mass is used rather than change in mass. [1]\n\n"
            "(c) The student determines the concentration of the cell contents is 0.35 mol/dm³ "
            "from a graph. Explain how the student would identify this value from the graph. [1]"
        ),
        "marks": 4,
        "command_word": "Calculate / Explain",
        "mark_scheme": (
            "(a) % change = (3.87 − 4.50) / 4.50 × 100 [1 for correct formula/substitution]\n"
            "= −0.63 / 4.50 × 100 = −14.0% [1 for correct answer to 1 d.p.]\n"
            "Accept −14% if clear 1 d.p. intended. Negative sign required for full marks.\n\n"
            "(b) Potato cylinders were (likely) not identical starting masses / "
            "to allow fair comparison between cylinders of different sizes / "
            "to standardise results [1]\n\n"
            "(c) The concentration where the graph line crosses the x-axis / "
            "where percentage change = 0 [1]\n"
            "Accept: 'where the line of best fit crosses zero on the y-axis'."
        ),
        "priority": "⭐ High — appears 6/8 Paper 1 papers",
        "hint": "% change = (change in mass ÷ starting mass) × 100. The x-intercept = isotonic concentration."
    },
    {
        "id": "CB005",
        "paper": 1,
        "topic": "Cell Biology",
        "subtopic": "Stem Cells",
        "question": (
            "A patient needs a new heart valve. Doctors are considering using stem cells "
            "taken from the patient's own body to grow the replacement valve.\n\n"
            "Give two advantages of using the patient's own stem cells "
            "compared to using embryonic stem cells."
        ),
        "marks": 2,
        "command_word": "Give",
        "mark_scheme": (
            "Award 1 mark each for two of:\n"
            "• No risk of rejection / immune response (cells are genetically matched to the patient) [1]\n"
            "• No ethical issues / concerns about using embryos [1]\n"
            "• Patient does not need immunosuppressant drugs [1]\n"
            "Do NOT accept 'cheaper' without biological justification."
        ),
        "priority": "High — appears 5/8 Paper 1 papers",
        "hint": "Think about why the body might reject foreign cells, and about ethical concerns."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 1 — ORGANISATION (Digestion, Heart, Infection)
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "OR001",
        "paper": 1,
        "topic": "Organisation",
        "subtopic": "Enzymes — pH Effect on Amylase",
        "question": (
            "A student investigated the effect of pH on the activity of amylase. "
            "The student used a colorimeter to measure the amount of starch remaining at different pH values.\n\n"
            "The results showed that at pH 2, starch was not digested after 10 minutes. "
            "At pH 7, all starch was digested within 4 minutes.\n\n"
            "Explain why amylase activity is much lower at pH 2 than at pH 7. "
            "Use the concept of active site in your answer."
        ),
        "marks": 3,
        "command_word": "Explain",
        "mark_scheme": (
            "• Enzymes have a specific active site shape / active site is complementary to the substrate [1]\n"
            "• At pH 2, the low pH (high H⁺ concentration) changes the shape of the active site / "
            "denatures the enzyme / breaks ionic/hydrogen bonds in the enzyme [1]\n"
            "• The substrate (starch) can no longer fit into the active site / "
            "enzyme-substrate complexes cannot form as efficiently / "
            "rate of reaction decreases [1]\n"
            "Note: 'denatured' alone scores 1 mark only if active site shape change is explained. "
            "For full marks must link pH change → active site shape change → reduced substrate binding."
        ),
        "priority": "⭐ High — appears 5/8 Paper 1 papers",
        "hint": "Structure your answer: pH changes → bonds in enzyme break → active site shape changes → substrate cannot bind."
    },
    {
        "id": "OR002",
        "paper": 1,
        "topic": "Organisation",
        "subtopic": "Food Tests — Required Practical",
        "question": (
            "A student has three unknown food solutions labelled A, B and C. "
            "She wants to test each solution for the presence of:\n"
            "• starch\n• reducing sugar\n• protein\n\n"
            "Describe how she should carry out these three food tests. "
            "For each test, state the reagent used and the colour of a positive result."
        ),
        "marks": 6,
        "command_word": "Describe",
        "mark_scheme": (
            "Starch test:\n"
            "• Add iodine solution to the food sample [1]\n"
            "• Positive result: blue-black colour [1]\n\n"
            "Reducing sugar test:\n"
            "• Add Benedict's reagent to the food sample [1]\n"
            "• Heat in a water bath / gently boil [1]\n"
            "• Positive result: brick red / orange / yellow colour [1]\n\n"
            "Protein test (Biuret):\n"
            "• Add Biuret reagent / sodium hydroxide then copper sulfate solution [1]\n"
            "• Positive result: purple / lilac / violet colour [1]\n\n"
            "Award maximum 6 marks. Reagent + positive colour required for each test to score both marks. "
            "Accept 'turn blue-black from yellow/orange' for iodine positive result."
        ),
        "priority": "⭐ High — appears 5/8 Paper 1 papers",
        "hint": "For each test: name the reagent, describe the method (including heating where needed), and state the positive colour change."
    },
    {
        "id": "OR003",
        "paper": 1,
        "topic": "Organisation",
        "subtopic": "Heart Structure & CHD",
        "question": (
            "Coronary heart disease (CHD) occurs when fatty material builds up "
            "inside the coronary arteries.\n\n"
            "Explain how CHD can cause a heart attack. [3]\n\n"
            "The cardiac output formula is:\n"
            "Cardiac output = stroke volume × heart rate\n\n"
            "A patient has a cardiac output of 4800 cm³/min and a heart rate of 80 beats/min. "
            "Calculate the stroke volume. Include the unit in your answer. [2]"
        ),
        "marks": 5,
        "command_word": "Explain / Calculate",
        "mark_scheme": (
            "Explain CHD (3 marks):\n"
            "• Fatty deposits / plaques build up in the coronary arteries, "
            "narrowing them / reducing blood flow [1]\n"
            "• Less / no oxygen (and glucose) is delivered to heart muscle cells [1]\n"
            "• Heart muscle cells cannot respire aerobically / cells die / "
            "heart muscle stops contracting effectively → heart attack [1]\n\n"
            "Calculate stroke volume (2 marks):\n"
            "• Correct rearrangement: stroke volume = cardiac output ÷ heart rate [1]\n"
            "• = 4800 ÷ 80 = 60 cm³ (per beat) — unit required [1]\n"
            "Accept cm³/beat or cm³. Penalise wrong unit only once."
        ),
        "priority": "⭐ High — CHD 6/8, cardiac output 1/8 Paper 1 papers",
        "hint": "For CHD: fatty deposits → blocked artery → no O₂ → cells die. For calculation, rearrange the formula."
    },
    {
        "id": "OR004",
        "paper": 1,
        "topic": "Organisation",
        "subtopic": "Villi Adaptation",
        "question": (
            "Describe how the small intestine is adapted for efficient absorption "
            "of digested food molecules into the bloodstream."
        ),
        "marks": 4,
        "command_word": "Describe",
        "mark_scheme": (
            "Award 1 mark each for four of:\n"
            "• Covered in villi / microvilli → very large surface area for absorption [1]\n"
            "• Walls of villi are only one cell thick / thin walls → short diffusion pathway [1]\n"
            "• Rich blood supply / capillaries inside each villus → maintains concentration gradient / "
            "carries absorbed molecules away quickly [1]\n"
            "• Lacteals in villi absorb fatty acids and glycerol (fat digestion products) [1]\n"
            "• Villi contain mitochondria to provide ATP for active transport [1]\n"
            "Each point must link the feature to a benefit for full credit. "
            "'Large surface area' alone (without villi/microvilli) scores 0."
        ),
        "priority": "High — appears 4/8 Paper 1 papers",
        "hint": "For each adaptation: state the feature AND explain how it aids absorption."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 1 — INFECTION & RESPONSE
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "IR001",
        "paper": 1,
        "topic": "Infection & Response",
        "subtopic": "Vaccination & Immunity",
        "question": (
            "Explain how a vaccine protects a person from a disease "
            "when they are later exposed to the actual pathogen."
        ),
        "marks": 4,
        "command_word": "Explain",
        "mark_scheme": (
            "• The vaccine contains dead / weakened / inactivated pathogen or antigens [1]\n"
            "• This stimulates white blood cells (lymphocytes) to produce antibodies "
            "specific to the pathogen's antigens [1]\n"
            "• Memory cells (lymphocytes) are produced and remain in the body [1]\n"
            "• On future exposure to the pathogen, memory cells rapidly produce large amounts "
            "of the correct antibody / respond faster than the primary response, "
            "before the pathogen can cause disease [1]\n"
            "Do NOT accept 'immune system is stimulated' without specifying white blood cells / antibodies. "
            "Memory cells must be linked to RAPID or LARGE response for mark 4."
        ),
        "priority": "⭐ High — appears in every Paper 1 (8/8)",
        "hint": "Think: vaccine → white blood cells stimulated → antibodies made → memory cells stored → rapid response on re-exposure."
    },
    {
        "id": "IR002",
        "paper": 1,
        "topic": "Infection & Response",
        "subtopic": "Pathogens — Types & Control",
        "question": (
            "Match each disease to the correct type of pathogen.\n\n"
            "Diseases: Malaria, Salmonella food poisoning, Measles, Athlete's foot\n\n"
            "Pathogen types: Bacterium, Virus, Fungus, Protist\n\n"
            "Then for malaria, give two methods used to reduce its spread and explain why each is effective."
        ),
        "marks": 6,
        "command_word": "Match / Give / Explain",
        "mark_scheme": (
            "Matching (1 mark each, 4 marks total):\n"
            "• Malaria — Protist [1]\n"
            "• Salmonella food poisoning — Bacterium [1]\n"
            "• Measles — Virus [1]\n"
            "• Athlete's foot — Fungus [1]\n\n"
            "Malaria control (1 mark method + 1 mark explanation, any two methods):\n"
            "• Mosquito nets / bed nets → prevent mosquitoes biting sleeping people, "
            "reducing transmission of protist [1+1]\n"
            "• Insecticide / pesticide spraying → kills mosquitoes, reducing vector population [1+1]\n"
            "• Draining standing water / removing water-filled containers → "
            "removes mosquito breeding sites, reducing population [1+1]\n"
            "• Antimalarial drugs → kill the protist inside the human body [1+1]\n"
            "Award max 2 marks for malaria control section."
        ),
        "priority": "⭐ High — appears in every Paper 1 (8/8)",
        "hint": "Remember: malaria = protist (transmitted by mosquito); the other three are common."
    },
    {
        "id": "IR003",
        "paper": 1,
        "topic": "Infection & Response",
        "subtopic": "Antibiotic Resistance",
        "question": (
            "Explain why the development of antibiotic-resistant bacteria "
            "is a serious threat to human health. "
            "Include an explanation of how antibiotic resistance develops in your answer."
        ),
        "marks": 5,
        "command_word": "Explain",
        "mark_scheme": (
            "How resistance develops (natural selection — max 3 marks):\n"
            "• Mutation occurs in bacteria producing a resistant variant [1]\n"
            "• When antibiotics are used, non-resistant bacteria are killed / "
            "resistant bacteria survive and reproduce [1]\n"
            "• Resistance allele is passed on to offspring (inherited) / "
            "frequency of resistant bacteria increases over generations [1]\n\n"
            "Why this is a threat (max 2 marks):\n"
            "• Infections caused by resistant bacteria cannot be treated with existing antibiotics [1]\n"
            "• New antibiotics are difficult / expensive / slow to develop; "
            "resistance may spread faster than new drugs are created [1]\n"
            "• Resistant strains (e.g. MRSA) can spread between people / "
            "hospital-acquired infections become untreatable [1]\n"
            "Award max 5 marks total."
        ),
        "priority": "⭐ High — appears 5/8 Paper 1 papers + related in Paper 2",
        "hint": "Two parts: (1) how resistance evolves via natural selection; (2) why this is dangerous for treating disease."
    },
    {
        "id": "IR004",
        "paper": 1,
        "topic": "Infection & Response",
        "subtopic": "Drug Development & Clinical Trials",
        "question": (
            "Before a new drug can be prescribed to patients, it must go through clinical trials.\n\n"
            "(a) Describe the stages of drug testing before a clinical trial begins. [2]\n\n"
            "(b) In Phase 1 of a clinical trial, the drug is tested on a small group of healthy volunteers "
            "using a very low dose.\n\n"
            "Suggest why:\n"
            "(i) Healthy volunteers are used rather than patients. [1]\n"
            "(ii) A very low dose is used. [1]"
        ),
        "marks": 4,
        "command_word": "Describe / Suggest",
        "mark_scheme": (
            "(a) Pre-clinical testing:\n"
            "• Tested on cells / cell cultures / in the lab / in vitro [1]\n"
            "• Then tested on animals (to check for toxicity, efficacy, and suitable dose) [1]\n\n"
            "(b)(i) Healthy volunteers used because:\n"
            "• Any side effects can be detected without confusion with symptoms of a disease / "
            "easier to identify side effects caused by the drug alone [1]\n"
            "Accept: ethical reasons (not ethical to give untested drug to sick people)\n\n"
            "(b)(ii) Low dose used because:\n"
            "• To check for safety / adverse effects at the lowest possible dose / "
            "to avoid harming volunteers [1]"
        ),
        "priority": "High — appears 5/8 Paper 1 papers",
        "hint": "Pre-clinical = cells then animals. Phase 1 = healthy volunteers, low dose for safety."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 1 — BIOENERGETICS
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "BE001",
        "paper": 1,
        "topic": "Bioenergetics",
        "subtopic": "Photosynthesis — Equation & Limiting Factors",
        "question": (
            "Write the balanced symbol equation for photosynthesis. [1]\n\n"
            "A student grew a plant in a greenhouse and measured the rate of photosynthesis "
            "at different light intensities. The results showed that the rate increased "
            "up to 800 lux, then stayed constant despite further increases in light intensity.\n\n"
            "Suggest two factors that could be limiting the rate of photosynthesis "
            "at light intensities above 800 lux. [2]\n\n"
            "Explain why the minimum light intensity for maximum rate of photosynthesis "
            "may not be the most profitable light intensity to use in a greenhouse. [2]"
        ),
        "marks": 5,
        "command_word": "Write / Suggest / Explain",
        "mark_scheme": (
            "Equation: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂ [1]\n"
            "(Accept word equation: carbon dioxide + water → glucose + oxygen; must be balanced or equivalent)\n\n"
            "Limiting factors at high light (any 2):\n"
            "• CO₂ concentration [1]\n"
            "• Temperature / enzyme activity [1]\n"
            "• Water availability [1]\n\n"
            "Why minimum light intensity may not be most profitable (2 marks):\n"
            "• Cost of providing lighting / electricity may exceed extra income from increased yield [1]\n"
            "• Other factors (CO₂/temperature) are limiting so more light has no extra benefit [1]\n"
            "Must refer to cost or economic factor for first mark. Must give a logical reason."
        ),
        "priority": "⭐ High — photosynthesis appears in every Paper 1 (8/8)",
        "hint": "Symbol equation needs correct formulae and balancing. Limiting factors: CO₂, temperature (not light — that's already saturating)."
    },
    {
        "id": "BE002",
        "paper": 1,
        "topic": "Bioenergetics",
        "subtopic": "Photosynthesis — Pondweed Investigation",
        "question": (
            "A student used aquatic pondweed to investigate how light intensity affects "
            "the rate of photosynthesis. She counted the number of bubbles produced per minute "
            "at different distances from the lamp.\n\n"
            "(a) Identify one variable the student should control to make the investigation valid. "
            "Explain why this variable should be controlled. [2]\n\n"
            "(b) Suggest two improvements to the method to measure the rate of photosynthesis "
            "more accurately. [2]\n\n"
            "(c) The student places the lamp 20 cm from the plant and records 40 bubbles/min. "
            "Predict the number of bubbles per minute when the lamp is moved to 40 cm. "
            "Use the inverse square law in your answer. [3]"
        ),
        "marks": 7,
        "command_word": "Identify / Suggest / Predict",
        "mark_scheme": (
            "(a) Any one control variable + valid explanation:\n"
            "• Temperature — temperature affects enzyme activity and therefore the rate of "
            "photosynthesis independently of light intensity [1+1]\n"
            "• CO₂ concentration — CO₂ is a reactant and limiting factor [1+1]\n"
            "• Type/species of plant — different plants may have different rates [1+1]\n\n"
            "(b) Any two improvements:\n"
            "• Collect the gas in a graduated/calibrated tube/syringe to measure volume "
            "rather than count bubbles (bubbles may vary in size) [1]\n"
            "• Time for a set volume of gas to be produced (rather than count bubbles per minute) [1]\n"
            "• Use a light meter to measure actual light intensity at each distance [1]\n"
            "• Repeat and take mean to reduce effect of random error [1]\n\n"
            "(c) Inverse square law: I ∝ 1/d²\n"
            "• At 20 cm: I ∝ 1/400; at 40 cm: I ∝ 1/1600 [1]\n"
            "• Light intensity at 40 cm = ¼ of that at 20 cm (distance doubled → intensity quartered) [1]\n"
            "• Predicted bubbles = 40 × ¼ = 10 bubbles/min [1]\n"
            "Award 2 marks if correct answer (10) given with partial working. "
            "Award 1 mark if method is correct but arithmetic error."
        ),
        "priority": "⭐ High — appears in every Paper 1 (8/8)",
        "hint": "Inverse square law: doubling distance quarters intensity (I ∝ 1/d²). So 40 bubbles at 20cm → 10 at 40cm."
    },
    {
        "id": "BE003",
        "paper": 1,
        "topic": "Bioenergetics",
        "subtopic": "Respiration — Aerobic & Anaerobic",
        "question": (
            "During vigorous exercise, the body switches from aerobic to anaerobic respiration "
            "in the muscles.\n\n"
            "(a) Write the word equation for anaerobic respiration in human muscles. [1]\n\n"
            "(b) After vigorous exercise, a person continues to breathe heavily for several minutes. "
            "Explain why, using the concept of oxygen debt. [4]"
        ),
        "marks": 5,
        "command_word": "Write / Explain",
        "mark_scheme": (
            "(a) glucose → lactic acid [1]\n"
            "(Must be word equation — not symbol. 'Lactate' accepted.)\n\n"
            "(b) Oxygen debt explanation (max 4 marks):\n"
            "• During exercise, muscles respire anaerobically and lactic acid builds up [1]\n"
            "• Lactic acid must be broken down / oxidised / converted to glucose (via liver) — "
            "this requires oxygen / creates an oxygen debt [1]\n"
            "• After exercise, continued heavy breathing supplies extra oxygen [1]\n"
            "• To repay the oxygen debt / to break down the lactic acid / "
            "restore normal conditions [1]\n"
            "Accept: 'heart rate remains elevated to deliver oxygen to tissues'."
        ),
        "priority": "High — appears 4/8 Paper 1 papers",
        "hint": "Anaerobic equation: glucose → lactic acid. Oxygen debt = the oxygen needed after exercise to break down the lactic acid that built up."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 1 — TRANSPORT IN PLANTS
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "TP001",
        "paper": 1,
        "topic": "Organisation",
        "subtopic": "Transport in Plants — Xylem & Phloem",
        "question": (
            "Describe how water moves from the soil to the atmosphere through a plant. "
            "Include the names of tissues involved in your answer."
        ),
        "marks": 4,
        "command_word": "Describe",
        "mark_scheme": (
            "• Water enters root hair cells by osmosis (down a water potential gradient) [1]\n"
            "• Water moves across the root cells into the xylem [1]\n"
            "• Water moves up the xylem (to the leaves) / transpiration stream [1]\n"
            "• Water evaporates from the leaf cells / is lost through the stomata "
            "by transpiration / diffusion [1]\n"
            "Must mention xylem for mark 3. Must mention stomata or transpiration for mark 4. "
            "Accept 'phloem' in place of xylem only if explained as an error — "
            "xylem is correct here."
        ),
        "priority": "High — appears 4/8 Paper 1 papers",
        "hint": "Root hair cells → osmosis → xylem → leaves → stomata → transpiration."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 2 — HOMEOSTASIS & RESPONSE
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "HR001",
        "paper": 2,
        "topic": "Homeostasis & Response",
        "subtopic": "Blood Glucose Control — Insulin & Glucagon",
        "question": (
            "A person eats a large meal containing a lot of carbohydrates. "
            "Describe and explain how the body keeps blood glucose concentration "
            "within the normal range during the 3 hours after the meal.\n\n"
            "In your answer, name the hormones involved and describe the role of the liver."
        ),
        "marks": 6,
        "command_word": "Describe / Explain",
        "mark_scheme": (
            "Max 6 marks from:\n"
            "After the meal — blood glucose rises:\n"
            "• Pancreas detects rise in blood glucose [1]\n"
            "• Insulin is released from the pancreas [1]\n"
            "• Insulin causes cells (liver and muscle) to take up glucose [1]\n"
            "• Liver converts glucose to glycogen for storage (glycogenesis) [1]\n"
            "• Blood glucose concentration falls back to normal [1]\n\n"
            "If blood glucose falls too low:\n"
            "• Pancreas releases glucagon [1]\n"
            "• Glucagon causes the liver to convert glycogen back to glucose (glycogenolysis) [1]\n"
            "• Blood glucose rises back to normal [1]\n\n"
            "Negative feedback concept:\n"
            "• This is an example of negative feedback — changes are detected and reversed [1]\n\n"
            "Award max 6 marks. Must name insulin AND glucagon for full credit. "
            "Must mention liver role specifically."
        ),
        "priority": "⭐ High — appears 7/8 Paper 2 papers",
        "hint": "Structure: rise detected → insulin released → liver stores glucose as glycogen → level normalises. Then: falls → glucagon → glycogen→glucose → normalises."
    },
    {
        "id": "HR002",
        "paper": 2,
        "topic": "Homeostasis & Response",
        "subtopic": "Nervous System — Reflex Arc",
        "question": (
            "A person touches a hot surface and quickly pulls their hand away. "
            "This is a reflex action.\n\n"
            "(a) Describe the pathway of impulses from the stimulus to the response. "
            "Name each component in the pathway. [4]\n\n"
            "(b) Explain why a reflex action is faster than a voluntary (conscious) action. [1]\n\n"
            "(c) Explain how information travels differently along a neurone compared "
            "to across a synapse. [2]"
        ),
        "marks": 7,
        "command_word": "Describe / Explain",
        "mark_scheme": (
            "(a) Pathway (1 mark each, in correct order):\n"
            "• Receptor (detects stimulus — pain/heat in skin) [1]\n"
            "• Sensory neurone (carries impulse to spinal cord) [1]\n"
            "• Relay neurone (in the spinal cord) [1]\n"
            "• Motor neurone → effector/muscle (causes muscle to contract, pulling hand away) [1]\n"
            "Accept 'spinal cord' in place of relay neurone.\n\n"
            "(b) Reflex is faster because:\n"
            "• The impulse does not travel to / via the brain / takes a shorter pathway [1]\n\n"
            "(c) Information travel:\n"
            "• Along a neurone: electrical impulse / electrical signal [1]\n"
            "• Across a synapse: chemical signal / neurotransmitter is released [1]\n"
            "Must contrast electrical (neurone) with chemical (synapse) for both marks."
        ),
        "priority": "⭐ High — appears 7/8 Paper 2 papers",
        "hint": "Reflex arc order: receptor → sensory neurone → relay neurone → motor neurone → effector. Reflex is fast because it bypasses the brain."
    },
    {
        "id": "HR003",
        "paper": 2,
        "topic": "Homeostasis & Response",
        "subtopic": "Reaction Time — Required Practical",
        "question": (
            "A student carried out an investigation into reaction time using the ruler drop test. "
            "She tested whether caffeine affects reaction time.\n\n"
            "(a) Describe how the ruler drop test is used to measure reaction time. [3]\n\n"
            "(b) Give two variables the student should control in this investigation. [2]\n\n"
            "(c) The student repeated the test five times and obtained the following results "
            "in centimetres: 14, 13, 26, 12, 15.\n"
            "Identify the anomalous result and calculate the mean of the remaining results. [2]"
        ),
        "marks": 7,
        "command_word": "Describe / Give / Calculate",
        "mark_scheme": (
            "(a) Ruler drop test:\n"
            "• Participant holds their thumb and finger (open) at the zero end of the ruler / "
            "ruler held vertically between the participant's fingers [1]\n"
            "• The ruler is dropped (without warning) and the participant catches it [1]\n"
            "• The distance the ruler fell (in cm) is read at the point where the participant catches it / "
            "lower distance = faster reaction time [1]\n\n"
            "(b) Any two control variables:\n"
            "• Same person / same hand used [1]\n"
            "• Same time of day / same conditions [1]\n"
            "• No other stimulants / food consumed [1]\n"
            "• Same distance ruler is held above fingers [1]\n\n"
            "(c) Anomalous result: 26 cm [1]\n"
            "Mean of remaining four: (14 + 13 + 12 + 15) ÷ 4 = 54 ÷ 4 = 13.5 cm [1]"
        ),
        "priority": "⭐ High — appears 6/8 Paper 2 papers",
        "hint": "Ruler test: hold ruler, drop, catch. The anomaly is the outlier (26). Mean of 14, 13, 12, 15 = 13.5."
    },
    {
        "id": "HR004",
        "paper": 2,
        "topic": "Homeostasis & Response",
        "subtopic": "Menstrual Cycle Hormones",
        "question": (
            "Describe the role of each of the following hormones in the menstrual cycle. "
            "For each hormone, name where it is produced and state its target organ and effect.\n\n"
            "(a) FSH [2]\n"
            "(b) Oestrogen [2]\n"
            "(c) LH [1]\n"
            "(d) Progesterone [1]"
        ),
        "marks": 6,
        "command_word": "Describe",
        "mark_scheme": (
            "(a) FSH:\n"
            "• Produced by the pituitary gland [1]\n"
            "• Target: ovary; causes a follicle to mature / stimulates oestrogen production [1]\n\n"
            "(b) Oestrogen:\n"
            "• Produced by the ovary [1]\n"
            "• Causes the uterus lining to build up; inhibits FSH; stimulates LH release [1]\n"
            "(Either two effects for mark 2)\n\n"
            "(c) LH:\n"
            "• Produced by pituitary; causes ovulation (release of the egg) [1]\n\n"
            "(d) Progesterone:\n"
            "• Produced by the corpus luteum (after ovulation); maintains the uterus lining [1]\n"
            "Accept 'ovary' for progesterone source."
        ),
        "priority": "⭐ High — appears 6/8 Paper 2 papers",
        "hint": "FSH (pituitary → ovary), Oestrogen (ovary → uterus), LH (pituitary → triggers ovulation), Progesterone (corpus luteum → maintains lining)."
    },
    {
        "id": "HR005",
        "paper": 2,
        "topic": "Homeostasis & Response",
        "subtopic": "IVF — Fertility Treatment",
        "question": (
            "A couple are having IVF (in vitro fertilisation) treatment.\n\n"
            "(a) Name the two hormones given to the woman at the start of IVF treatment "
            "and explain why they are given. [2]\n\n"
            "(b) Describe the steps that take place after the hormones are given "
            "to achieve a pregnancy. [4]"
        ),
        "marks": 6,
        "command_word": "Name / Explain / Describe",
        "mark_scheme": (
            "(a) Hormones (1 mark each):\n"
            "• FSH — to stimulate multiple follicles to mature / "
            "to produce more eggs than normal [1]\n"
            "• LH — to trigger ovulation / release of mature eggs [1]\n\n"
            "(b) Steps (1 mark each, max 4):\n"
            "• Eggs are collected / removed from the ovaries by a minor surgical procedure [1]\n"
            "• Eggs are fertilised with sperm in a laboratory dish / in vitro [1]\n"
            "• Fertilised eggs develop into embryos (over several days) [1]\n"
            "• One or two embryos are checked for genetic conditions / screened [1]\n"
            "• One (or two) healthy embryo(s) is transferred / implanted into the uterus [1]\n"
            "Award max 4 marks for part (b). Must be in logical order."
        ),
        "priority": "⭐ High — appears 6/8 Paper 2 papers",
        "hint": "FSH = stimulate multiple eggs; LH = trigger release. Then: collect eggs → fertilise in lab → embryo → implant."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 2 — INHERITANCE, VARIATION & EVOLUTION
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "IVE001",
        "paper": 2,
        "topic": "Inheritance, Variation & Evolution",
        "subtopic": "Punnett Square — Genetic Disorder",
        "question": (
            "Cystic fibrosis is caused by a recessive allele (f). "
            "The dominant allele is F.\n\n"
            "Two parents who are both carriers of cystic fibrosis have children.\n\n"
            "(a) Complete a Punnett square to show the possible genotypes of their offspring. [2]\n\n"
            "(b) State the probability that a child will have cystic fibrosis. [1]\n\n"
            "(c) State the probability that a child will be a carrier but not have cystic fibrosis. [1]"
        ),
        "marks": 4,
        "command_word": "Complete / State",
        "mark_scheme": (
            "(a) Punnett square:\n"
            "Parents: Ff × Ff\n"
            "Correct parental gametes shown: F and f on both sides [1]\n"
            "Correct offspring: FF, Ff, Ff, ff [1]\n"
            "(Both marks for correct grid; 1 mark if gametes shown but one offspring error)\n\n"
            "(b) Probability of cystic fibrosis (ff): 1 in 4 / 25% / 0.25 [1]\n\n"
            "(c) Probability of carrier (Ff): 2 in 4 / 1 in 2 / 50% / 0.5 [1]\n"
            "Accept any correct equivalent fraction, decimal or percentage."
        ),
        "priority": "⭐ High — Punnett squares appear 7/8 Paper 2 papers",
        "hint": "Both parents are Ff (carriers). Cross Ff × Ff. Results: 1 FF : 2 Ff : 1 ff. ff = affected (¼); Ff = carrier (½)."
    },
    {
        "id": "IVE002",
        "paper": 2,
        "topic": "Inheritance, Variation & Evolution",
        "subtopic": "Natural Selection & Evolution",
        "question": (
            "A population of mice lives in a snowy environment. "
            "Most mice are brown, but some have a mutation that gives them white fur.\n\n"
            "Explain how the white-furred mice could become the dominant variety "
            "in the population over many generations. "
            "Use the theory of natural selection in your answer."
        ),
        "marks": 5,
        "command_word": "Explain",
        "mark_scheme": (
            "Award marks for these points in a logical sequence:\n"
            "• There is variation in fur colour within the mouse population [1]\n"
            "• White mice are better camouflaged in snow / less visible to predators [1]\n"
            "• White mice are more likely to survive (to reproductive age) [1]\n"
            "• White mice are more likely to reproduce and pass on the white fur allele "
            "to their offspring [1]\n"
            "• Over many generations, the frequency of the white fur allele increases "
            "in the population [1]\n"
            "Answers must show a logical progression from variation → survival advantage → "
            "reproduction → change in allele frequency. Do NOT award marks for points "
            "stated without biological cause-and-effect linkage."
        ),
        "priority": "⭐ High — natural selection appears 7/8 Paper 2 papers",
        "hint": "Always follow: variation → selection pressure → survival advantage → reproduction → inheritance → allele frequency increases over generations."
    },
    {
        "id": "IVE003",
        "paper": 2,
        "topic": "Inheritance, Variation & Evolution",
        "subtopic": "Classification — Three Domain System",
        "question": (
            "(a) Name the three domains in the three-domain classification system. [1]\n\n"
            "(b) A scientist finds a microorganism living in a hot spring at 95°C. "
            "The microorganism has a cell wall but no membrane-bound nucleus, "
            "and its cell wall has a different chemical composition to bacteria.\n\n"
            "Suggest which domain this microorganism belongs to. Give a reason. [2]\n\n"
            "(c) State three types of evidence used by scientists today to classify organisms. [3]"
        ),
        "marks": 6,
        "command_word": "Name / Suggest / State",
        "mark_scheme": (
            "(a) Three domains: Archaea, Bacteria, Eukaryota [1] (all three required)\n\n"
            "(b) Domain: Archaea [1]\n"
            "Reason: Archaea survive in extreme environments / "
            "have a different cell wall to bacteria / "
            "no membrane-bound nucleus (like bacteria) but chemically distinct [1]\n"
            "Accept any valid reason that links to a feature of Archaea.\n\n"
            "(c) Any three of:\n"
            "• DNA sequence analysis [1]\n"
            "• Amino acid sequence comparison [1]\n"
            "• Biochemical analysis / comparison of biochemistry [1]\n"
            "• Morphological / physical features (as additional evidence) [1]\n"
            "Do NOT accept 'fossil evidence' — that is for evolutionary relationships, "
            "not current classification."
        ),
        "priority": "⭐ High — appears 6/8 Paper 2 papers",
        "hint": "Three domains: Archaea, Bacteria, Eukaryota. Archaea = extreme environments, different cell wall chemistry. Modern classification uses DNA/amino acid sequences."
    },
    {
        "id": "IVE004",
        "paper": 2,
        "topic": "Inheritance, Variation & Evolution",
        "subtopic": "Selective Breeding",
        "question": (
            "A farmer wants to breed cattle that produce more milk.\n\n"
            "(a) Describe the steps involved in a selective breeding programme "
            "to achieve this. [3]\n\n"
            "(b) Give one disadvantage of selective breeding. [1]"
        ),
        "marks": 4,
        "command_word": "Describe / Give",
        "mark_scheme": (
            "(a) Selective breeding steps (1 mark each, must be in logical order):\n"
            "• Identify / select the individuals with the desired characteristic "
            "(highest milk yield) [1]\n"
            "• Breed these selected individuals together [1]\n"
            "• Select the offspring with the best milk yield and breed them again / "
            "repeat over many generations until the desired trait is established [1]\n\n"
            "(b) Disadvantage (any one of):\n"
            "• Reduced genetic variation / reduced gene pool [1]\n"
            "• Inbreeding can lead to recessive genetic diseases becoming more common [1]\n"
            "• If environment changes, less variation to adapt / greater risk of extinction [1]\n"
            "Accept any biologically valid disadvantage."
        ),
        "priority": "High — appears 4/8 Paper 2 papers",
        "hint": "Steps: select → breed → select offspring → repeat. Disadvantage = reduced genetic variation."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 2 — ECOLOGY
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "EC001",
        "paper": 2,
        "topic": "Ecology",
        "subtopic": "Quadrat Sampling — Population Estimate",
        "question": (
            "A student used quadrats to estimate the population of daisies in a field.\n\n"
            "The field has a total area of 5000 m². "
            "The student placed 20 quadrats, each with an area of 0.25 m², randomly across the field. "
            "The mean number of daisies per quadrat was 7.\n\n"
            "(a) Explain how the student should place the quadrats randomly. [2]\n\n"
            "(b) Calculate the estimated population of daisies in the field. "
            "Show your working. [3]"
        ),
        "marks": 5,
        "command_word": "Explain / Calculate",
        "mark_scheme": (
            "(a) Random placement:\n"
            "• Use a random number generator / random number table to generate coordinates [1]\n"
            "• Place the quadrat at the co-ordinate position / "
            "do not choose where to place them (avoid bias) [1]\n"
            "Accept: 'throw quadrat over shoulder' as a random method (with caveat — "
            "not truly random but accepted at GCSE).\n\n"
            "(b) Population estimate calculation:\n"
            "• Method: (mean per quadrat / area of quadrat) × total area [1]\n"
            "OR: mean per m² × total area\n"
            "• Mean per m² = 7 ÷ 0.25 = 28 daisies/m² [1]\n"
            "• Estimated population = 28 × 5000 = 140 000 daisies [1]\n"
            "Award 2 marks if correct answer (140 000) with partial working shown. "
            "Award 1 mark if correct method shown but arithmetic error."
        ),
        "priority": "⭐ High — appears 7/8 Paper 2 papers",
        "hint": "Population = (mean per quadrat ÷ quadrat area) × total area = (7 ÷ 0.25) × 5000."
    },
    {
        "id": "EC002",
        "paper": 2,
        "topic": "Ecology",
        "subtopic": "Biotic & Abiotic Factors",
        "question": (
            "A student investigated the distribution of daisy plants in a field. "
            "She found daisies were more common near the fence than in the middle of the field.\n\n"
            "Suggest two biotic factors and two abiotic factors that could explain "
            "the distribution of the daisies. "
            "For each factor, explain how it would affect the daisies' distribution."
        ),
        "marks": 4,
        "command_word": "Suggest / Explain",
        "mark_scheme": (
            "Award 1 mark per factor (name) + must explain the effect:\n"
            "Biotic factors (any two):\n"
            "• Competition — more competition from grass/other plants in the middle → "
            "fewer daisies [1]\n"
            "• Grazing — more grazing by animals in the open field → fewer daisies survive [1]\n"
            "• Disease — more pathogen spread in densely planted areas [1]\n\n"
            "Abiotic factors (any two):\n"
            "• Light intensity — more shade near the fence / less competition for light near fence [1]\n"
            "• Soil moisture — different moisture levels near fence affect growth [1]\n"
            "• Temperature — microclimate differences near fence [1]\n"
            "• Soil pH / nutrients — different near fence [1]\n"
            "Each mark requires factor + effect. Factor name alone = 0."
        ),
        "priority": "⭐ High — appears 7/8 Paper 2 papers",
        "hint": "Biotic = living (competition, predation, disease). Abiotic = non-living (light, temperature, moisture, pH). Must explain effect for each."
    },
    {
        "id": "EC003",
        "paper": 2,
        "topic": "Ecology",
        "subtopic": "Carbon Cycle & Human Impact",
        "question": (
            "Describe the carbon cycle, explaining how carbon moves through living organisms "
            "and is returned to the atmosphere."
        ),
        "marks": 6,
        "command_word": "Describe / Explain",
        "mark_scheme": (
            "Award 1 mark each for up to 6 of the following:\n"
            "• CO₂ is removed from the atmosphere by plants during photosynthesis [1]\n"
            "• Carbon is incorporated into organic molecules / glucose / "
            "used to make carbohydrates, proteins, fats in plants [1]\n"
            "• Carbon passes along food chains when animals eat plants (and other animals) [1]\n"
            "• Carbon is returned to the atmosphere as CO₂ during respiration "
            "(by plants, animals and decomposers) [1]\n"
            "• When organisms die, decomposers (bacteria and fungi) break down "
            "the organic material [1]\n"
            "• Decomposers release CO₂ via respiration / decomposition [1]\n"
            "• Combustion of fossil fuels / wood releases stored carbon as CO₂ [1]\n"
            "Award max 6 marks. Must mention photosynthesis AND respiration "
            "for a balanced answer to score 5+."
        ),
        "priority": "⭐ High — appears 5/8 Paper 2 papers",
        "hint": "Circle: photosynthesis removes CO₂ → passes through food chains → respiration returns CO₂ → decomposers return CO₂ → combustion returns CO₂."
    },
    {
        "id": "EC004",
        "paper": 2,
        "topic": "Ecology",
        "subtopic": "Deforestation & Environmental Impact",
        "question": (
            "Deforestation is increasing in many parts of the world.\n\n"
            "Describe two reasons why deforestation occurs and explain "
            "two effects of deforestation on the environment."
        ),
        "marks": 4,
        "command_word": "Describe / Explain",
        "mark_scheme": (
            "Reasons for deforestation (any two, 1 mark each):\n"
            "• To create agricultural land for crops / cattle farming [1]\n"
            "• To grow crops for biofuels [1]\n"
            "• To provide timber / wood for building / paper production [1]\n"
            "• To build settlements / infrastructure [1]\n\n"
            "Effects on environment (any two, 1 mark each):\n"
            "• Less CO₂ absorbed by photosynthesis → increased atmospheric CO₂ → "
            "enhanced greenhouse effect / global warming [1]\n"
            "• CO₂ released when trees are burned / decompose [1]\n"
            "• Loss of biodiversity / habitat destruction → species extinction [1]\n"
            "• Increased risk of flooding / soil erosion (trees no longer hold soil/water) [1]\n"
            "Each effect must have a causal explanation to score the mark."
        ),
        "priority": "High — appears 4/8 Paper 2 papers",
        "hint": "Reasons: farming, cattle, biofuels, timber. Effects: CO₂ increase, biodiversity loss, flooding, soil erosion."
    },
    {
        "id": "EC005",
        "paper": 2,
        "topic": "Ecology",
        "subtopic": "Climate Change & Global Warming",
        "question": (
            "Scientists have recorded an increase in average global temperature over the last century.\n\n"
            "(a) Name two greenhouse gases other than CO₂. [2]\n\n"
            "(b) Give two consequences of global warming for living organisms. [2]"
        ),
        "marks": 4,
        "command_word": "Name / Give",
        "mark_scheme": (
            "(a) Any two of:\n"
            "• Methane (CH₄) [1]\n"
            "• Nitrous oxide / N₂O [1]\n"
            "• Water vapour [1]\n"
            "Do NOT accept CO₂ (already given) or 'ozone' alone.\n\n"
            "(b) Any two consequences:\n"
            "• Changes in species distribution / migration patterns "
            "(species move to cooler regions / poles) [1]\n"
            "• Changes in timing of migration / breeding seasons [1]\n"
            "• Rising sea levels → loss of coastal habitat [1]\n"
            "• More extreme weather events (droughts, floods) → habitat destruction [1]\n"
            "• Melting of polar ice → habitat loss for polar species [1]\n"
            "Accept any biologically valid consequence with enough detail."
        ),
        "priority": "⭐ High — appears 5/8 Paper 2 papers",
        "hint": "Greenhouse gases (other than CO₂): methane, nitrous oxide, water vapour. Effects: species range shifts, sea level rise, extreme weather."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 1 — CELL BIOLOGY (continued)
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "CB006",
        "paper": 1,
        "topic": "Cell Biology",
        "subtopic": "Osmosis — Required Practical",
        "question": (
            "A student investigated osmosis using potato cylinders.\n\n"
            "She cut five cylinders of equal length and mass, then placed each in a "
            "different sucrose solution (0.0 M, 0.2 M, 0.4 M, 0.6 M, 0.8 M) for 30 minutes.\n\n"
            "(a) State two variables the student must control to make this a fair test. [2]\n\n"
            "(b) The cylinder in 0.0 M solution gained 0.4 g in mass. "
            "The original mass was 2.0 g. Calculate the percentage change in mass. [2]\n\n"
            "(c) Explain why the cylinder in 0.8 M solution lost mass. [3]"
        ),
        "marks": 7,
        "command_word": "State / Calculate / Explain",
        "mark_scheme": (
            "(a) Any two of (1 mark each):\n"
            "• Temperature of solution [1]\n"
            "• Length / surface area of potato cylinder [1]\n"
            "• Volume / concentration of sucrose solution [1]\n"
            "• Time left in solution [1]\n"
            "• Species / type of potato [1]\n\n"
            "(b)\n"
            "• % change = (change in mass ÷ original mass) × 100 [1]\n"
            "• = (0.4 ÷ 2.0) × 100 = +20% [1]\n"
            "Award 1 mark if formula correct but arithmetic error leads to wrong answer (show working).\n\n"
            "(c)\n"
            "• The sucrose solution is more concentrated than the cell sap / "
            "the water potential of the solution is lower than the cell [1]\n"
            "• Water moves out of the cell by osmosis [1]\n"
            "• Down the water potential gradient / from higher to lower water potential [1]\n"
            "Must mention osmosis to score 2nd mark. Do NOT credit 'diffusion'."
        ),
        "priority": "⭐ High — required practical, appears every year",
        "hint": "% change = (change ÷ original) × 100. Osmosis = water moves from high to low water potential."
    },
    {
        "id": "CB007",
        "paper": 1,
        "topic": "Cell Biology",
        "subtopic": "Stem Cells",
        "question": (
            "Evaluate the use of embryonic stem cells in medicine.\n\n"
            "Your answer should include the potential benefits and ethical concerns "
            "of using embryonic stem cells."
        ),
        "marks": 6,
        "command_word": "Evaluate",
        "mark_scheme": (
            "This is a 6-mark extended writing question. Mark using levels:\n\n"
            "Level 3 (5–6 marks): Detailed, balanced account with both benefits and concerns, "
            "using scientific terminology correctly.\n"
            "Level 2 (3–4 marks): Some discussion of benefits and concerns but lacks balance or detail.\n"
            "Level 1 (1–2 marks): Basic statements about stem cells with little evaluation.\n\n"
            "Credit points (any combination):\n"
            "Benefits:\n"
            "• Embryonic stem cells are pluripotent — can differentiate into any cell type [1]\n"
            "• Could be used to treat/replace damaged tissues (e.g. Parkinson's, diabetes, spinal injury) [1]\n"
            "• Could provide replacement organs reducing transplant waiting lists [1]\n"
            "• Therapeutic cloning removes risk of rejection (genetically matched) [1]\n\n"
            "Ethical concerns:\n"
            "• Embryo is destroyed in the process — some consider this taking a human life [1]\n"
            "• Embryos cannot give consent [1]\n"
            "• Religious objections to 'playing God' / interfering with natural development [1]\n"
            "• Risk of uncontrolled cell division / tumour formation [1]\n\n"
            "Conclusion/evaluation:\n"
            "• Weighs benefits against concerns with a justified conclusion [1]\n"
            "• Mentions adult stem cells as an alternative with fewer ethical issues [1]"
        ),
        "priority": "⭐ High — 6-mark evaluate question, appears 4/8 papers",
        "hint": "Benefits: pluripotent, treat disease, therapeutic cloning. Concerns: embryo destruction, consent, religion, tumour risk."
    },
    {
        "id": "CB008",
        "paper": 1,
        "topic": "Cell Biology",
        "subtopic": "Diffusion & Active Transport",
        "question": (
            "(a) State the definition of diffusion. [2]\n\n"
            "(b) Explain why the villi in the small intestine are well adapted for the absorption "
            "of glucose by diffusion. Give three adaptations. [3]\n\n"
            "(c) Glucose can also be absorbed from the small intestine by active transport. "
            "Give one difference between diffusion and active transport. [1]"
        ),
        "marks": 6,
        "command_word": "State / Explain / Give",
        "mark_scheme": (
            "(a)\n"
            "• Diffusion is the net movement of particles [1]\n"
            "• from an area of higher concentration to an area of lower concentration [1]\n"
            "(Both marks needed for full definition; accept 'down a concentration gradient'.)\n\n"
            "(b) Any three of (1 mark each):\n"
            "• Large surface area (many villi / microvilli / large total area) [1]\n"
            "• Rich blood supply / capillary network maintains concentration gradient [1]\n"
            "• Thin walls (one cell thick) — short diffusion distance [1]\n"
            "• Villi are long / finger-like — increase surface area [1]\n\n"
            "(c) Any one of:\n"
            "• Active transport requires energy (ATP) / diffusion does not [1]\n"
            "• Active transport moves substances against the concentration gradient; "
            "diffusion moves with the gradient [1]"
        ),
        "priority": "⭐ High — appears 6/8 Paper 1 papers",
        "hint": "Diffusion: net movement, high to low concentration. Villi adaptations: SA, thin walls, blood supply."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 1 — ORGANISATION (continued)
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "OR005",
        "paper": 1,
        "topic": "Organisation",
        "subtopic": "Enzymes — Required Practical (pH & amylase)",
        "question": (
            "A student investigated the effect of pH on the rate of amylase activity.\n\n"
            "She added starch solution and amylase to a spotting tile. "
            "Every 30 seconds she placed a drop of the mixture onto iodine solution.\n\n"
            "(a) What colour change would indicate that starch has been completely broken down? [1]\n\n"
            "(b) The student repeated the experiment at pH 4, 6, 7, 8, and 10. "
            "She measured the time taken for starch to be fully digested. "
            "Explain why amylase works fastest at pH 7 and hardly at all at pH 4. [4]"
        ),
        "marks": 5,
        "command_word": "State / Explain",
        "mark_scheme": (
            "(a)\n"
            "• Iodine stays orange-brown / does not turn blue-black [1]\n\n"
            "(b)\n"
            "• Enzymes have an active site with a specific shape [1]\n"
            "• At pH 7 the active site is the complementary shape to the substrate (starch) — "
            "enzyme-substrate complex forms efficiently [1]\n"
            "• At pH 4 (too acidic), H⁺ ions change the shape of the active site / "
            "enzyme is denatured [1]\n"
            "• The substrate can no longer fit / enzyme-substrate complex cannot form [1]\n"
            "Must use the term 'active site' to access marks about shape. "
            "Do NOT accept 'enzyme is destroyed' — must say 'denatured' or 'shape changes'."
        ),
        "priority": "⭐ High — enzyme required practical, every Paper 1",
        "hint": "Iodine: blue-black = starch present; orange-brown = starch gone. Denaturation = active site shape changes."
    },
    {
        "id": "OR006",
        "paper": 1,
        "topic": "Organisation",
        "subtopic": "The Heart & Circulatory System",
        "question": (
            "The diagram below shows the human heart (assume standard diagram with four chambers).\n\n"
            "(a) Name the blood vessel labelled A that carries oxygenated blood "
            "from the lungs to the heart. [1]\n\n"
            "(b) Describe the route blood takes through the heart from the vena cava "
            "to the aorta. [4]\n\n"
            "(c) Explain what is meant by a 'double circulatory system'. [2]"
        ),
        "marks": 7,
        "command_word": "Name / Describe / Explain",
        "mark_scheme": (
            "(a)\n"
            "• Pulmonary vein [1]\n\n"
            "(b) In order (1 mark each, sequence must be correct):\n"
            "• Blood enters right atrium from vena cava [1]\n"
            "• Passes through tricuspid valve into right ventricle [1]\n"
            "• Right ventricle contracts → blood pumped via pulmonary artery to lungs [1]\n"
            "• Returns via pulmonary vein to left atrium → bicuspid valve → left ventricle → aorta [1]\n"
            "Accept correct valves named. Do NOT penalise for not naming valves if route is correct.\n\n"
            "(c)\n"
            "• Blood passes through the heart twice for each complete circuit of the body [1]\n"
            "• One circuit goes to the lungs (pulmonary), the other goes to the body (systemic) [1]"
        ),
        "priority": "⭐ High — appears 5/8 Paper 1 papers",
        "hint": "Pulmonary vein = oxygenated blood TO heart. Double circulation = two loops: lungs + body."
    },
    {
        "id": "OR007",
        "paper": 1,
        "topic": "Organisation",
        "subtopic": "Coronary Heart Disease",
        "question": (
            "A patient has been diagnosed with coronary heart disease (CHD).\n\n"
            "(a) Explain how CHD develops. [3]\n\n"
            "(b) Discuss the advantages and disadvantages of treating CHD with a stent "
            "compared to using statins. [4]"
        ),
        "marks": 7,
        "command_word": "Explain / Discuss",
        "mark_scheme": (
            "(a)\n"
            "• Fatty deposits (atheroma / plaque) build up in the walls of the coronary arteries [1]\n"
            "• This narrows the lumen of the artery / restricts blood flow to the heart muscle [1]\n"
            "• The heart muscle receives less oxygen → cannot respire aerobically → "
            "may lead to a heart attack [1]\n\n"
            "(b) Stents:\n"
            "Advantage: immediate / long-lasting effect; physically widens artery; "
            "no need to take daily medication [1]\n"
            "Disadvantage: surgical risk (infection, blood clots, reaction to anaesthetic) [1]\n\n"
            "Statins:\n"
            "Advantage: non-surgical; reduces LDL cholesterol / slows plaque build-up; "
            "reduces risk of further disease [1]\n"
            "Disadvantage: must be taken daily / long term; side effects (muscle pain, liver damage); "
            "does not physically remove blockage [1]\n"
            "Award 1 mark per developed comparison point (advantage or disadvantage must be specific)."
        ),
        "priority": "High — appears 4/8 Paper 1 papers",
        "hint": "CHD: plaque → narrowed artery → less O₂ to heart muscle. Stents = physical fix; statins = chemical prevention."
    },
    {
        "id": "OR008",
        "paper": 1,
        "topic": "Organisation",
        "subtopic": "Cancer & Tumours",
        "question": (
            "(a) State what is meant by a tumour. [1]\n\n"
            "(b) Give two differences between a benign tumour and a malignant tumour. [2]\n\n"
            "(c) Name two lifestyle factors that can increase the risk of developing cancer. [2]"
        ),
        "marks": 5,
        "command_word": "State / Give / Name",
        "mark_scheme": (
            "(a)\n"
            "• A mass of abnormally / uncontrollably dividing cells [1]\n\n"
            "(b) Any two differences (1 mark each):\n"
            "• Benign tumour stays in one place / does not spread; "
            "malignant tumour spreads to other parts of the body (metastasis) [1]\n"
            "• Benign tumour has a distinct boundary; malignant tumour invades surrounding tissue [1]\n"
            "• Malignant tumour cells break off and travel through blood/lymph; benign cells do not [1]\n\n"
            "(c) Any two of:\n"
            "• Smoking / tobacco use [1]\n"
            "• Excessive alcohol consumption [1]\n"
            "• Obesity / poor diet (high fat, processed meat) [1]\n"
            "• Excessive UV exposure / sunbathing [1]\n"
            "• Lack of physical exercise [1]"
        ),
        "priority": "Medium — appears 3/8 Paper 1 papers",
        "hint": "Benign = contained; malignant = spreads (metastasis). Lifestyle risks: smoking, alcohol, obesity, UV."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 1 — INFECTION & RESPONSE (continued)
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "IR005",
        "paper": 1,
        "topic": "Infection & Response",
        "subtopic": "The Immune System",
        "question": (
            "Explain how the body's immune system responds to a bacterial infection. [6]"
        ),
        "marks": 6,
        "command_word": "Explain",
        "mark_scheme": (
            "6-mark extended writing. Mark using levels:\n\n"
            "Level 3 (5–6): Clear, detailed account covering detection, phagocytosis, "
            "lymphocyte response, and memory cells using correct scientific terminology.\n"
            "Level 2 (3–4): Partial account — covers phagocytosis and antibody production "
            "but lacks detail on memory or mechanism.\n"
            "Level 1 (1–2): Basic points about white blood cells fighting infection.\n\n"
            "Credit points:\n"
            "• Phagocytes detect and engulf (phagocytose) pathogens [1]\n"
            "• Pathogen has antigens on its surface [1]\n"
            "• Lymphocytes produce antibodies complementary to specific antigens [1]\n"
            "• Antibodies bind to antigens → pathogen clumped / destroyed [1]\n"
            "• Memory lymphocytes remain in bloodstream [1]\n"
            "• On re-infection, faster and larger antibody response prevents symptoms [1]\n"
            "• Antitoxins produced to neutralise toxins made by bacteria [1]"
        ),
        "priority": "⭐ High — 6-mark, appears 5/8 Paper 1 papers",
        "hint": "Sequence: antigens detected → phagocytes engulf → lymphocytes produce antibodies → memory cells remain."
    },
    {
        "id": "IR006",
        "paper": 1,
        "topic": "Infection & Response",
        "subtopic": "Monoclonal Antibodies",
        "question": (
            "(a) State what is meant by a monoclonal antibody. [2]\n\n"
            "(b) Describe how monoclonal antibodies can be used in the treatment of cancer. [3]\n\n"
            "(c) A pregnancy test uses monoclonal antibodies. "
            "Explain how the test produces a positive result. [2]"
        ),
        "marks": 7,
        "command_word": "State / Describe / Explain",
        "mark_scheme": (
            "(a)\n"
            "• Antibodies produced from a single clone of cells [1]\n"
            "• That are identical / specific to one antigen [1]\n\n"
            "(b)\n"
            "• Monoclonal antibodies are made that are complementary to antigens on cancer cells [1]\n"
            "• The antibodies carry a drug / toxic chemical / radioactive substance [1]\n"
            "• Delivered specifically to cancer cells → kills them / minimises damage to healthy cells [1]\n\n"
            "(c)\n"
            "• The antibodies are specific to the hCG hormone (produced in pregnancy) [1]\n"
            "• If hCG is present in urine, antibodies bind to it → triggers a colour change / "
            "visible indicator [1]"
        ),
        "priority": "High — appears 4/8 Paper 1 papers",
        "hint": "Monoclonal = identical antibodies from one clone. Cancer treatment: antibody + drug → targeted delivery."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 1 — BIOENERGETICS (continued)
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "BE004",
        "paper": 1,
        "topic": "Bioenergetics",
        "subtopic": "Respiration — Aerobic & Anaerobic",
        "question": (
            "(a) Write the word equation for aerobic respiration. [1]\n\n"
            "(b) A sprinter runs 100 m in 10 seconds. "
            "During the race, lactic acid builds up in their muscles.\n\n"
            "(i) Explain why lactic acid builds up during intense exercise. [2]\n\n"
            "(ii) After the race, the sprinter breathes heavily for several minutes. "
            "Explain why. [3]"
        ),
        "marks": 6,
        "command_word": "Write / Explain",
        "mark_scheme": (
            "(a)\n"
            "• glucose + oxygen → carbon dioxide + water [1]\n"
            "(Accept chemical equation: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O)\n\n"
            "(b)(i)\n"
            "• During intense exercise, oxygen supply to muscles is insufficient [1]\n"
            "• Muscles respire anaerobically → glucose → lactic acid (instead of CO₂ + water) [1]\n\n"
            "(b)(ii)\n"
            "• Lactic acid has built up in muscles — this is the 'oxygen debt' [1]\n"
            "• Extra oxygen needed to break down / oxidise lactic acid → glucose / CO₂ + water [1]\n"
            "• Increased breathing rate delivers more oxygen to respire the lactic acid [1]\n"
            "Accept 'repay the oxygen debt'. Must link heavy breathing to lactic acid breakdown."
        ),
        "priority": "⭐ High — appears 6/8 Paper 1 papers",
        "hint": "Aerobic: glucose + O₂ → CO₂ + water. Anaerobic: glucose → lactic acid. Oxygen debt = lactic acid breakdown."
    },
    {
        "id": "BE005",
        "paper": 1,
        "topic": "Bioenergetics",
        "subtopic": "Photosynthesis — Limiting Factors",
        "question": (
            "A student measured the rate of photosynthesis of pondweed at different "
            "light intensities, keeping CO₂ concentration and temperature constant.\n\n"
            "At low light intensity, increasing the light intensity increased the rate of photosynthesis. "
            "At high light intensity, further increases in light had no effect.\n\n"
            "(a) Explain why increasing light intensity no longer increases the rate "
            "at high light intensity. [2]\n\n"
            "(b) Suggest two ways the student could further increase the rate of "
            "photosynthesis from the plateau. [2]\n\n"
            "(c) Explain the importance of photosynthesis to ecosystems. [3]"
        ),
        "marks": 7,
        "command_word": "Explain / Suggest",
        "mark_scheme": (
            "(a)\n"
            "• A different factor is now limiting the rate [1]\n"
            "• CO₂ concentration / temperature is limiting — not enough CO₂ / enzymes "
            "working at maximum rate [1]\n\n"
            "(b) Any two of:\n"
            "• Increase CO₂ concentration [1]\n"
            "• Increase temperature (within the optimum range) [1]\n"
            "• Increase water supply [1]\n\n"
            "(c)\n"
            "• Photosynthesis produces glucose / organic compounds — provides food / energy "
            "for all organisms in the ecosystem [1]\n"
            "• Produces oxygen — needed for aerobic respiration by all organisms [1]\n"
            "• Removes CO₂ from the atmosphere — reduces the greenhouse effect / "
            "maintains atmospheric balance [1]"
        ),
        "priority": "⭐ High — limiting factors, every Paper 1",
        "hint": "Plateau = another factor is limiting (CO₂ or temperature). Importance: food/energy source, O₂ production, CO₂ removal."
    },
    {
        "id": "BE006",
        "paper": 1,
        "topic": "Bioenergetics",
        "subtopic": "Metabolism",
        "question": (
            "Metabolism is the sum of all chemical reactions in a cell or organism.\n\n"
            "(a) State one anabolic reaction that occurs in plants. [1]\n\n"
            "(b) State one catabolic reaction that occurs in all living organisms. [1]\n\n"
            "(c) Explain how exercise affects the metabolic rate of a person. [2]"
        ),
        "marks": 4,
        "command_word": "State / Explain",
        "mark_scheme": (
            "(a) Any one of:\n"
            "• Photosynthesis (converting CO₂ + H₂O → glucose) [1]\n"
            "• Synthesis of starch / cellulose / proteins / lipids / DNA from simpler molecules [1]\n\n"
            "(b) Any one of:\n"
            "• Aerobic / anaerobic respiration (breaking down glucose) [1]\n"
            "• Digestion of proteins → amino acids / starch → glucose [1]\n\n"
            "(c)\n"
            "• Exercise increases metabolic rate [1]\n"
            "• More energy needed by muscles → increased rate of aerobic respiration [1]"
        ),
        "priority": "Medium — appears 3/8 Paper 1 papers",
        "hint": "Anabolic = building up (photosynthesis, synthesis). Catabolic = breaking down (respiration, digestion)."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 1 — TRANSPORT IN PLANTS (continued)
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "TP002",
        "paper": 1,
        "topic": "Transport in Plants",
        "subtopic": "Transpiration",
        "question": (
            "A potometer is used to measure the rate of water uptake in a plant.\n\n"
            "(a) State two environmental conditions that would increase the rate of transpiration. "
            "For each condition, explain why it increases the rate. [4]\n\n"
            "(b) State what is meant by the transpiration stream. [2]"
        ),
        "marks": 6,
        "command_word": "State / Explain",
        "mark_scheme": (
            "(a) Any two conditions with explanation (1 mark condition + 1 mark explanation each):\n"
            "• Higher temperature → faster evaporation of water from leaf cells / "
            "faster diffusion of water vapour out of stomata [1+1]\n"
            "• Higher wind speed → water vapour swept away from leaf surface → "
            "steeper concentration gradient maintained [1+1]\n"
            "• Lower humidity → steeper concentration gradient between leaf air spaces "
            "and outside air → faster diffusion [1+1]\n"
            "• Higher light intensity → stomata open wider → more water vapour diffuses out [1+1]\n\n"
            "(b)\n"
            "• The movement of water through the plant from the roots to the leaves [1]\n"
            "• Through the xylem vessels [1]"
        ),
        "priority": "⭐ High — appears 6/8 Paper 1 papers",
        "hint": "Transpiration rate increases with: higher temp, higher wind speed, lower humidity, higher light. All increase the concentration gradient."
    },
    {
        "id": "TP003",
        "paper": 1,
        "topic": "Transport in Plants",
        "subtopic": "Xylem & Phloem",
        "question": (
            "(a) Give two structural features of xylem vessels that adapt them "
            "for the transport of water. [2]\n\n"
            "(b) State the substance transported in phloem and where it is transported from and to. [2]\n\n"
            "(c) Explain how guard cells control the opening and closing of stomata. [3]"
        ),
        "marks": 7,
        "command_word": "Give / State / Explain",
        "mark_scheme": (
            "(a) Any two of:\n"
            "• Dead cells (no cytoplasm or nucleus) — unobstructed flow [1]\n"
            "• No end walls / continuous tube [1]\n"
            "• Walls thickened with lignin — strong, prevents collapse [1]\n"
            "• Hollow lumen [1]\n\n"
            "(b)\n"
            "• Sucrose / sugars (and amino acids) [1]\n"
            "• From leaves (source) to all other parts of the plant including roots and storage organs (sink) [1]\n\n"
            "(c)\n"
            "• In light, guard cells absorb water by osmosis → become turgid [1]\n"
            "• Turgid guard cells bend / bow outwards → stomatal pore opens [1]\n"
            "• In darkness, guard cells lose water → become flaccid → stomata close [1]"
        ),
        "priority": "High — appears 4/8 Paper 1 papers",
        "hint": "Xylem: dead, lignified, no end walls. Phloem: transports sucrose from source to sink. Stomata: turgid = open, flaccid = closed."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 2 — HOMEOSTASIS & RESPONSE (continued)
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "HR006",
        "paper": 2,
        "topic": "Homeostasis & Response",
        "subtopic": "The Kidney & Osmoregulation",
        "question": (
            "(a) State what is meant by osmoregulation. [1]\n\n"
            "(b) Describe how the kidney produces urine. [4]\n\n"
            "(c) A patient's kidneys have failed. "
            "Compare dialysis with a kidney transplant as treatments. [4]"
        ),
        "marks": 9,
        "command_word": "State / Describe / Compare",
        "mark_scheme": (
            "(a)\n"
            "• Control of water and ion content / concentration of blood / body fluids [1]\n\n"
            "(b)\n"
            "• Blood is filtered under pressure in the glomerulus / Bowman's capsule "
            "(ultrafiltration) [1]\n"
            "• Small molecules (glucose, urea, ions, water) pass into the nephron / "
            "renal tubule [1]\n"
            "• Glucose is selectively reabsorbed back into blood [1]\n"
            "• Some water / ions are reabsorbed depending on body's needs; "
            "urea remains and is excreted as urine [1]\n\n"
            "(c) Dialysis:\n"
            "• Removes waste products / urea from blood [1]\n"
            "• Must be done regularly (e.g. 3× per week) — restricts lifestyle [1]\n"
            "Transplant:\n"
            "• Permanent solution — no need for regular dialysis sessions [1]\n"
            "• Risk of organ rejection — immunosuppressant drugs needed for life [1]\n"
            "• Shortage of donors [1]\n"
            "Award comparisons that clearly contrast both treatments."
        ),
        "priority": "High — appears 4/8 Paper 2 papers",
        "hint": "Kidney: ultrafiltration → selective reabsorption → urine. Dialysis vs transplant: convenience vs rejection risk."
    },
    {
        "id": "HR007",
        "paper": 2,
        "topic": "Homeostasis & Response",
        "subtopic": "Hormones & Diabetes",
        "question": (
            "(a) Explain how the body responds when blood glucose concentration becomes too high "
            "after a meal. Include the roles of the pancreas and liver. [4]\n\n"
            "(b) Compare Type 1 and Type 2 diabetes. Include causes and treatments. [4]"
        ),
        "marks": 8,
        "command_word": "Explain / Compare",
        "mark_scheme": (
            "(a)\n"
            "• Pancreas detects high blood glucose [1]\n"
            "• Insulin secreted by pancreas into bloodstream [1]\n"
            "• Insulin stimulates liver (and muscle) cells to convert glucose to glycogen [1]\n"
            "• Blood glucose falls back to normal [1]\n\n"
            "(b) Comparison (award 1 mark per clear comparison point):\n"
            "• Type 1: pancreas does not produce insulin; "
            "Type 2: cells become insensitive/resistant to insulin [1]\n"
            "• Type 1: tends to develop in childhood / sudden onset; "
            "Type 2: tends to develop in adults / often linked to obesity/diet [1]\n"
            "• Type 1 treatment: insulin injections / insulin pump; "
            "Type 2 treatment: lifestyle changes (diet, exercise), may need medication [1]\n"
            "• Type 1: autoimmune / genetic cause; "
            "Type 2: lifestyle / genetic factors [1]"
        ),
        "priority": "⭐ High — blood glucose control, every Paper 2",
        "hint": "High glucose → insulin released → glycogen stored in liver. Type 1 = no insulin; Type 2 = resistant to insulin."
    },
    {
        "id": "HR008",
        "paper": 2,
        "topic": "Homeostasis & Response",
        "subtopic": "Plant Hormones & Tropisms",
        "question": (
            "(a) Explain how auxin causes shoots to grow towards light (phototropism). [4]\n\n"
            "(b) Give one commercial use of plant hormones. [1]\n\n"
            "(c) Name the hormone involved in the germination of seeds. [1]"
        ),
        "marks": 6,
        "command_word": "Explain / Give / Name",
        "mark_scheme": (
            "(a)\n"
            "• Light causes auxin to accumulate on the shaded side of the shoot [1]\n"
            "• Higher auxin concentration on shaded side [1]\n"
            "• Auxin causes cells to elongate / grow longer [1]\n"
            "• Shaded side grows faster → shoot bends towards light [1]\n\n"
            "(b) Any one of:\n"
            "• Weedkillers / herbicides (selective) [1]\n"
            "• Rooting powder (to encourage root growth in cuttings) [1]\n"
            "• Ripening fruit (ethene) [1]\n"
            "• Controlling dormancy in seeds [1]\n\n"
            "(c)\n"
            "• Gibberellin [1]"
        ),
        "priority": "High — appears 4/8 Paper 2 papers",
        "hint": "Auxin: light → accumulates on dark side → elongation → bending. Commercial: herbicides, rooting powder, ethene (ripening)."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 2 — INHERITANCE, VARIATION & EVOLUTION (continued)
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "IVE005",
        "paper": 2,
        "topic": "Inheritance, Variation & Evolution",
        "subtopic": "Inherited Disorders",
        "question": (
            "Cystic fibrosis (CF) is a genetic disorder caused by a recessive allele.\n\n"
            "(a) Both parents are carriers of the CF allele but do not have the condition.\n\n"
            "Use a genetic diagram (Punnett square) to show the probability "
            "that their child will have cystic fibrosis. [3]\n\n"
            "(b) Explain why the parents do not have the condition even though they carry the allele. [2]\n\n"
            "(c) Explain what is meant by codominance. Give one example. [2]"
        ),
        "marks": 7,
        "command_word": "Use / Explain",
        "mark_scheme": (
            "(a)\n"
            "• Correct parental genotypes: Ff × Ff (or N/n if defined) [1]\n"
            "• Correct Punnett square showing FF, Ff, Ff, ff offspring [1]\n"
            "• Probability 1/4 (25%) or 1 in 4 chance of having CF (ff) [1]\n\n"
            "(b)\n"
            "• The parents are heterozygous — they have one dominant (F) and one recessive (f) allele [1]\n"
            "• The dominant allele masks the effect of the recessive allele / "
            "only one dominant allele is needed to prevent CF [1]\n\n"
            "(c)\n"
            "• Codominance: both alleles are expressed in the phenotype / "
            "neither allele is dominant over the other [1]\n"
            "• Example: ABO blood group (e.g. blood type AB — both A and B antigens expressed); "
            "or sickle cell anaemia (HbAHbS shows both traits) [1]"
        ),
        "priority": "⭐ High — Punnett squares/genetics, every Paper 2",
        "hint": "CF carriers: Ff × Ff → 25% FF : 50% Ff : 25% ff. Codominance: both alleles expressed (e.g. AB blood type)."
    },
    {
        "id": "IVE006",
        "paper": 2,
        "topic": "Inheritance, Variation & Evolution",
        "subtopic": "Sex Determination & Inherited Characteristics",
        "question": (
            "Red-green colour blindness is a sex-linked recessive condition. "
            "The allele is carried on the X chromosome.\n\n"
            "(a) A woman who is a carrier (X^N X^n) has children with a man who has normal vision (X^N Y).\n\n"
            "Use a genetic diagram to show the probability of their sons being colour blind. [3]\n\n"
            "(b) Explain why colour blindness is more common in males than in females. [2]"
        ),
        "marks": 5,
        "command_word": "Use / Explain",
        "mark_scheme": (
            "(a)\n"
            "• Correct parent genotypes shown: X^N X^n × X^N Y [1]\n"
            "• Correct offspring: X^N X^N, X^N X^n, X^N Y, X^n Y [1]\n"
            "• 1/2 or 50% of sons are colour blind (X^n Y) [1]\n\n"
            "(b)\n"
            "• Males have only one X chromosome [1]\n"
            "• One copy of the recessive allele is sufficient to cause colour blindness in males; "
            "females need two copies [1]"
        ),
        "priority": "⭐ High — sex-linked inheritance, appears 5/8 Paper 2 papers",
        "hint": "Males XY: one X allele is enough for recessive condition. Females XX: need two recessive alleles."
    },
    {
        "id": "IVE007",
        "paper": 2,
        "topic": "Inheritance, Variation & Evolution",
        "subtopic": "Evolution — Evidence",
        "question": (
            "(a) Describe three pieces of evidence that support the theory of evolution by natural selection. [3]\n\n"
            "(b) Explain why Darwin's theory of evolution was not immediately accepted by scientists "
            "when he published it in 1859. [3]"
        ),
        "marks": 6,
        "command_word": "Describe / Explain",
        "mark_scheme": (
            "(a) Any three of:\n"
            "• Fossil record — shows gradual change in organisms over time [1]\n"
            "• DNA / molecular evidence — similar DNA sequences in closely related species [1]\n"
            "• Antibiotic resistance — observed evolution in bacteria in real time [1]\n"
            "• Comparative anatomy — homologous structures in different species "
            "(e.g. pentadactyl limb) [1]\n"
            "• Biogeography — distribution of species relates to evolutionary history [1]\n\n"
            "(b)\n"
            "• Darwin could not explain how characteristics were passed on "
            "(genetics was not yet known) [1]\n"
            "• Insufficient fossil evidence available at the time [1]\n"
            "• Conflicted with religious belief that species were created by God [1]\n"
            "• The idea was so different from accepted thinking that it was controversial [1]"
        ),
        "priority": "High — appears 4/8 Paper 2 papers",
        "hint": "Evidence: fossils, DNA, antibiotic resistance, homologous structures. Not accepted: no genetics, religious conflict, radical idea."
    },
    {
        "id": "IVE008",
        "paper": 2,
        "topic": "Inheritance, Variation & Evolution",
        "subtopic": "Variation & Mutation",
        "question": (
            "(a) State the difference between continuous and discontinuous variation. "
            "Give one example of each. [4]\n\n"
            "(b) Explain how mutations can lead to new phenotypes. [3]"
        ),
        "marks": 7,
        "command_word": "State / Explain",
        "mark_scheme": (
            "(a)\n"
            "• Continuous variation: shows a range of values with no distinct categories [1]\n"
            "• Example: height, mass, shoe size, arm span [1]\n"
            "• Discontinuous variation: falls into distinct categories with no intermediate values [1]\n"
            "• Example: blood group, tongue rolling, attached/free ear lobes [1]\n\n"
            "(b)\n"
            "• A mutation is a random change in the DNA base sequence / gene [1]\n"
            "• This changes the amino acid sequence of the protein coded for [1]\n"
            "• The altered protein may function differently → change in phenotype "
            "(e.g. altered enzyme activity, different pigmentation) [1]"
        ),
        "priority": "Medium — appears 3/8 Paper 2 papers",
        "hint": "Continuous: range (height). Discontinuous: distinct groups (blood group). Mutation → changed protein → changed phenotype."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PAPER 2 — ECOLOGY (continued)
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "EC006",
        "paper": 2,
        "topic": "Ecology",
        "subtopic": "Food Webs & Energy Transfer",
        "question": (
            "The following food chain shows energy transfer in a woodland ecosystem:\n\n"
            "Oak leaves → Caterpillars → Blue tits → Sparrowhawks\n\n"
            "(a) Name the producer in this food chain. [1]\n\n"
            "(b) Only about 10% of the energy at each trophic level is passed to the next level. "
            "If the oak leaves contain 50,000 kJ of energy, calculate the energy available "
            "to the sparrowhawk. [2]\n\n"
            "(c) Explain why energy is lost between each trophic level. [3]"
        ),
        "marks": 6,
        "command_word": "Name / Calculate / Explain",
        "mark_scheme": (
            "(a)\n"
            "• Oak leaves [1]\n\n"
            "(b)\n"
            "• 50,000 × 0.1 × 0.1 × 0.1 = 50 kJ [1]\n"
            "• (Or: 50,000 → 5,000 → 500 → 50) [1]\n"
            "Award 1 mark for correct method even if arithmetic wrong.\n\n"
            "(c) Any three of:\n"
            "• Energy used in respiration by organisms at each level (heat loss) [1]\n"
            "• Energy lost in faeces / undigested material [1]\n"
            "• Energy used in movement / maintaining body temperature [1]\n"
            "• Not all of the organism is eaten / parts are not consumed [1]\n"
            "• Energy lost as urine / excretion [1]"
        ),
        "priority": "⭐ High — energy transfer, appears 6/8 Paper 2 papers",
        "hint": "10% rule: × 0.1 per level. 50,000 → 5,000 → 500 → 50 kJ. Energy lost: respiration, faeces, movement."
    },
    {
        "id": "EC007",
        "paper": 2,
        "topic": "Ecology",
        "subtopic": "Decomposers & the Water Cycle",
        "question": (
            "(a) Explain the role of decomposers in ecosystems. [3]\n\n"
            "(b) Describe how water is cycled through an ecosystem. "
            "Include the processes of evaporation, transpiration, condensation, and precipitation. [4]"
        ),
        "marks": 7,
        "command_word": "Explain / Describe",
        "mark_scheme": (
            "(a)\n"
            "• Decomposers (bacteria and fungi) break down dead organic material / "
            "waste products [1]\n"
            "• By secreting enzymes onto the material (extracellular digestion) [1]\n"
            "• They return mineral ions / nutrients to the soil for plants to absorb [1]\n\n"
            "(b)\n"
            "• Water evaporates from oceans / rivers / lakes → water vapour in atmosphere [1]\n"
            "• Transpiration from plant leaves adds water vapour to atmosphere [1]\n"
            "• Water vapour rises and cools → condensation forms clouds [1]\n"
            "• Precipitation (rain/snow) returns water to land / oceans [1]"
        ),
        "priority": "Medium — appears 3/8 Paper 2 papers",
        "hint": "Decomposers: break down dead matter → return nutrients. Water cycle: evaporation → transpiration → condensation → precipitation."
    },
    {
        "id": "EC008",
        "paper": 2,
        "topic": "Ecology",
        "subtopic": "Biodiversity & Conservation",
        "question": (
            "(a) Define the term biodiversity. [2]\n\n"
            "(b) Give three reasons why it is important to maintain high biodiversity. [3]\n\n"
            "(c) Describe one method that can be used to maintain biodiversity. [2]"
        ),
        "marks": 7,
        "command_word": "Define / Give / Describe",
        "mark_scheme": (
            "(a)\n"
            "• The variety of living organisms [1]\n"
            "• Within an ecosystem / species / at the genetic level [1]\n\n"
            "(b) Any three of:\n"
            "• Ecosystems with high biodiversity are more stable / resilient to change [1]\n"
            "• Many species have potential for medical / scientific value (e.g. drugs from plants) [1]\n"
            "• Loss of one species can have knock-on effects on food webs [1]\n"
            "• Organisms provide ecosystem services (pollination, nutrient cycling, water purification) [1]\n"
            "• Moral / ethical responsibility to protect other species [1]\n\n"
            "(c) Any one of:\n"
            "• Breeding programmes in zoos / captive breeding [1+1: what + how it helps]\n"
            "• Seed banks — preserving genetic diversity of plant species [1+1]\n"
            "• Nature reserves / protecting habitats from development [1+1]\n"
            "• International agreements / laws to limit hunting or habitat destruction [1+1]\n"
            "Award 1 mark for naming a method, 1 mark for explaining how it maintains biodiversity."
        ),
        "priority": "High — appears 4/8 Paper 2 papers",
        "hint": "Biodiversity: variety of species/genes. Conservation: breeding programmes, seed banks, reserves, legal protection."
    },
    {
        "id": "EC009",
        "paper": 2,
        "topic": "Ecology",
        "subtopic": "Pollution & Human Impact",
        "question": (
            "Human activities cause pollution of air, land, and water.\n\n"
            "(a) Name one pollutant that causes acid rain and explain how it damages ecosystems. [2]\n\n"
            "(b) Explain how eutrophication occurs and what effect it has on aquatic life. [4]"
        ),
        "marks": 6,
        "command_word": "Name / Explain",
        "mark_scheme": (
            "(a)\n"
            "• Sulfur dioxide (SO₂) / nitrogen oxides (NOₓ) [1]\n"
            "• Dissolves in rainwater → acid rain → damages leaves/bark of trees / "
            "acidifies lakes → kills aquatic organisms / leaches minerals from soil [1]\n\n"
            "(b)\n"
            "• Fertilisers / nitrates wash off fields into rivers / lakes (leaching / run-off) [1]\n"
            "• Algae use the extra nitrates → rapid algal bloom on water surface [1]\n"
            "• Algae block light → aquatic plants below cannot photosynthesise → die [1]\n"
            "• Decomposers (bacteria) break down dead plants → use up oxygen in water [1]\n"
            "• Fish and other aquatic organisms die due to lack of oxygen [1]\n"
            "Award 4 marks from the 5 available (or 4 clearly stated and linked points)."
        ),
        "priority": "High — eutrophication, appears 4/8 Paper 2 papers",
        "hint": "Eutrophication: fertiliser → algal bloom → blocks light → plants die → decomposers use O₂ → aquatic life dies."
    },

    # ─────────────────────────────────────────────────────────────────────────
    # CROSS-TOPIC: REQUIRED PRACTICALS & MATHS SKILLS
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "RP001",
        "paper": 1,
        "topic": "Required Practicals",
        "subtopic": "Food Tests",
        "question": (
            "A student tested an unknown food sample for the presence of glucose, starch, "
            "and protein.\n\n"
            "(a) For each food test below, state the reagent used and the positive result:\n\n"
            "   (i) Test for glucose [2]\n"
            "   (ii) Test for starch [2]\n"
            "   (iii) Test for protein (Biuret test) [2]\n\n"
            "(b) The student found that the food contained starch but not glucose. "
            "Suggest what this tells you about the digestive state of the food. [1]"
        ),
        "marks": 7,
        "command_word": "State / Suggest",
        "mark_scheme": (
            "(i) Glucose:\n"
            "• Reagent: Benedict's solution [1]\n"
            "• Positive result: blue → brick red / orange-red precipitate (on heating) [1]\n\n"
            "(ii) Starch:\n"
            "• Reagent: Iodine solution [1]\n"
            "• Positive result: yellow-brown → blue-black [1]\n\n"
            "(iii) Protein (Biuret):\n"
            "• Reagents: sodium hydroxide + copper sulfate (Biuret reagent) [1]\n"
            "• Positive result: blue → purple / lilac [1]\n\n"
            "(b)\n"
            "• The starch has not yet been digested / amylase has not broken starch down into glucose [1]"
        ),
        "priority": "⭐ High — required practical, appears every Paper 1",
        "hint": "Benedict's: blue→red (glucose). Iodine: brown→blue-black (starch). Biuret: blue→purple (protein)."
    },
    {
        "id": "RP002",
        "paper": 2,
        "topic": "Required Practicals",
        "subtopic": "Population Sampling — Quadrats",
        "question": (
            "A student used quadrats to estimate the population of daisies in a field.\n\n"
            "(a) Describe how the student should use quadrats to obtain a valid estimate "
            "of the daisy population. [4]\n\n"
            "(b) The field has an area of 2,000 m². "
            "In 10 quadrats of 0.5 m² each, the student counted a mean of 6 daisies per quadrat. "
            "Calculate the estimated total number of daisies in the field. [2]"
        ),
        "marks": 6,
        "command_word": "Describe / Calculate",
        "mark_scheme": (
            "(a)\n"
            "• Use random sampling — place quadrats using random coordinates "
            "(e.g. random number generator) to avoid bias [1]\n"
            "• Place a sufficient number of quadrats across the field [1]\n"
            "• Count all daisies rooted inside (or intersecting two sides of) the quadrat [1]\n"
            "• Calculate the mean number of daisies per quadrat [1]\n\n"
            "(b)\n"
            "• Number of quadrats that fit in field = 2,000 ÷ 0.5 = 4,000 [1]\n"
            "• Total population = 4,000 × 6 = 24,000 daisies [1]\n"
            "Award 1 mark for correct method even if arithmetic wrong."
        ),
        "priority": "⭐ High — required practical, every Paper 2",
        "hint": "Random sampling avoids bias. Population = (field area ÷ quadrat area) × mean count."
    },
    {
        "id": "RP003",
        "paper": 2,
        "topic": "Required Practicals",
        "subtopic": "Reaction Time Investigation",
        "question": (
            "A student investigated the effect of caffeine on reaction time using a ruler drop test.\n\n"
            "(a) Describe how the ruler drop test measures reaction time. [2]\n\n"
            "(b) The student's results before caffeine: reaction times (ms) were "
            "250, 230, 260, 240, 250.\n\n"
            "   (i) Calculate the mean reaction time. [1]\n"
            "   (ii) Identify the anomalous result in the data. [1]\n\n"
            "(c) Suggest why the student repeated the test five times rather than once. [1]"
        ),
        "marks": 5,
        "command_word": "Describe / Calculate / Identify / Suggest",
        "mark_scheme": (
            "(a)\n"
            "• The ruler is dropped and the participant catches it as fast as possible [1]\n"
            "• The distance it falls before being caught is measured and converted to time "
            "(or the distance is used as a proxy for reaction time) [1]\n\n"
            "(b)(i)\n"
            "• Mean = (250 + 230 + 260 + 240 + 250) ÷ 5 = 246 ms [1]\n\n"
            "(b)(ii)\n"
            "• 260 ms (highest value, furthest from other readings) [1]\n\n"
            "(c)\n"
            "• To calculate a mean / reduce the effect of anomalous results / "
            "improve reliability of data [1]"
        ),
        "priority": "High — required practical, appears 4/8 Paper 2 papers",
        "hint": "More repeats = more reliable mean. Anomalous = value far from others. Mean = sum ÷ count."
    },
    {
        "id": "MS001",
        "paper": 1,
        "topic": "Maths Skills",
        "subtopic": "Graph Interpretation & Rate Calculation",
        "question": (
            "The graph below shows the volume of oxygen produced by a plant over 10 minutes "
            "at two different light intensities (assume data: at high light intensity, "
            "50 cm³ O₂ produced in 10 min; at low intensity, 20 cm³ in 10 min).\n\n"
            "(a) Calculate the rate of oxygen production at high light intensity. "
            "Give the unit. [2]\n\n"
            "(b) The graph shows that the rate at high intensity slows after 8 minutes. "
            "Suggest why. [1]\n\n"
            "(c) Describe the relationship between light intensity and rate of photosynthesis "
            "shown by the graph. [2]"
        ),
        "marks": 5,
        "command_word": "Calculate / Suggest / Describe",
        "mark_scheme": (
            "(a)\n"
            "• Rate = 50 ÷ 10 = 5 cm³/min [1]\n"
            "• Correct unit: cm³ per minute (cm³ min⁻¹) [1]\n\n"
            "(b)\n"
            "• Another factor (CO₂ or temperature) has become limiting [1]\n"
            "OR carbon dioxide / water has been used up [1]\n\n"
            "(c)\n"
            "• As light intensity increases, rate of photosynthesis increases [1]\n"
            "• The relationship is linear / proportional (up to the plateau) [1]\n"
            "Do NOT accept 'directly proportional' unless the graph passes through the origin."
        ),
        "priority": "⭐ High — graph + rate, every paper",
        "hint": "Rate = quantity ÷ time. Describe trends: use 'as X increases, Y increases'. Plateau = limiting factor."
    },

]

# ─── Helper functions ─────────────────────────────────────────────────────────

def get_all_questions():
    return QUESTIONS

def get_questions_by_paper(paper_num):
    return [q for q in QUESTIONS if q["paper"] == paper_num]

def get_questions_by_topic(topic):
    return [q for q in QUESTIONS if q["topic"].lower() == topic.lower()]

def get_question_by_id(qid):
    for q in QUESTIONS:
        if q["id"] == qid:
            return q
    return None

TOPICS_PAPER1 = sorted(set(q["topic"] for q in QUESTIONS if q["paper"] == 1))
TOPICS_PAPER2 = sorted(set(q["topic"] for q in QUESTIONS if q["paper"] == 2))
