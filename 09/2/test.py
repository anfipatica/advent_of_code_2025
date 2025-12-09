#coor1[2,3] coor2[9,5]
#coor1[9,5] coor2[2,3]

def	is_valid(coor_list: list[Coor], rectangle: Rectangle):

	valid_checks: int = 0

	# First let's check coor1:
	#  check collition on y axys: |
	if rectangle.coor2.y < rectangle.coor1.y: # ↑
		for c1 in range(0, len(coor_list)):
			if coor_list[c1] is rectangle.coor1 or coor_list[c1].y > rectangle.coor1.y or coor_list[c1].x > rectangle.coor1.x:
				continue
			if coor_list[c1].x == rectangle.coor1.x:
				valid_checks += 1
				break
			for c2 in range(0, len(coor_list)):
				if coor_list[c2].y == coor_list[c1].y and coor_list[c2].x >= rectangle.coor1.x:
					valid_checks += 1
					break

	elif rectangle.coor2.y > rectangle.coor1.y: # ↓ 
		for c1 in range(0, len(coor_list)):
			if coor_list[c1] is rectangle.coor1 or coor_list[c1].y < rectangle.coor1.y or coor_list[c1].x > rectangle.coor1.x:
				continue
			if coor_list[c1].x == rectangle.coor1.x:
				valid_checks += 1
				break
			for c2 in range(0, len(coor_list)):
				if coor_list[c2].y == coor_list[c1].y and coor_list[c2].x >= rectangle.coor1.x:
					valid_checks += 1
					break
	if valid_checks < 1:
		return False
	

def	horizontal_check(coor_list: list[Coor], coor1: Coor, coor2: Coor):

	if coor2.y < coor1.y: # ↑
		for c1 in range(0, len(coor_list)):
			if coor_list[c1] is coor1 or coor_list[c1].y > coor2.y or coor_list[c1].x > coor1.x:
				continue
			if coor_list[c1].x == coor1.x:
				valid_checks += 1
				break
			for c2 in range(0, len(coor_list)):
				if coor_list[c2].y == coor_list[c1].y and coor_list[c2].x >= coor1.x:
					valid_checks += 1
					break

	elif coor2.y > coor1.y: # ↓ 
		for c1 in range(0, len(coor_list)):
			if coor_list[c1] is coor1 or coor_list[c1].y < coor2.y or coor_list[c1].x > coor1.x:
				continue
			if coor_list[c1].x == coor1.x:
				valid_checks += 1
				break
			for c2 in range(0, len(coor_list)):
				if coor_list[c2].y == coor_list[c1].y and coor_list[c2].x >= coor1.x:
					valid_checks += 1
					break
	if valid_checks < 1:
		return False