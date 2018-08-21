from collections import defaultdict

if __name__ == "__main__":
	with open("generated_output.txt", 'r') as filename:
		begin_dict = defaultdict(int)
		mid_dict = defaultdict(int)
		end_dict = defaultdict(int)
		item_amounts = defaultdict(int)
		temporal_slice = None
		
		for line in filename:
			items = eval(line)
			
			
			for i, item in enumerate(items):
				if i < 5:
					temporal_slice = begin_dict
				elif i < 10:
					temporal_slice = mid_dict
				else:
					temporal_slice = end_dict
				item_amounts[item] += 1
				temporal_slice[item] += 1
	
	for k, v in item_amounts.items():
		print(k, v)
		print("beg", begin_dict[k])
		print("mid", mid_dict[k])
		print("end", end_dict[k])
		print()
		
	print(len(item_amounts.items()))