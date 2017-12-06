def main():
	f = open("day2.txt", "r")
	quotients = []
	lines = list(f)
	for line in lines:
		value_line = [int(x) for x in line.split("\t")]
		for i in range(len(value_line)):
			value = value_line[i]
			for j in range(i+1, len(value_line)):
				alt = value_line[j]
				if value % alt == 0 or alt % value == 0:
					if value > alt:
						quotients.append(value / alt)
					else:
						quotients.append(alt/value)
					break
	f.close()
	print sum(quotients)
	


if __name__ == '__main__':
	main()