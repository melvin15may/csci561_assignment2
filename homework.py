from time import time

def game_score(play, opposite_play, game_space, state):
	play_value = 0
	for i in state[play]:
		play_value = play_value + game_space[i[0]][i[1]]
	neg_play_value = 0
	for i in state[opposite_play]:
		neg_play_value = neg_play_value + game_space[i[0]][i[1]]
	return (play_value - neg_play_value)

def stake(n, play, opposite_play, current_state):
	"""
	Get all states formed when STAKE action performed
	"""
	total_occupied = current_state["X"] + current_state["O"] 
	"""
		states = [{
			"X": ...,
			"O": ...,
			"type" : "stake"
		},{
		...
		}]
	"""
	states = []
	board_range = range(n) 
	for i in board_range:
		for j in board_range:
			if not [i,j] in total_occupied:
				temp_play = {}
				temp_play[play] = current_state[play] + [[i,j]]
				temp_play[opposite_play] = current_state[opposite_play]
				#temp_play[play].append()
				temp_play["move"] = [i,j]
				temp_play["type"] = "Stake"
				states.append(temp_play)

	return states

def raid(n, play, opposite_play, current_state):
	""" 
	Get all states formed on raid
	"""
	total_occupied = current_state["X"] + current_state["O"] 
	states = []
	current_state_play = current_state[play]
	current_state_opposite_play = current_state[opposite_play]

	def get_neighbors(pos):
		return {
			"left": [pos[0], (pos[1] - 1)], 
			"right": [pos[0], (pos[1] + 1)], 
			"bottom": [(pos[0] + 1), pos[1]], 
			"up" : [(pos[0] - 1), pos[1]]
			}
	
	def board_conditions(pos):
		if pos in total_occupied:
			return False
		if pos[0] < 0:
			return False
		if pos[0] >= n:
			return False
		if pos[1] < 0:
			return False
		if pos[1] >= n:
			return False
		return True

	def conquer_opposite_play(opposite_player_pos, pos):
		nb = get_neighbors(pos)
		pos_array = [pos]
		if nb['left'] in opposite_player_pos:
			pos_array.append(nb['left'])
		if nb['right'] in opposite_player_pos:
			pos_array.append(nb['right'])
		if nb['bottom'] in opposite_player_pos:
			pos_array.append(nb['bottom'])
		if nb['up'] in opposite_player_pos:
			pos_array.append(nb['up'])
		return pos_array

	for pos in current_state_play:
		nb = get_neighbors(pos)
		if board_conditions(nb['left']):
			new_state = {}
			conquered_play = conquer_opposite_play(current_state_opposite_play,nb['left'])
			new_state[play] = current_state[play] + conquered_play
			new_state[opposite_play] = [xx for xx in current_state_opposite_play if xx not in conquered_play]
			new_state["move"] = nb["left"]
			new_state["type"] = "Raid"
			states.append(new_state)		
		if board_conditions(nb['right']):
			new_state = {}
			conquered_play = conquer_opposite_play(current_state_opposite_play,nb['right'])
			new_state[play] = current_state[play] + conquered_play
			new_state[opposite_play] = [xx for xx in current_state_opposite_play if xx not in conquered_play]
			new_state["move"] = nb["right"]
			new_state["type"] = "Raid"
			states.append(new_state)		
		if board_conditions(nb['bottom']):
			new_state = {}
			conquered_play = conquer_opposite_play(current_state_opposite_play,nb['bottom'])
			new_state[play] = current_state[play] + conquered_play
			new_state[opposite_play] = [xx for xx in current_state_opposite_play if xx not in conquered_play]
			new_state["move"] = nb["bottom"]
			new_state["type"] = "Raid"
			states.append(new_state)		
		if board_conditions(nb['up']):
			new_state = {}
			conquered_play = conquer_opposite_play(current_state_opposite_play,nb['up'])
			new_state[play] = current_state[play] + conquered_play
			new_state[opposite_play] = [xx for xx in current_state_opposite_play if xx not in conquered_play]
			new_state["move"] = nb["up"]
			new_state["type"] = "Raid"
			states.append(new_state)
	return states

