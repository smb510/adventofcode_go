def main():
	blocks = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
	configs = {}
	block_str = str(blocks)
	i = 0
	while block_str not in configs:	
		configs[block_str] = i
		blocks = redistribute(blocks)
		block_str = str(blocks)
		i += 1
	print(configs[block_str], i)



def redistribute(banks):
	max_val = max(banks)
	idx = banks.index(max_val)
	banks[idx] = 0
	while max_val > 0:
		idx = (idx + 1) % len(banks)
		banks[idx] += 1
		max_val -= 1
	return banks



if __name__ == '__main__':
	main()