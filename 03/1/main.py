
def	find_biggest_digit(line:str, start: int, limit: int) -> int:
	biggest_digit: str = "0"
	index: int = 0

	for i in range(start, len(line) - 1):
		if biggest_digit[0] < line[i] and i < limit:
			biggest_digit = line[i]
			index = i
	return index


def	check_line(line: str) -> int:
	n1_index: int
	n2_index: int

	n1_index = find_biggest_digit(line, 0, len(line) - 2)
	n2_index = find_biggest_digit(line, n1_index + 1, len(line) - 1)
	joltage = int(line[n1_index]+line[n2_index])

	return joltage


def	main():
	total_joltage: int = 0

	with open("./input.txt", "r") as file:
		for line in file:
			total_joltage += check_line(line)
	print(total_joltage)

if __name__ == "__main__":
	main()