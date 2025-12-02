def	check_number(number: str) -> bool:
	repetition: int = 0

	for pattern_len in range(1, len(number)):
		pattern: str = number[:pattern_len]
		repetition = number.count(pattern)
		if pattern_len * repetition != len(number):
			continue
		if repetition >= 2:
			print("INVALID ID. number: %s, pattern: %s" %(number, pattern))
			return True
	return False

def	check_range(start: int, end: int):
	if not hasattr(check_range, "invalid_ids_sum"):
		check_range.invalid_ids_sum = 0
	invalid_numbers: int = 0
	while start <= end:
		if check_number(str(start)) == True:
			invalid_numbers += 1
			check_range.invalid_ids_sum += start
		start += 1
	print("Invalid numbers for range that ends with %d: %d | SUM -> %d"
		%(end, invalid_numbers, check_range.invalid_ids_sum))

def	main():
	with open("./input.txt", "r") as file:
		input:str = file.read()
		ranges: list[str] = input.split(",")
		for range in ranges:
			splitted_range:list[str] = range.split("-")
			check_range(int(splitted_range[0]), int(splitted_range[1]))

if __name__ == "__main__":
	main()