# Self-Regulation Ontology: objective performance-task subset

Redistribution decision: **permitted under CC BY 4.0**. The source repository README explicitly grants sharing/adaptation of its data. The original license statement is preserved as a labeled excerpt in `codebooks/LICENSE-statement-source.txt`; full license text is supplied separately. This dataset's rights remain separate from the parent repository's AGPL license.

Source repository: https://github.com/IanEisenberg/Self_Regulation_Ontology
Pinned source commit: `4e6e837fb5aaca87ed5914fd9be251156f43eec9`
License statement: https://github.com/IanEisenberg/Self_Regulation_Ontology/blob/4e6e837fb5aaca87ed5914fd9be251156f43eec9/README.md#license
Primary article and attribution: Eisenberg et al. (2019), Uncovering the structure of self-regulation through data-driven ontology discovery. Nature Communications 10, 2319. https://doi.org/10.1038/s41467-019-10301-1
Retest article: Enkavi et al. (2019), Large-scale analysis of test-retest reliabilities of self-regulation measures. https://doi.org/10.1073/pnas.1818430116
Retrieved: 2026-10-29.

## Scope and changes

The source mixes performance tasks, personality/health surveys, preferences and decision tasks. This mirror includes **23 objectively scored performance tasks** from both `Complete_02-16-2019` and `Retest_02-16-2019`, preserving each original `.csv.gz` byte-for-byte inside two clearly labeled subset ZIPs. It omits personality/health surveys, preference/risk/discounting tasks and ancillary demographic tables. Raven and cognitive-reflection content are also omitted here to keep the stimulus-rights boundary narrow. This is an explicitly selected performance subset, not the entire study deposit. Packaging and selection are the only changes.

Included tasks: adaptive_n_back, attention_network_task, choice_reaction_time, digit_span, directed_forgetting, dot_pattern_expectancy, go_nogo, hierarchical_rule, keep_track, local_global_letter, motor_selective_stop_signal, psychological_refractory_period_two_choices, recent_probes, shape_matching, shift_task, simon, simple_reaction_time, spatial_span, stim_selective_stop_signal, stop_signal, stroop, threebytwo, tower_of_london.

The complete source study reports 522 participants and 150 retest participants; usable N varies by task, QC and cleaning. Those totals have not been re-established for these packaged raw files. The original data READMEs explain raw versus processed data. `codebooks/observed-column-schemas.json` is a **project-generated field inventory**, not an original author codebook. Trial columns vary across tasks. Use the author's task-specific analysis code and experimental documentation for scoring rather than assigning common semantics to every column. No survey items or stimuli/images were separately copied.
