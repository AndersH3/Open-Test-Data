# Executive findings

## What this research establishes

There is a substantial supply of human skill-response data online, but no single source supplies every response format, construct and reuse permission. The 37 catalogue entries cover reasoning, vocabulary, general knowledge, spatial ability, memory, attention, mathematics, science, adult literacy and numeracy, digital competence, language production and short-answer explanation. Personality, beliefs, preferences and self-reported ability are excluded from the skill-response scope.

The most important practical choice is the observation needed by the proposed scoring rule. Binary correctness supports one class of models; selected distractors, partial work, timing, repeated attempts and human rubric judgments support others. These are not interchangeable. A public sample test or aggregate item statistic does not supply the joint response patterns required to compare individual scores.

This report combines the full source review with a separate redistribution audit and downloaded collection. Every source has a decision, including sources not mirrored because their terms are restrictive, permission remains unresolved or an official download could not be obtained. Source-specific licences, original codebooks where available, project field guides and checksum manifests accompany the mirrored collection. The project licence does not override third-party conditions.

## Most useful starting points

| Research question | Practical sources | Interpretation |
|---|---|---|
| Can a scoring pipeline reproduce a familiar small item matrix? | SAPA ability/iqitems, fraction subtraction, ECPE grammar | Useful compact structural benchmarks. SAPA's two objects are the same sample; binary-only exports cannot recover distractor choices. Exact packaged response objects are mirrored under their formal GPL grants; separate test-stimulus rights remain distinct. |
| Does a score capture spatial performance and latency? | Ganis-Kievit mental rotation | Direct behaviour, stimulus conditions and response-time documentation; a small, task-specific validation sample. [Original deposit](https://doi.org/10.6084/m9.figshare.1045385). |
| Does a task score remain stable on retesting? | Self-Regulation Ontology objective task subset | Raw trials and retest data permit task-specific stability checks. Exclude surveys and preference tasks. [Author data and licence](https://github.com/IanEisenberg/Self_Regulation_Ontology). |
| How should span performance receive partial credit? | Mathy-Friedman working-memory data | Original trial and participant-level files document different span-scoring rules. Preserve repeated-trial structure. [Versioned deposit](https://data.mendeley.com/datasets/kfc3jyggs7/1). |
| What do distractor choices add to educational scoring? | Eedi NeurIPS 2020; EdNet | Actual answers and keys support option-based analysis. Eedi retains only the latest student-question answer and uses separate ID spaces across task pairs; its images have additional restrictions. EdNet is longitudinal test preparation. [Eedi source](https://www.eedischool.com/projects/neurips-education-challenge), [EdNet source](https://github.com/riiid/ednet). |
| How does a score behave during learning? | Junyi 2020, EdNet, ASSISTments 2009 | Define initial knowledge, current knowledge or learning gain before evaluation. Hints, feedback, stopping rules and future attempts must not leak into predictions. [Junyi release](https://www.kaggle.com/datasets/junyiacademy/learning-activity-public-dataset-by-junyi-academy). |
| Can a score generalize across populations or countries? | PISA, PIAAC, TIMSS, PIRLS, ICILS | Large samples are useful, but exposure design, weights and latent-score estimation require their technical manuals. These sources are linked rather than mirrored where sharing permission is absent. |
| How should written performance be evaluated? | MERLIN; Cambridge FCE and Write & Improve | Use ordinal/human-rating methods and account for task and rater effects. MERLIN is redistributable; Cambridge release terms prohibit corpus sharing. [MERLIN source](https://www.merlin-platform.eu/), [Cambridge terms](https://researchdatasets.cambridge.org/datasets/clc-fce-dataset). |
| Can a short-answer score distinguish error types? | BEETLE and SciEntsBank | Nominal accuracy judgments and reference answers support grading studies. They do not form an equally spaced five-level scale. [Organizer release](https://github.com/myrosia/semeval-2013-task7). |

## Six findings that materially affect analysis

1. **Response codes carry scientific meaning.** Omitted, not-reached, not-administered and incorrect are different states. Preserve the original representation and document every transformation.
2. **Units must remain explicit.** A student, test submission, token, step, attempt, action, passage and question are different units. Dataset-size claims should state which one is counted.
3. **Timing is a measurement definition.** Last-visit time, total time, bundle/screen time, exercise duration and event timestamps require different analyses. PISA 2018's corrected supplement is a particularly clear example.
4. **A sample is not a norm.** Volunteer online samples, scanner-based cohorts, narrow historical tests and selected practice users do not automatically represent a deployment population.
5. **Observed performance is not error-free ability.** Plausible values, estimated diagnostic classes, expert Q-matrices and CEFR judgments are useful annotations or model outputs, not known personal ground truth.
6. **Reuse permission must be checked at the file and component level.** Data, code, stimuli, photographs, question images, rubrics and papers can carry different conditions. Non-commercial and ShareAlike licences permit some redistribution while retaining those obligations; an unresolved licence is not an open grant.

## Recommended progression for scoring research

First validate the scoring pipeline on a small documented response source. Then use an independently acquired dataset with the required response information and a held-out evaluation design. Estimate all weights and transformations on training observations. Compare uncertainty, calibration, ranking stability and prediction of held-out performance, rather than only correlation with a score derived from the same answers.

For practice data, use time-respecting splits and keep a learner's related records together where appropriate. For transfer to new content, hold out whole items, passages or tasks. For population claims, preserve survey design and imputation rules. A novel score that gives rare responses extra weight requires particular care about guessing, small cells, local dependence and outliers.

These recommendations are a methodological synthesis of the reviewed sources. No scoring algorithm was fitted, no causal claim was tested, and no source has been certified for high-stakes individual decisions in this task. Detailed evidence and limitations follow in the source profiles and acquisition ledger.
