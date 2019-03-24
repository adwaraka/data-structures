'''
There is a rabbit that starts in the middle of an n x m matrix, n > 0, m > 0.
Each element of a matrix is an integer representing points gained for being on the spot. 
If there are multiple possible "middles" then choose the one which has the highest point value to start on. 
On each iteration, the rabbit can move up, left, right, or down. 
The rabbit will always move to the next spot with the highest point value 
and will "consume" those points (set the point value in that position to 0). 
The rabbit spots when all positions around it are 0s. 
Calculate how many points the rabbit will score for a given m x n matrix.

Padding the Garden with zeroes to skip boundary conditions
'''
def potential_center(garden):
	row = len(garden)
	col = len(garden[0])
	if row%2 == 0 and col%2 == 0:
		higher_carrot_count = {'1': garden[row//2][col//2],
			'2': garden[row//2-1][col//2],
			'3': garden[row//2][col//2-1],
			'4': garden[row//2-1][col//2-1]
			}
		sorted_d = sorted(higher_carrot_count.items(), key=lambda (k,v): v, reverse=True)
		if sorted_d[0][0] is '1':
			potential_center_x, potential_center_y = row//2, col//2
		elif sorted_d[0][0] is '2':
			potential_center_x, potential_center_y = row//2-1 , col//2
		elif sorted_d[0][0] is '3':
			potential_center_x, potential_center_y = row//2, col//2-1 
		else:
			potential_center_x, potential_center_y = row//2-1, col//2-1 
	elif row%2 != 0 and col%2 == 0:
		higher_carrot_count = {'1': garden[row//2][col//2], '2': garden[row//2][col//2-1]}
		sorted_d = sorted(higher_carrot_count.items(), key=lambda (k,v): v, reverse=True)
		if sorted_d[0][0] is '1':
			potential_center_x, potential_center_y = row//2, col//2
		else:
			potential_center_x, potential_center_y = row//2 , col//2-1
	elif row%2 == 0 and col%2 != 0:
		higher_carrot_count = {'1': garden[row//2][col//2], '2': garden[row//2-1][col//2]}
		sorted_d = sorted(higher_carrot_count.items(), key=lambda (k,v): v, reverse=True)
		if sorted_d[0][0] is '1':
			potential_center_x, potential_center_y = row//2, col//2
		else:
			potential_center_x, potential_center_y = row//2-1, col//2
	else:
		potential_center_x, potential_center_y = row//2, col//2
	return potential_center_x, potential_center_y 


def hungry_rabbit(garden):
	starting_pos_x, starting_pos_y = potential_center(garden)
	carrots_eaten = garden[starting_pos_x][starting_pos_y]
	cur_x, cur_y = starting_pos_x, starting_pos_y
	print "Position {}, {} and currently eaten carrot quantity {}".format(cur_x - 1, cur_y - 1, carrots_eaten)
	garden[cur_x][cur_y] = 0
	while get_adjacent_squares_carrot(garden, cur_x, cur_y) != (0, 0, 0, 0):
		new_pos_x, new_pos_y = get_next_max_carrot(garden, cur_x, cur_y)
		carrots_eaten+=garden[new_pos_x][new_pos_y]
		garden[new_pos_x][new_pos_y] = 0
		print "Position {}, {} and currently eaten carrot quantity {}".format(new_pos_x - 1, new_pos_y - 1, carrots_eaten)
		cur_x, cur_y = new_pos_x, new_pos_y
	return carrots_eaten


def get_adjacent_squares_carrot(garden, cur_x, cur_y):
	return garden[cur_x+1][cur_y], garden[cur_x-1][cur_y], garden[cur_x][cur_y+1], garden[cur_x][cur_y-1]


def get_next_max_carrot(garden, cur_x, cur_y):
	carrot_count = {
	'1' : garden[cur_x+1][cur_y], 
	'2': garden[cur_x-1][cur_y], 
	'3': garden[cur_x][cur_y+1], 
	'4': garden[cur_x][cur_y-1]
	}
	sorted_d = sorted(carrot_count.items(), key=lambda (k,v): v, reverse=True)
	#print sorted_d
	if sorted_d[0][0] is '1':
		new_pos_x, new_pos_y = cur_x+1, cur_y
	elif sorted_d[0][0] is '2':
		new_pos_x, new_pos_y = cur_x-1, cur_y
	elif sorted_d[0][0] is '3':
		new_pos_x, new_pos_y = cur_x, cur_y+1 
	else:
		new_pos_x, new_pos_y = cur_x, cur_y-1 
	return new_pos_x, new_pos_y


#TODO Handle the boundary conditions. Currently adding a padding logic
if __name__ == "__main__":
    garden = [[5, 7, 8, 6, 3],
    [0, 0, 7, 0, 4],
    [4, 6, 3, 4, 9],
    [3, 1, 0, 5, 8]]
    for row in garden:
    	row.insert(0, 0)
    	row.append(0)
    upper_lower_boundary = [0]*len(garden[0])
    garden.insert(0, upper_lower_boundary)
    garden.append(upper_lower_boundary)
    print "Carrots Eaten: {}".format(hungry_rabbit(garden)) 
