# -- Class Declarations -----------------

class Player():
	
	def __init__(self, name, handicap, strokes):
		self.name = name
		self.handicap = handicap
		self.strokes = strokes
		
	def calc_stableford(self):
		stableford = 0
		for item in self.strokes.items():
			if item[1] != "X":
				stableford = stableford + int(item[1])
		return stableford
	
	
class Hole:

	def __init__(self, index, par):
		self.index = index
		self.par = par


# -- Useful Methods ---------------------

def calc_free_strokes(handicap, hole_index):
	if handicap == 6:
		if 1 <= hole_index <= 6:
			return 1
		return 0
	elif handicap == 18:
		return 1
	elif handicap == 25:
		if 1 <= hole_index <= 7:
			return 2
		return 1
	elif handicap == 36:
		return 2


def calc_net_strokes(strokes_taken, free_strokes):
	return strokes_taken - free_strokes


def calc_score_to_par(net_strokes, hole_par):
	return net_strokes - hole_par


def calc_points_on_hole(score_to_par):
	if score_to_par >= 2:
		return 0
	return 2 - score_to_par


# -- Driver Code ------------------------

import sys


def main():
	stdin = list(sys.stdin)
	hole_list = process_holes(stdin)
	player_list = process_players(stdin, hole_list)
	print_results(player_list)


def process_holes(stdin):
	hole_list = []

	par_string = stdin[0].strip()
	par_list = par_string.split(" ")
	index_string = stdin[1].strip()
	index_list = index_string.split()

	for i in range(0, len(par_list)):
		par = int(par_list[i])
		index = int(index_list[i])
		hole = Hole(index, par)

		hole_list.append(hole)

	return hole_list


def process_players(stdin, hole_list):

	player_list = []
	for i in range(2, len(stdin)):

		player_string = stdin[i].strip()
		player_attributes = player_string.split(" ")

		#print(player_attributes)
		
		player_name_length = len(player_attributes) - len(hole_list) - 1
		#print(player_name_length)
		
		player_name = ""
		for i in range(0, player_name_length):
			player_name = player_name + player_attributes[i]
			if i < player_name_length - 1:
				player_name = player_name + " "
		
		#print('"{}"'.format(player_name))
		
		player_handicap = player_attributes[player_name_length]

		#print(player_handicap)
		
		player_strokes = {}
		for j in range(player_name_length+1, len(player_attributes)):
			strokes = player_attributes[j]
			player_strokes[hole_list[j-player_name_length-1].index] = strokes

		#print(player_strokes)
			
		player = Player(player_name, player_handicap, player_strokes)
		player_list.append(player)
		
	return player_list

def print_results(players):
	for player in players:
		print ("{:>18} : {}".format(player.name, player.calc_stableford()))


if __name__ == "__main__":
	main()