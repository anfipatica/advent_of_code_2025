
g_split: int = 0

def	throw_beam(diagram: list[bytearray], y: int, x: int) -> list[bytearray]:
	global	g_split
	if y >= len(diagram):
		return diagram
	if diagram[y][x] == ord("."):
		diagram[y][x] = ord("|")
		throw_beam(diagram, y + 1, x)
	elif diagram[y][x] == ord("^"):
		g_split += 1
		throw_beam(diagram, y, x - 1)
		throw_beam(diagram, y, x + 1)

	return diagram

def	main():
	global	g_split
	diagram: list[bytearray] = []
	with open("./input.txt", "r") as file:
		for line in file:
			diagram.append(bytearray(line.strip(), "utf-8"))

	diagram = throw_beam(diagram, 1, diagram[0].find(ord("S")))
	for line in diagram:
		print(line)
	print(g_split)


if __name__ == "__main__":
	main()