def main():
	try:
		input_file = open("input.txt","r")
		input_lines = input_file.readlines()

		input_lines = [l.strip("\n") for l in input_lines]

		input_file.close()

		n = int(input_lines.pop(0))
		mode = input_lines.pop(0)
		play = input_lines.pop(0)
		depth = int(input_lines.pop(0))	

		opposite_play = "X"
		if play == "X":
			opposite_play ="O"

		cell_values = []

		"""
			board_loc = {
				"X"  : [[x,y]...]

			}
		"""

		board_loc = {
			"X": [],
			"O": []
		}

		for i in range(n):
			cell_values.append([int(x) for x in	input_lines.pop(0).split(" ")])

		for i in range(n):
			row = input_lines.pop(0)
			for j,jj in enumerate(row):
				if jj == "X":
					board_loc["X"].append([i,j])
				elif jj == "O":
					board_loc["O"].append([i,j])

		def minimax():
			def max_value(state, ddepth = 0):
				if ddepth >= depth:
					return game_score(play, opposite_play, cell_values, state)
				v = -float("inf")
				states = stake(n, play, opposite_play, state) + raid(n, play, opposite_play, state)
				for s in states:
					v = max(v, min_value(s.copy(), (ddepth + 1)))
				return v

			def min_value(state, ddepth = 0):
				if ddepth >= depth:
					return game_score(play, opposite_play, cell_values, state)
				v = float("inf")
				states = stake(n, opposite_play, play, state) + raid(n, opposite_play, play, state)
				for s in states:
					v = min(v, max_value(s.copy(), (ddepth + 1)))
				return v

			states = stake(n, play, opposite_play, board_loc) + raid(n, play, opposite_play, board_loc)
			max_score = -float("inf")
			max_score_state = {}
			max_move_type = ""

			for s in states:
				mm = min_value(s.copy(), 1)
				if max_score < mm:
					max_score = mm
					max_move_type = s["type"]
					max_score_state = s
				elif (max_score == mm) and (s["type"] == "Stake") and (max_move_type == "Raid"):
					max_score_state = s
					max_move_type = s["type"]

			write_file(max_score_state)

		def alphabeta():
			def max_value(state, alpha, beta, ddepth = 0):
				if ddepth >= depth:
					return game_score(play, opposite_play, cell_values, state)
				v = -float("inf")
				states = stake(n, play, opposite_play, state) + raid(n, play, opposite_play, state)
				for s in states:
					v = max(v, min_value(s.copy(), alpha, beta, ddepth+1))
					if v >= beta:
						return v
					alpha = max(alpha, v)
				return v

			def min_value(state, alpha, beta, ddepth=0):
				if ddepth >= depth: 
					return game_score(play, opposite_play, cell_values, state)
				v = float("inf")
				states = stake(n, opposite_play, play, state) + raid(n, opposite_play, play, state)
				#print states
				for s in states:
					v = min(v, max_value(s.copy(), alpha, beta, ddepth+1))
					if v <= alpha:
						return v
					beta = min(beta, v)
				return v

			states = stake(n, play, opposite_play, board_loc) + raid(n, play, opposite_play, board_loc)
			
			max_score = -float("inf")
			max_score_state = {}
			max_move_type = ""
			for s in states:
				mm = min_value(s, -float("inf"), float("inf"), 1)
				if max_score < mm:
					max_score = mm
					max_score_state = s.copy()
					max_move_type = s["type"]
				elif (max_score == mm) and (s["type"] == "Stake") and (max_move_type == "Raid"):	
					max_score_state = s
					max_move_type = s["type"]
			write_file(max_score_state)


		def write_file(state, file_name="output.txt"):
			s = "%s%s %s\n" % (chr(65 + state["move"][1]), str(state["move"][0]+1), state["type"] )
			for i in range(n):
				for j in range(n):
					if [i,j] in state["X"]:
						s += "X"
					elif [i,j] in state["O"]:
						s += "O"
					else: 
						s += "."
				s = s + "\n"
			s.strip("\n")
			target = open(file_name,"w")
			target.write(s)
			target.close()

		if mode == "MINIMAX":
			minimax()
		elif mode == "ALPHABETA":
			alphabeta()


	except IOError:
		print "IO Error"

st = time()
main()
print time() - st