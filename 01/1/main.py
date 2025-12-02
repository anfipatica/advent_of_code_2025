
def	rotate_dial(rotations: int, dial: int, dir: int) -> int:

	while rotations > 0:
		dial += dir
		if (dial < 0):
			dial = 99
		if (dial > 99):
			dial = 0
		rotations -= 1
	return dial


def	main():
	dial: int = 50
	password: int = 0

	with open("./input.txt", "r") as file:
		for line in file:
			if line[0] == 'L':
				dial = rotate_dial(int(line[1:]), dial, -1)
			else:
				dial = rotate_dial(int(line[1:]), dial, 1)
			if dial == 0:
				password += 1
			print(dial)
	print("password: %d" %(password))


if __name__ == "__main__":
	main()
