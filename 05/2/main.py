
START:	int = 0
END:	int = 1

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

def	merge_overlaping_ranges(valid_ids: list[list], start: int, end: int) -> list[list]:
	overlap: bool = False
	if not valid_ids:
		valid_ids.append([start, end])

	for id_range in valid_ids:
		# SOLAPAMIENTO TOTAL
		if start <= id_range[START] and end >= id_range[END]: # el nuevo rango absorbe el anterior
			id_range[START] = start
			id_range[END] = end
			overlap = True
		elif id_range[START] <= start and id_range[END] >= end: # el nuevo rango es absorbido
			start = id_range[START]
			end = id_range[END]
			overlap = True
		
		# SOLAPAMIENTO PARCIAL
		elif start >= id_range[START] and start <= id_range[END]: # el inicio del nuevo rango está dentro del otro
			if end > id_range[END]: # partial overlap
				start = id_range[START]
				id_range[END] = end
			else: # total overlap
				start = id_range[START]
				end = id_range[END]
			overlap = True

		elif end >= id_range[START] and end <= id_range[END]:
			if start < id_range[END]:
				end = id_range[END]
				id_range[START] = start # partial overlap
			else: # total overlap
				start = id_range[START]
				end = id_range[END]
			overlap = True

	# SIN SOLAPAMIENTO, SE CREA NUEVO RANGO
	if overlap == False:
		valid_ids.append([start, end])
	return valid_ids


def	separate_file(file) -> list[list]:

	numbers_splitted: list[str]
	ordered_ids: list[list] = []
	valid_ids: list[list] = []
	check_ids: list[int] = []

	for line in file:
		if line == "\n":
			break
		numbers_splitted = line.strip().split("-")
		ordered_ids = add_ids_to_list(ordered_ids, int(numbers_splitted[0]), int(numbers_splitted[1]))
	
	for id_range in ordered_ids:
		valid_ids = merge_overlaping_ranges(valid_ids, id_range[START], id_range[END])

	
	return valid_ids

def	count_ids(id_list: list[list], index: int) -> bool:
	pass

def	main():
	valid_ids: list[list] = []
	total_valid_ids: int = 0

	with open("./input.txt", "r") as file:
		valid_ids = separate_file(file)
		print("resulting list:")
		for id in valid_ids:
			print(id)
		for id_range in valid_ids:
			total_valid_ids += id_range[END] - id_range[START] + 1

	print("RESULT: %d" %(total_valid_ids))


### 323763676291254 TOO LOW
### 360341832208384 
### 360341832208314

### 360341832208407
### 360608726043689 TOO HIGH
### 360608726043727 TOO HIGH

if __name__ == "__main__":
	main()