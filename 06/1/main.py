
def	operate(numbers: list[list[int]], operands: list[str]):
	result:			int
	total_result:	int = 0

	for j in range(0, len(numbers[0])):
		result = 0
		for i in range(0, len(numbers)):
			if operands[j] == '*':
				if result == 0:
					result = 1
				result *= numbers[i][j]
			elif operands[j] == '+':
				result += numbers[i][j]
			else:
				print("what")
		print("result: %d" %(result))
		total_result += result
	print("TOTAL RESULT: %d" %(total_result))


def	list_str_to_int(str_list: list[str]) -> list[int]:
	int_list: list[int] = []

	for element in str_list:
		if element:
			int_list.append(int(element))
	return int_list


def	main():
	splitted_line:	list[str]
	numbers:		list[list[int]] = []

	with open("input.txt", "r") as file:
		for line in file:
			splitted_line = line.strip().split()
			if splitted_line[0].isdigit():
				numbers.append(list_str_to_int(splitted_line))
			else:
				operate(numbers, splitted_line)


if __name__ == "__main__":
	main()