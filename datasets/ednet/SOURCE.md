# EdNet KT1-KT4 and Contents

Provider: Riiid / Santa. Source checked and files retrieved on 2026-10-29.

- Author repository, licence declaration and original field descriptions: https://github.com/riiid/ednet
- Author repository README: https://raw.githubusercontent.com/riiid/ednet/master/README.md
- Original archive links: [KT1](https://bit.ly/ednet_kt1), [KT2](https://bit.ly/ednet-kt2), [KT3](https://bit.ly/ednet-kt3), [KT4](https://bit.ly/ednet-kt4), [Contents](https://bit.ly/ednet-content)
- Paper: https://arxiv.org/abs/1912.03072

## Rights

The authors explicitly release the dataset under **CC BY-NC 4.0** for research. The full legal text is in LICENSE.txt, obtained from the SPDX licence corpus: https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-NC-4.0.txt . Canonical licence: https://creativecommons.org/licenses/by-nc/4.0/ . Attribution and noncommercial conditions remain attached to these files. The project's software licence does not replace them.

## Contents and changes

The full KT1, KT2, KT3, KT4 and Contents ZIP files are acquired without modifying their bytes. KT1 acquisition combines validated official-source prefix/ranges with an immutable matching mirror for remaining ranges: https://huggingface.co/datasets/Lucy9999/EdNet-KT1/resolve/790cff06b7c112c4ec072217257de5dd4ec1e77a/EdNet-KT1.zip . Fixed byte windows and size match the official file; the final archive must match the mirror LFS SHA-256 recorded in mirror-verification.json. The mirror card's MIT label does not replace Riiid's canonical CC BY-NC4 dataset licence. The release inventory records exact sizes and SHA-256 hashes. Each learner's events are stored in a separate CSV inside the source ZIP. KT1 covers question-solving responses; KT2 adds answer selection/submission events; KT3 adds explanations/lectures; KT4 adds broader activity. These are overlapping representations, not four independent samples. No unreleased question text, pictures, audio or TOEIC score file is implied.

UPSTREAM_README.md is the author's original repository README/codebook, preserved unchanged. CODEBOOK.md is a concise project field guide. Large originals are distributed as release assets to keep the Git repository usable.

## Citation

Choi, Y. et al. (2020). EdNet: A Large-Scale Hierarchical Dataset in Education. In Artificial Intelligence in Education. Also available as arXiv:1912.03072. Credit Riiid and the named authors of the linked paper.

## Limitations

Timestamps were shifted for privacy. Questions share bundles and can share elapsed times. Practice, feedback, recommendations and answer revisions affect responses. Higher-level actions must not be counted as all being scored answers. See the author README for exact action/source semantics.
