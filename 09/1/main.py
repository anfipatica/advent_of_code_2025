class	Rectangle:
	def	__init__(self, coor1: list[int], coor2: list[int]):
		self.x1 = coor1[0]
		self.y1 = coor1[1]
		self.x2 = coor2[0]
		self.y2 = coor2[1]
		self.area = abs(self.x1 - self.x2 + 1) * abs(self.y1 - self.y2 + 1)

	def	__str__(self) -> str:
		return (f"{self.area}: coor1[{self.x1},{self.y1}] coor2[{self.x2},{self.y2}]")


def	find_biggest_rectangle(coor: list[list[int]]) -> Rectangle:
	biggest:	Rectangle = None
	current:	Rectangle

	for	i in range(0, len(coor)):
		for element in coor:
			if element is coor[i]:
				continue
			current = Rectangle(coor[i], element)
			if not biggest or current.area > biggest.area:
				biggest = current
	return biggest


def	main():
	rectangle: Rectangle

	coor: list[list[int]] = []

	with open("./input.txt", "r") as file:
		for line in file:
			coor.append([int(n) for n in line.strip().split(",")])
	rectangle = find_biggest_rectangle(coor)
	print(rectangle)


if __name__ == "__main__":
	main()