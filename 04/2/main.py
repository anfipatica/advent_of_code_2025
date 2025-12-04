
def	check_tile(map: list[bytearray], y: int, x: int) -> bool:
	if y < 0 or x < 0 or y >= len(map) or x >= len(map[y]):
		return False
	if map[y][x] == ord('@'):
		return True
	return False
	
def	check_area(map: list[bytearray], y: int, x: int) -> bool:
	rolls: int = 0
	rolls += check_tile(map, y - 1, x - 1)
	rolls += check_tile(map, y - 1, x)
	rolls += check_tile(map, y - 1, x + 1)
	rolls += check_tile(map, y, x - 1)
	rolls += check_tile(map, y, x + 1)
	rolls += check_tile(map, y + 1, x - 1)
	rolls += check_tile(map, y + 1, x)
	rolls += check_tile(map, y + 1, x + 1)
	if rolls >= 4:
		return False
	return True

def	read_map(map: list[bytearray]) -> tuple[int, list[bytearray]]:
	reachable_rolls:	int = 0
	is_reachable:		bool
	y:					int = 0
	x:					int

	while y < len(map):
		x = 0
		while x < len(map[y]):
			if map[y][x] == ord('@'):
				is_reachable = check_area(map, y, x)
				if is_reachable == True:
					reachable_rolls += 1
					map[y][x] = ord('x')
			x += 1
		y += 1
	return reachable_rolls, map

def	main():
	total_reachable_rolls:	int = 0
	reachable_rolls:		int = -1
	
	map: list[bytearray] = []

	with open("./input.txt", "r") as file:
		for line in file:
			map.append(bytearray(line.strip(), "utf-8"))

	while reachable_rolls != 0:
		reachable_rolls, map = read_map(map)
		total_reachable_rolls += reachable_rolls
	print(total_reachable_rolls)

if __name__ == "__main__":
	main()