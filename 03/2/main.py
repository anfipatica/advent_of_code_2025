def	find_biggest_digit(line:str, start: int, limit: int) -> int:
	biggest_digit: str = "0"
	index: int = 0

	for i in range(start, len(line) - limit - 1):
		if biggest_digit[0] < line[i]:
			if line[i] == '9':
				return i
			biggest_digit = line[i]
			index = i
	return index


def	check_line(line: str) -> int:
	index: int = -1
	joltage: int = 0

	for i in range(12, 0, -1):
		index = find_biggest_digit(line, index + 1, i - 1)
		joltage = joltage * 10 + int(line[index])
	return joltage


def	main():
	total_joltage: int = 0

	with open("./input.txt", "r") as file:
		for line in file:
			total_joltage += check_line(line)
	print(total_joltage)

if __name__ == "__main__":
	main()