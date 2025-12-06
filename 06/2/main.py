
def	operate(numbers: list[list[int]], operands: list[str]):
	result:			int
	total_result:	int = 0
	for i in range(0, len(numbers)):
		result = 0
		print(numbers[i])
		for number in numbers[i]:
			if operands[i] == '*':
				if result == 0:
					result = 1
				if number != 0:
					result *= number
			elif operands[i] == '+':
				result += number
		print("result: %d" %(result))
		total_result += result
	print("TOTAL RESULT: %d" %(total_result))


def	chop_lines(number_lines: list[str]) -> tuple[list[int], list[str]]:
	space_index:	int = 0
	numbers:		list[int] = []
	chopped:		list[str] = []
	for i in range(0, len(number_lines)):
		if number_lines[i].find(" ") == -1:
			space_index = number_lines[i].find("\n")
		if space_index < number_lines[i].find(" "):
			space_index = number_lines[i].find(" ")

	for line in number_lines:

		numbers.append(int(line[:space_index].replace(" ", "0")))
		if space_index + 1 >= len(line) - 1:
			continue
		chopped.append(line[space_index + 1:])

	return (numbers, chopped)


def	to_cephalopod_numbers(numbers: list[int]) -> list[int]:
	cephalod:		list[int] = []
	cephalod_index:	int = 0
	index:			int = 0
	module:			int = 0

	for n in numbers:
		cephalod.append(0)
	while True:
		if cephalod_index == len(numbers):
			break
		if index == len(numbers):
			cephalod_index += 1
			index = 0
			continue
		module = numbers[index] % 10
		if module != 0:
			cephalod[cephalod_index] = cephalod[cephalod_index] * 10 + module
		if numbers[index] != 0:
			numbers[index] = int(numbers[index] / 10)
		index += 1

	return (cephalod)


def	extract_numbers(number_lines: list[str]) -> list[list[int]]:
	numbers:	list[int]
	cephalopod:	list[list[int]] = []

	while number_lines:
		numbers, number_lines = chop_lines(number_lines)
		cephalopod.append(to_cephalopod_numbers(numbers))
	return cephalopod


def	main():
	number_lines:	list[str] = []
	cephalopod:		list[list[int]]

	with open("input.txt", "r") as file:
		for line in file:
			if line.find("*") == -1 and line.find("+") == -1 :
				number_lines.append(line)
			else:
				cephalopod = extract_numbers(number_lines)
				operate(cephalopod, line.strip().split())


if __name__ == "__main__":
	main()