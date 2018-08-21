import numpy as np
from collections import Counter, defaultdict
import random

PLAYERS = ["A", "B", "C"]

class Player:
	def __init__(self, name, ind):
		self.name = name
		self.index = ind
		self.wins = 0
		self.matchesPerOpp = defaultdict(int)
		self.winsPerOpp = defaultdict(int)
	
	def perOpponent(self, opps, tournament):
	
		for opp in opps:
			matchesWithOpp = tournament.getMatchesBetween(self, opp)
			matchWins = tournament.getMatchesWithWinAgainst(self, opp)
			self.matchesPerOpp[opp] += len(matchesWithOpp)
			self.winsPerOpp[opp] += len(matchWins)

	def assignProb(self, prob):
		self.probability = int(prob)

	def __str__(self):
		return self.name
		
class Match:
	def __init__(self, p0, p1, zero_or_1):
		self.players = {p0, p1}
		if zero_or_1 == 0:
			self.winner = p0
			self.loser = p1
		else:
			self.winner = p1
			self.loser = p0

	def __str__(self):
		return "{}_beats_{}".format(self.winner, self.loser)
			
class Tournament:
	def __init__(self, players, matches):
		self.matches = matches
		self.players= players
	
	def getMatchesBetween(self, p0, p1):
		return [m for m in self.matches if p0 in m.players and p1 in m.players]
	
	def getMatchesWithWin(self, winner):
		return [m for m in self.matches if winner in m.players and winner == m.winner]
		
	def getMatchesWithWinAgainst(self, winner, opp):
		return [m for m in self.matches if winner in m.players and opp in m.players and winner == m.winner]

	def getNumMatchesTotal(self):
		return len(self.matches)
	
		
def assembleMatches(players, num_matches):
	
	matches = []
	for i in range(num_matches):
		splayers = set(players)
		# pick 2 players at random
		p0 = random.choice(list(splayers))
		splayers.remove(p0)
		p1 = random.choice(list(splayers))
		m = Match(p0, p1, random.choice([0,1]))
		matches.append(m)
	return matches
		

def compute_rank_scores(tournament, max_iters=1000, error_tol=1e-3):
	''' Computes Bradley-Terry using iterative algorithm
		See: https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model
	'''
	# Do some aggregations for convenience
	# Total wins per player
	players= tournament.players
	
	#ranks = pd.Series(np.ones(len(players)) / len(players), index=players)
	ranks = np.ones(len(players)) / len(players)
	for iters in range(max_iters):
		oldranks = ranks.copy()
		for player in players:
			denom = np.sum( player.matchesPerOpp[p] / (ranks[p.index] + ranks[player.index]) for p in players if p != player)
			ranks[player.index] = 1.0 * player.wins / denom

		ranks /= sum(ranks)

		if np.sum(np.abs(ranks - oldranks)) < error_tol:
			break

	if np.sum(np.abs(ranks - oldranks)) < error_tol:
		print(" * Converged after %d iterations.", iters)
	else:
		print(" * Max iterations reached (%d iters).", max_iters)


	# Scale logarithm of score to be between 1 and 1000
	for i, r in enumerate(ranks):
		players[i].assignProb(np.log1p(1000 * r) / np.log1p(1000) * 1000)
		#players[i].assignProb(r)



if __name__ == "__main__":
	# assemble matches
	players=  []
	for i, p in enumerate(PLAYERS):
		players.append(Player(p, i))
	
	
	matches = assembleMatches(players, 1000)
	
	T = Tournament(players, matches)
	
	for p in T.players:
		p.wins=	 len(T.getMatchesWithWin(p))
		others= [pprime for pprime in T.players if pprime != p]
		p.perOpponent(others, T)

		
	compute_rank_scores(T)
	
	#print(players)
	with open('ranks.txt', 'w') as filename:
		for p in T.players:
			filename.write(p.name)
			filename.write("\t")
			filename.write(str(p.probability))
			filename.write("\n")
	
	