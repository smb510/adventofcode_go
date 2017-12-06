def main():
	valid = 0
	f = open("day4.txt", "r")
	lines = list(f)
	for line in lines:
		words = [''.join(sorted(word)) for word in line.strip().split(" ")]
		print words
		if len(set(words)) == len(words):
			valid += 1

	print valid

	f.close()

if __name__ == '__main__':
	main()