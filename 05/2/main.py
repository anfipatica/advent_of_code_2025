
def	add_ids_to_list(valid_ids: list[tuple[int, int]], start: int, end: int) -> list[tuple[int, int]]:

	for index in range(0, len(valid_ids) + 1):
		if index == len(valid_ids):
			valid_ids.append((start, end))
		elif valid_ids[index][0] >= start:
			if index == 0:
				valid_ids.insert(0, (start, end))
			else:
				valid_ids.insert(index, (start, end))
			break
	return valid_ids

def	separate_file(file) -> list[tuple[int, int]]:

	numbers_splitted: list[str]
	valid_ids: list[tuple[int, int]] = []
	check_ids: list[int] = []

	for line in file:
		if line == "\n":
			break
		numbers_splitted = line.strip().split("-")
		valid_ids = add_ids_to_list(valid_ids, int(numbers_splitted[0]), int(numbers_splitted[1]))

	return valid_ids

def	count_ids(id_list: list[tuple[int, int]], index: int) -> bool:
	if not hasattr(count_ids, "biggest_id"):
		count_ids.biggest_id = 0
	id_n: int
	print("biggest_number %d" %(count_ids.biggest_id))
	if index != 0 and id_list[index][1] < count_ids.biggest_id: #total overlap, no new number
		print("0.    0")
		return 0
	elif index != 0 and id_list[index][0] < id_list[index - 1][1]: # overlap parcial
		id_n = id_list[index][1] - count_ids.biggest_id
		print("1.    %d" %(id_n))
	elif index != 0 and id_list[index][0] < count_ids.biggest_id:
		id_n = id_list[index][1] - count_ids.biggest_id
		print("3.    %d" %(id_n))
	else:
		id_n = id_list[index][1] - id_list[index][0] + 1
		print("2.    %d" %(id_n))
	if id_list[index][0] == count_ids.biggest_id or id_list[index][1] == count_ids.biggest_id:
		id_n -= 1
	count_ids.biggest_id = id_list[index][1]
	return id_n

def	main():
	valid_ids: list[tuple[int, int]] = []
	total_valid_ids: int = 0

	with open("./input.txt", "r") as file:
		valid_ids = separate_file(file)
		print("resulting list:")
		for id in valid_ids:
			print(id)
		print("----------------")
		for index in range(0, len(valid_ids)):
			print(f"now checking: {valid_ids[index]}")
			total_valid_ids += count_ids(valid_ids, index)
			print("")
	print("RESULT: %d" %(total_valid_ids))


### 323763676291254 TOO LOW
### 360341832208384 
### 360608726043689 TOO HIGH
### 360608726043727 TOO HIGH

if __name__ == "__main__":
	main()