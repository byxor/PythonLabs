# -- Class Declarations -----------------


class Player(object):
	
	def __init__(self, name, handicap, strokes):
		self.name = name
		self.handicap = handicap
		self.strokes = strokes

	def __str__(self):
		s = "P: {}, handi={}, strokes={}"
		return s.format(self.name, self.handicap, self.strokes)
	
class Hole(object):

	def __init__(self, index, par):
		self.index = index
		self.par = par

	def __str__(self):
		s = "Hole {}, par {}."
		return s.format(self.index, self.par)


# -- Useful Methods ---------------------


def _calc_free_strokes(handicap, index):
	if handicap == 6:
		if 1 <= index <= 6:
			return 1
		return 0
	elif handicap == 18:
		return 1
	elif handicap == 25:
		if 1 <= index <= 7:
			return 2
		return 1
	elif handicap == 36:
		return 2
	elif handicap == 40:
		if 1 <= index <= 4:
			return 3
		elif 5 <= index <= 18:
			return 2
		return 0
	elif handicap == 54:
		return 3
	return 0


def _calc_net_strokes(strokes_taken, free_strokes):
	return strokes_taken - free_strokes


def _calc_score_to_par(net_strokes, hole_par):
	return net_strokes - hole_par


def _calc_points_on_hole(score_to_par):
	if score_to_par >= 2:
		return 0
	return 2 - score_to_par


def calc_points_on_hole(h_index, h_par, p_handicap, p_strokes_taken):
	p_free_strokes = _calc_free_strokes(p_handicap, h_index)
	p_net_strokes = _calc_net_strokes(p_strokes_taken, p_free_strokes)
	p_score_to_par = _calc_score_to_par(p_net_strokes, h_par)
	p_points_on_hole = _calc_points_on_hole(p_score_to_par)
	return p_points_on_hole


def calc_stableford(player, hole_list):
	stableford = 0
	for item in player.strokes.items():
		hole_index = item[0]
		strokes_taken = item[1]
		stableford += calc_points_on_hole(hole_index, hole_list[hole_index-1].par, player.handicap, strokes_taken)
	return stableford


# -- IO Code ------------------------


def process_holes(parline, indexline):
	hole_list = []

	pars = parline.split(" ")
	inds = indexline.split(" ")

	for i in range(0, len(pars)):
		hole = Hole(int(inds[i]), int(pars[i]))
		hole_list.append(hole)

	return hole_list


def process_players(playerlines):
	return [process_player(playerline) for playerline in playerlines]


def process_player(playerline):
	info = playerline.split(" ")
	pname_length = _get_pname_length(info)
	pname = _get_pname(info, pname_length)
	phandicap = int(info[pname_length])
	strokes = {}
	for i in range(pname_length+1, len(info)):
		if info[i] == "X":
			continue
		strokes[i+1] = int(info[i])
	return Player(pname, phandicap, strokes)


def _get_pname_length(info):
	return len(info)-19


def _get_pname(info, pname_length):
	pname = ""
	for i in range(0, pname_length):
		if i>0:
			pname += " "
		pname+=info[i]
	return pname


# -- Driver Code ------------------------


def main():
	import sys
	input = [line.strip() for line in sys.stdin]
	hole_list = process_holes(input[0], input[1])

	#[print(hole) for hole in hole_list]

	player_list = process_players(input[2:len(input)])

	for player in player_list:
		print(calc_stableford(player, hole_list))

	#[print(player) for player in player_list]

	stableford = {}
	for player in player_list:
		stableford[player] = calc_stableford(player, hole_list)

	print(stableford)

if __name__ == "__main__":
	main()
