from create_test_data import Tournament, Match, Player, compute_rank_scores
from calculatePairwiseSeries import NUM_ITEMS
import random
import numpy as np

# can fill this in manually if changes from calculatePairwiseSeries.py
#NUM_ITEMS = 6

if __name__ == "__main__":
	data = []
	with open("generated_output.txt", 'r') as filename:
		for line in filename:
			data.append(eval(line))
	
	players=  [Player(str(i), i) for i in range(NUM_ITEMS)]

	matches= []
	for p in data:
		for item in p:
			# pick 0 or 1
			index = random.choice([0,1])
			winner = item[index]
			# flip bit with ^
			loser = item[index ^ 1]
			m = Match(players[winner], players[loser], index)
			matches.append(m)
			
	t = Tournament(players, matches)
	
	for p in t.players:
		p.wins=	 len(t.getMatchesWithWin(p))
		others= [pprime for pprime in t.players if pprime != p]
		p.perOpponent(others, t)
		
	compute_rank_scores(t)
	
	#print(players)
	with open('testing_video_ranks.txt', 'w') as filename:
		for p in t.players:
			filename.write(p.name)
			filename.write("\t")
			filename.write(str(p.probability))
			filename.write("\n")