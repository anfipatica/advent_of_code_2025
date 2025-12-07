def	throw_beam(diagram: list[list[int]], s_y: int, s_x: int) -> list[list[int]]:

	diagram[s_y][s_x] = 1

	for y in range(1, len(diagram)):
		for x in range(0, len(diagram[y])):
			if diagram[y][x] > 0 and y + 1 < len(diagram):
				if diagram[y + 1][x] == -1:
					diagram[y + 1][x - 1] += diagram[y][x]
					diagram[y + 1][x + 1] += diagram[y][x]
				elif diagram[y + 1][x] == 0:
					diagram[y + 1][x] = diagram[y][x]
				else:
					diagram[y + 1][x] += diagram[y][x]
	return diagram

def	main():
	diagram: list[list[int]] = []
	with open("./input.txt", "r") as file:
		i:int = 0
		x: int
		for line in file:
			if line:
				diagram.append([])
			for char in line.strip():
				if char == ".":
					diagram[i].append(0)
				elif char == "S":
					diagram[i].append(-2)
					x = line.find("S")
				else:
					diagram[i].append(-1)
			i += 1

	diagram = throw_beam(diagram, 1, x)
	for line in diagram:
		print(line)
	timelines: int = 0

	for char in diagram[len(diagram) - 2]:
		if char > 0:
			timelines += char
	print(timelines)


if __name__ == "__main__":
	main()