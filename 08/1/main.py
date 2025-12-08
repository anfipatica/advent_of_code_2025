
class	Box:
	def	__init__(self, x: int, y: int, z: int, index: int):
		self.x:			int = x
		self.y:			int = y
		self.z:			int = z
		self.circuit:	int = -1
	def	__str__(self) -> str:
		return "%d:%d:%d -> %d" %(self.x, self.y, self.z, self.circuit)


def	get_circuit(box: Box) -> int:
	return box.circuit


def	euclidean_distance(box1: Box, box2: Box) -> int:
	return ((box1.x - box2.x) * (box1.x - box2.x) +
			(box1.y - box2.y) * (box1.y - box2.y) +
			(box1.z - box2.z) * (box1.z - box2.z))


def	calculate_length(cirtuit_max: int, box_list: list[Box]):
	n_boxes: int
	circuit_len: list[int] = []

	total_len: int = 1
	for i in range(0, cirtuit_max):
		n_boxes = 0
		for box in box_list:
			if box.circuit == i:
				n_boxes += 1
		if n_boxes > 0:
			circuit_len.append(n_boxes)
	circuit_len.sort(reverse=True)

	for i in range(0,3):
		total_len *= circuit_len[i]

	print(total_len)


def	create_or_add_circuit(circuit: int, box_list: list[Box], b1: int, b2: int) -> tuple[int, list[Box]]:

	if box_list[b1].circuit >= 0 and box_list[b2].circuit >= 0 and box_list[b1].circuit ==box_list[b2].circuit:
		return circuit, box_list

	if box_list[b1].circuit >= 0:
		if box_list[b2].circuit >= 0:
			for box in box_list:
				if box is not box_list[b2] and box.circuit == box_list[b2].circuit:
					box.circuit = box_list[b1].circuit
		box_list[b2].circuit = box_list[b1].circuit
	elif box_list[b2].circuit >= 0:
		box_list[b1].circuit = box_list[b2].circuit
	else:
		box_list[b1].circuit = circuit
		box_list[b2].circuit = circuit
		circuit += 1
	return circuit, box_list


def	choose_conection(box_list: list[Box]) -> tuple[int, int]:
	if not hasattr(choose_conection, "last_distance"):
		choose_conection.last_distance = 0
	
	smallest_distance:	int = None
	distance:			int
	box1:			int
	box2:			int

	for i1 in range(0, len(box_list)):
		for i2 in range(0, len(box_list)):
			distance = euclidean_distance(box_list[i1], box_list[i2])
			if not smallest_distance or smallest_distance > distance:
				if box_list[i1] is box_list[i2]:
					continue
				if distance < choose_conection.last_distance:
					continue
				if distance == choose_conection.last_distance and box_list[i1].circuit == box_list[i2].circuit:
					continue
				smallest_distance = distance
				box1 = i1
				box2 = i2

	choose_conection.last_distance = smallest_distance
	return box1, box2


def	connect_junction_boxes(box_list: list[Box]):
	box1:			int
	box2:			int
	circuit:		int = 0

	for i in range(0,1000):
		box1, box2 = choose_conection(box_list)
		circuit, box_list = create_or_add_circuit(circuit, box_list, box1, box2)
		print(f"{i}.  {box_list[box1]} <-{box_list[box1].circuit}|{box_list[box2].circuit}-> {box_list[box2]}")

	box_list.sort(key=get_circuit)
	for element in box_list:
		print(element)

	calculate_length(circuit, box_list)


def	main():
	box_list: list[Box] = []
	splitted_n: list[str]
	index:		int = 0

	with open("./input.txt", "r") as file:
		for line in file:
			splitted_n = line.strip().split(",")
			box_list.append(Box(int(splitted_n[0]), int(splitted_n[1]), int(splitted_n[2]), index))
			index += 1
	
	connect_junction_boxes(box_list)

if __name__ == "__main__":
	main()