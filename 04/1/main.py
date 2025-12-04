
def	check_tile(map: list[str], y: int, x: int) -> bool:
	if y < 0 or x < 0 or y >= len(map) or x >= len(map[y]):
		return False
	if map[y][x] == '@':
		return True
	return False
	
def	check_area(map: list[str], y: int, x: int) -> bool:
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

def	read_map(map: list[str]) -> int:
	reachable_rolls:	int = 0
	y:					int = 0
	x:					int

	while y < len(map):
		x = 0
		while x < len(map[y]):
			if map[y][x] == '@':
				reachable_rolls += check_area(map, y, x)
			x += 1
		y += 1
	print(reachable_rolls)

def	main():
	map: list[str] = []

	with open("./input.txt", "r") as file:
		for line in file:
			map.append(line.removesuffix("\n"))
	read_map(map)

if __name__ == "__main__":
	main()