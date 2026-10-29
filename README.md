# Open-Test-Data

Research on **skill, knowledge and cognitive-performance tests with human response data available online**. Personality, attitudes, interests and self-reported ability are excluded from the skill-test shortlist.

**Research date: 29 October 2026.** The catalogue has **37 entries** across four domains. These are dataset versions and source families, not 37 independent experiments or 37 unrestricted open licenses. Conditional-access sources and practice logs are explicitly identified.

## Read the research

| Coverage | Profiles | Detailed findings |
|---|---:|---|
| Cognitive ability and performance | 11 | [Reasoning, vocabulary, knowledge, spatial rotation, memory, attention and inhibition](research/cognitive-ability.md) |
| Large educational and adult assessments | 9 | [PISA, PIAAC, TIMSS, PIRLS, ICILS and civic knowledge](research/large-scale-assessments.md) |
| Subject tests and learning datasets | 10 | [Fraction subtraction, ECPE, ASSISTments, Junyi, EdNet, Eedi, Duolingo, KDD and database exercises](research/subject-tests-and-learning.md) |
| Language assessment and short answers | 7 | [MERLIN, Cambridge writing/speaking, C-Tests, BEETLE and SciEntsBank](research/language-and-short-answers.md) |

Download/filter the full catalogue: **[JSON](data/catalogue.json)** · **[CSV](data/catalogue.csv)**. See the [field definitions](data/README.md), [verification evidence](data/verification-evidence.json), [research method and analysis guidance](research/methodology.md), and [discovery resources/exclusions](research/discovery-and-exclusions.md).

## Where to start

These are practical research priorities, not rankings of test quality. Choose the response information needed by the proposed scoring method.

| Research need | Useful starting sources | Why they fit | Main qualification |
|---|---|---|---|
| Compact scoring-method prototype | SAPA `ability` / `iqitems` | 1,525 people × 16 items; binary and original option representations | Same sample in both objects; stimulus rights separate |
| Binary and diagnostic item models | Fraction subtraction; ECPE grammar | Verified dense matrices: 536 × 20 and 2,922 × 28; Q-matrices | Already scored; original distractor choices absent |
| Omission, guessing and partial-credit rules | OpenPsychometrics VIQT, MGKT, FSIQ alpha | Selected answers and documented historical scoring | Volunteer samples, version differences; redistribution rights unresolved |
| Distractor-sensitive educational scoring | Eedi NeurIPS 2020 | Actual choices, keys and correctness | Sparse selected data; release terms and image restrictions apply |
| Spatial accuracy and speed | Ganis–Kievit mental rotation | Actual/desired responses and timing; deposited data and stimuli CC BY 4.0 | Small task-specific validation sample |
| Stability of cognitive-task scoring | Self-Regulation Ontology performance subset | Trial data and retesting | Exclude surveys and preference tasks; inspect task reliability |
| Population and cross-country analysis | PISA 2022; TIMSS 2023; PIAAC 2023 | Large objective response sources with technical documentation | Adaptive/booklet exposure, sample design and provider terms |
| Digital skill performance | ICILS 2023 | Observed computer/information tasks and optional computational thinking | Shared-task rubric criteria and incomplete item-content release |
| Speed and revisits in large assessments | PISA 2018 corrected total-time supplement | Explicitly documented timing correction | Original last-visit time differs from total time |
| Human-rated written performance | MERLIN | Multilingual examination texts, CEFR ratings and CC BY-SA 4.0 resources | Task/language/rater effects; download endpoint needs rechecking |
| Short-answer grading | BEETLE; SciEntsBank | Original human answers, reference answers and nominal error judgments | Preserve official splits and select one archive view |
| Learning-aware scoring | ASSISTments 2009; EdNet; Junyi | Repeated performance, feedback and process fields | Define current knowledge versus initial ability; avoid future-data leakage |

PISA 2025 is also verified as released, including actual cognitive/process archive headers and codebook checks. It is a valuable new-cycle candidate; final technical documentation was still pending at this review's cutoff. See the [large-assessment findings](research/large-scale-assessments.md).

## Findings that change how these data can be used

- **A public download is not automatically an open redistribution license.** PISA/PIAAC have specific public-use terms; Cambridge research corpora prohibit redistribution. Eedi question images have additional use restrictions. External terms remain attached to external material.
- **Wrong-answer choices cannot be reconstructed from binary scores.** Fraction subtraction and ECPE support correctness-level models; option-based rules need sources retaining actual choices.
- **Practice records are not independent test attempts.** Feedback, repeated items, mastery stopping and adaptive recommendations affect observed performance.
- **Identifiers and versions matter.** ASSISTments 2015 has sequence IDs rather than actual question IDs. MGKT's historical data scoring differs from the current test webpage. Eedi task pairs cannot be linked by numeric IDs across releases.
- **Timing needs a definition.** Last-visit time, total time, screen/bundle time, exercise duration and item latency are different measurements.
- **Estimated ability is not ground truth.** Plausible values, diagnostic classes, CEFR judgments and Q-matrices have specific meanings; none provides an error-free personal skill label.

## What is saved here

Original research summaries, source links, structured metadata, verification notes and selected archive checksums. **No participant response files, restricted corpora, test photographs or protected question banks are included.** Some publicly accessible files were inspected temporarily to verify structure; many large datasets were checked through documentation, archive byte ranges or samples. Evidence levels and unresolved details are recorded explicitly.

The existing [repository license](LICENSE) applies to this project's original contributions. It does not grant rights to external datasets, test questions, keys, rubrics, images or recordings. Recheck the linked version-specific terms before obtaining or publishing external material.
