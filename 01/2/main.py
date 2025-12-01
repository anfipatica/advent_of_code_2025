
def	rotate_dial(rotations: int, dial: int, dir: int, password: int) -> int:

	while rotations > 0:
		dial += dir
		if (dial < 0):
			dial = 99
		if (dial > 99):
			dial = 0
		if dial == 0:
			password += 1
		rotations -= 1
	return dial, password


def	main():
	dial: int = 50
	password: int = 0

	with open("./input", "r") as file:
		for line in file:
			if line[0] == 'L':
				dial, password = rotate_dial(int(line[1:]), dial, -1, password)
			else:
				dial, password = rotate_dial(int(line[1:]), dial, 1, password)
			print(dial)
	print("password: %d" %(password))


if __name__ == "__main__":
	main()
