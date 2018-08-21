from math import factorial
import random

F2 = factorial(2)
NUM_ITEMS = 6

def n_choose_2(n):
	return factorial(n) / (F2*factorial(n-2))
	
def generateAll():
	unique_comparisons=  [(i,j) for i in range(NUM_ITEMS) for j in range(NUM_ITEMS) if i != j]
	print(unique_comparisons)
	# beginning = list(unique_comparisons)
	# middle = list(unique_comparisons)
	# ending = list(unique_comparisons)
	
	num_comparisons_per_participant = n_choose_2(NUM_ITEMS)
	num_groups = 0
	if (num_comparisons_per_participant % 3 != 0):
		if (num_comparisons_per_participant % 4 != 0):
			raise Exception("not divisible by 3 or 4")
		else:
			num_groups = 4
	else:
		num_groups = 3
		
	print("Num_groups:", num_groups)
		
	groups = [list(unique_comparisons) + list(unique_comparisons) + list(unique_comparisons) + list(unique_comparisons) for i in range(num_groups)]
	per_group = int(num_comparisons_per_participant/num_groups)
	
	# IDEA: for each participant, pick 5 from beginning, 5 from middle, and 5 from ending for a total of 15
	# each choice must be unique
	participant_series = []
	while(len(participant_series) < 90):
		groups = [list(unique_comparisons) + list(unique_comparisons) + list(unique_comparisons) + list(unique_comparisons) for i in range(num_groups)]
		
		for i in range(90):
			p = []
			flag_on_play = False
			for j in range(num_groups):
				
				have_not_yet_seen = list(groups[j])
				flag_on_play = False
				for pg in range(per_group):
					if len(have_not_yet_seen) == 0:
						flag_on_play = True
						break
					item = random.choice(have_not_yet_seen)
					item_reversed = (item[1], item[0])
					while item in p or item_reversed in p:
						item = random.choice(have_not_yet_seen)
						have_not_yet_seen.remove(item)
						item_reversed = (item[1], item[0])
						if len(have_not_yet_seen) == 0:
							flag_on_play = True
							break
					if flag_on_play:
						break
					groups[j].remove(item)
					p.append(item)
				if flag_on_play:
					break
			if flag_on_play:
				continue
			if tuple(p) in participant_series:
				continue
			participant_series.append(tuple(p))
			print(p)
		print(len(participant_series))
		
	with open("generated_output.txt", 'w') as filename:
		for p in participant_series:
			filename.write(str(p))
			filename.write("\n")

if __name__ == "__main__":
	generateAll()