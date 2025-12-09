from sys import exit

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
		self.area = (abs(self.coor1.x - self.coor2.x) + 1) * (abs(self.coor1.y - self.coor2.y) + 1)

	def	__str__(self) -> str:
		return (f"{self.area}: coor1{self.coor1} coor2{self.coor2}")

def	vertical_check(coor_list: list[Coor], coor1: Coor, coor2: Coor, dir: int):
	if dir == 0:
		return True
	for c1 in range(0, len(coor_list)):
		if dir < 0:
			if coor_list[c1] is coor1 or coor_list[c1].y > coor2.y or coor_list[c1].x > coor1.x:
				continue
		else:
			if coor_list[c1] is coor1 or coor_list[c1].y < coor2.y or coor_list[c1].x > coor1.x:
				continue
		if coor_list[c1].x == coor1.x:
			return True
		for c2 in range(0, len(coor_list)):
			if coor_list[c2].y == coor_list[c1].y and coor_list[c2].x >= coor1.x:
				return True
	return False

def	horizontal_check(coor_list: list[Coor], coor1: Coor, coor2: Coor, dir: int):
	if dir == 0:
		return True
	for c1 in range(0, len(coor_list)):
		if printer == True:
			print(coor_list[c1])
		if dir < 0:
			if coor_list[c1] is coor1 or coor_list[c1].x > coor2.x or coor_list[c1].y > coor1.y:
				continue
		else:
			if coor_list[c1] is coor1 or coor_list[c1].x < coor2.x or coor_list[c1].y > coor1.y:
				continue
		if coor_list[c1].y == coor1.y:
			return True
		for c2 in range(0, len(coor_list)):
			if coor_list[c2].x == coor_list[c1].x and coor_list[c2].y >= coor1.y:
				return True
	return False

def	is_valid(coor_list: list[Coor], rectangle: Rectangle):

	valid_checks: int = 0

	if vertical_check(coor_list, rectangle.coor1, rectangle.coor2, rectangle.coor2.y - rectangle.coor1.y) == False:
		return False
	if horizontal_check(coor_list, rectangle.coor1, rectangle.coor2, rectangle.coor2.y - rectangle.coor1.y) == False:
		return False
	if vertical_check(coor_list, rectangle.coor2, rectangle.coor1, rectangle.coor1.y - rectangle.coor2.y) == False:
		return False
	if horizontal_check(coor_list, rectangle.coor2, rectangle.coor1, rectangle.coor1.y - rectangle.coor2.y) == False:
		return False
	return True



def	find_biggest_rectangle(coor: list[Coor]) -> Rectangle:
	biggest:	Rectangle = None
	current:	Rectangle

	for	i in range(0, len(coor)):
		print(f"{i} - {biggest}")
		for element in coor:
			if element is coor[i]:
				continue
			current = Rectangle(coor[i], element)
			if biggest and current.area <= biggest.area:
				continue
			if (is_valid(coor, current) == False):
				continue
			biggest = current
	return biggest


def	main():
	rectangle: Rectangle

	coor: list[Coor] = []

	with open("./input.txt", "r") as file:
		for line in file:
			coor.append(Coor(line.strip().split(",")))
	rectangle = find_biggest_rectangle(coor)

	print(f"\n\nRESULT: {rectangle}")


if __name__ == "__main__":
	main()