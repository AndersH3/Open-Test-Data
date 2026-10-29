# Changelog for "Data for the 2018 Duolingo Shared Task on Second Language Acquisition Modeling (SLAM)"


## February 13, 2019
4.0: Adds translation prompts for all tracks/files, and fixes UD parsing errors

For `reverse_translate` and `reverse_tap` challenge types, we now include the prompt that the student saw as meta-data

```
# prompt:I cook fish.
# user:+H9QWAV4  countries:CA  days:0.026  client:ios  session:lesson  format:reverse_translate  time:11
fPMzRNKJ0201  Yo        PRON    Case=Nom|Number=Sing|Person=1|PronType=Prs|fPOS=PRON++               nsubj        2  0
fPMzRNKJ0202  cocino    VERB    Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin|fPOS=VERB++    ROOT         0  0
fPMzRNKJ0203  el        DET     Definite=Def|Gender=Masc|Number=Sing|PronType=Art|fPOS=DET++         det          4  1
fPMzRNKJ0204  pescado   NOUN    Gender=Masc|Number=Sing|fPOS=NOUN++                                  dobj         2  0

# prompt:It is soup.
# user:+H9QWAV4  countries:CA  days:0.028  client:ios  session:lesson  format:reverse_tap  time:11
Zz6tSKoQ0201  Es        VERB    Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|fPOS=VERB++    cop          2  0
Zz6tSKoQ0202  sopa      NOUN    Gender=Fem|Number=Sing|fPOS=NOUN++                                   ROOT         0  0
```

We also discovered in data preparation that bug removed punctuation from tokens, but not the UD parsing output. This
lead to alignment errors that affected 7% of tokens. However, we re-ran the track baseline (logistic regression) and
there were no significant changes in AUROC or F1 (new/old test set results for each track reported below):

* en_es   AUROC: 0.774/0.774   F1: 0.191/0.190
* es_en   AUROC: 0.745/0.746   F1: 0.176/0.175
* fr_en   AUROC: 0.771/0.771   F1: 0.285/0.281


## April 24, 2018
3.0: Adds TEST set keys (answers) and citation details.


## March 9, 2018
2.0: Adds blind TEST set data


## January 10, 2018
1.0: Initial TRAIN and DEV sets for SLAM Shared Task