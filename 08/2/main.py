
class	Box:
	def	__init__(self, x: int, y: int, z: int, index: int):
		self.x:			int = x
		self.y:			int = y
		self.z:			int = z
		self.circuit_id:	int = -1
	def	__str__(self) -> str:
		return "%d:%d:%d -> %d" %(self.x, self.y, self.z, self.circuit_id)

class	Circuit:
	def	__init__(self, box1: Box):
		self.circuit: list[Box] = [box1]
		self.distance: int = 0

def	get_circuit(box: Box) -> int:
	return box.circuit_id


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
			if box.circuit_id == i:
				n_boxes += 1
		if n_boxes > 0:
			circuit_len.append(n_boxes)
	circuit_len.sort(reverse=True)

	for i in range(0,3):
		total_len *= circuit_len[i]

	print(total_len)


def	create_or_add_circuit(circuit: int, box_list: list[Box], b1: int, b2: int) -> tuple[int, list[Box]]:

	if box_list[b1].circuit_id >= 0 and box_list[b2].circuit_id >= 0 and box_list[b1].circuit_id ==box_list[b2].circuit_id:
		return circuit, box_list

	if box_list[b1].circuit_id >= 0:
		if box_list[b2].circuit_id >= 0:
			for box in box_list:
				if box is not box_list[b2] and box.circuit_id == box_list[b2].circuit_id:
					box.circuit_id = box_list[b1].circuit_id
		box_list[b2].circuit_id = box_list[b1].circuit_id
	elif box_list[b2].circuit_id >= 0:
		box_list[b1].circuit_id = box_list[b2].circuit_id
	else:
		box_list[b1].circuit_id = circuit
		box_list[b2].circuit_id = circuit
		circuit += 1
	return circuit, box_list


def	choose_conection(box_list: list[Box], last_box: int, circuit: Circuit) -> Circuit:

	smallest_distance:	int = None
	distance:			int

	if (len(circuit.circuit) == len(box_list)):
		print(f":: {circuit.circuit[0]} - {circuit.circuit[1]} -> {circuit.distance}")
		return circuit
	for i in range(0, len(box_list)):
		if box_list[i].circuit_id == abs(box_list[last_box].circuit_id):
			continue
		distance = euclidean_distance(box_list[i], box_list[last_box])
		if not smallest_distance or smallest_distance > distance:
			if box_list[i] is box_list[last_box]:
				continue
			smallest_distance = distance
			circuit.distance += distance
			box_list[i].circuit_id = 1
			circuit.circuit.append(box_list[i])

			print(f"{circuit.distance} -> ")
			return (choose_conection(box_list, i, circuit))


def	connect_junction_boxes(box_list: list[Box]):
	box1:			int
	box2:			int = 0
	circuit_id:		int = 0
	total_distance:	int = 0
	circuit:		Circuit = Circuit(box_list[0])

	for i in range(0,len(box_list)): #quizas +1 ??
		circuit = choose_conection(box_list, box2, circuit)
		for element in circuit.circuit:
			print(element)
		box1 = i
		circuit = Circuit(box_list[box1])
		print(f"{i}.  {box_list[box1]} <-{box_list[box1].circuit_id}|{box_list[box2].circuit_id}-> {box_list[box2]}")

	# box_list.sort(key=get_circuit)
	# for element in box_list:
	# 	print(element)

	# calculate_length(circuit, box_list)


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