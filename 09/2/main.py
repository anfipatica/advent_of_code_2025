class	Coor:
	def	__init__(self, coor: list[int]):
		self.x = coor[0]
		self.y = coor[1]
	def	__init__(self, coor: list[str]):
		self.x = int(coor[0])
		self.y = int(coor[1])

	def	__str__(self) -> str:
		return (f"[{self.x},{self.y}]")

class	Rectangle:
	def	__init__(self, coor1: Coor, coor2: Coor):
		self.coor1: Coor = coor1
		self.coor2: Coor = coor2
		self.area = abs(self.coor1.x - self.coor2.x + 1) * abs(self.coor1.y - self.coor2.y + 1)

	def	__str__(self) -> str:
		return (f"{self.area}: coor1{self.coor1} coor2{self.coor2}")

def	is_valid(coor_list: list[Coor], rectangle: Rectangle):

	valid_checks: int

	for coor in coor_list:
		if coor is rectangle.coor1:
			continue
		valid_checks = 0
		if coor.y == rectangle.coor1.y:
			if rectangle.coor2.x < rectangle.coor1.x: # 2 <----- 1
				if coor.x <= rectangle.coor2.x:
					valid_checks += 1
			elif rectangle.coor2.x > rectangle.coor1.x: # 1 ---> 2
				if coor.x >= rectangle.coor2.x:
					valid_checks += 1
			else: # Both on same x axys. Automatically valid.
				return True
		if coor.x == rectangle.coor1.x:
			if rectangle.coor2.y < rectangle.coor1.y:
				if coor.y <= rectangle.coor2.y:
					valid_checks += 1
			elif rectangle.coor2.y > rectangle.coor1.y:
				if coor.y >= rectangle.coor2.y:
					valid_checks += 1
			else:
				return True
		if valid_checks == 2:
			return True
	return False

def	find_biggest_rectangle(coor: list[Coor]) -> Rectangle:
	biggest:	Rectangle = None
	current:	Rectangle

	for	i in range(0, len(coor)):
		for element in coor:
			if element is coor[i]:
				continue
			current = Rectangle(coor[i], element)
			if (is_valid(coor, current) == False):
				continue
			if not biggest or current.area > biggest.area:
				biggest = current
	return biggest


def	main():
	rectangle: Rectangle

	coor: list[Coor] = []

	with open("./input.txt", "r") as file:
		for line in file:
			coor.append(Coor(line.strip().split(",")))
	rectangle = find_biggest_rectangle(coor)
	print(rectangle)


if __name__ == "__main__":
	main()