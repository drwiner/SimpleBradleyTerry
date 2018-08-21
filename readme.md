## Simple Bradley Terry Model

##### Adapted from https://github.com/bjlkeng/Bradley-Terry-Model

Input is binary pairwise choice of form i < j.


Output is list of elements of form <player, "BT" score between 1 and 1000)>. Let S denote the list of BT scores of players p0,...,pk. The probability that comparison pi > pj is S(pi) / S(pi) + S(pj).   

- CalculatePairwiseSeries.py -- creates permutations of 15 pairwise comparisons for 100 participants, counterbalanced on left/right and for beginning, middle, and end

- eval_batch.py -- evaluates the distribution of permutations created from CalculatePairwiseSeries.py

- create_test_data.py -- creates test data and runs bradley terry model

- random_pairwise_series.py -- runs simulation on pairwise series with random comparison outcomes