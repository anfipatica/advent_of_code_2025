
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

def	add_check_ids_to_list(check_ids: list[int], id: int) -> list[int]:

	for index in range(0, len(check_ids) + 1):
		if index == len(check_ids):
			check_ids.append(id)
		elif check_ids[index] >= id:
			if index == 0:
				check_ids.insert(0, id)
			else:
				check_ids.insert(index, id)
			break
	return check_ids


def	separate_file(file) -> tuple[list[tuple[int, int]], list[int]]:

	numbers_splitted: list[str]
	valid_ids: list[tuple[int, int]] = []
	check_ids: list[int] = []

	for line in file:
		if line == "\n":
			break
		numbers_splitted = line.strip().split("-")
		valid_ids = add_ids_to_list(valid_ids, int(numbers_splitted[0]), int(numbers_splitted[1]))
	for line in file:
		check_ids = add_check_ids_to_list(check_ids, int(line.strip()))
	return valid_ids, check_ids

def	check_id(id_list: list[tuple[int, int]], id: int) -> bool:
	if not hasattr(check_id, "last_index"):
		check_id.last_index: int = 0

	for index in range(check_id.last_index, len(id_list)):
		check_id.last_index = index
		print("id: %d - index: %d" %(id, index))
		if id < id_list[index][0]: #Smaller than the last checked range, invalid.
			return False
		elif id <= id_list[index][1]: # Between the last checked range, valid.
			return True
	print("salimos por aqui con el numero %d", id)
	return False

#1410076818762
#2096639243989

def	main():
	valid_ids: list[tuple[int, int]] = []
	check_ids: list[int] = []
	total_valid_ids: int = 0

	with open("./input.txt", "r") as file:
		valid_ids, check_ids = separate_file(file)
		for id in check_ids:
			total_valid_ids += check_id(valid_ids, id)
	print(total_valid_ids)


if __name__ == "__main__":
	main()