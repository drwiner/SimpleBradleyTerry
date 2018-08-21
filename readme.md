## Simple Bradley Terry Model

##### Adapted from https://github.com/bjlkeng/Bradley-Terry-Model

Input is binary pairwise choice of form i < j.


Output is list of elements of form <player, "BT" score between 1 and 1000)>. Let S denote the list of BT scores of players p0,...,pk. The probability that comparison pi > pj is S(pi) / S(pi) + S(pj).   