from copy import deepcopy

with open("input.txt", "r") as f:
	codes_master = [int(i) for i in f.read().split(",")]

def main(noun, verb):
	codes = deepcopy(codes_master)
	codes[1] = noun
	codes[2] = verb

	for opcode_position in range(0, len(codes)-1, 4):

		if codes[opcode_position] == 99:
			return codes[0]
		else:
			input_position_1 = codes[opcode_position+1]
			input_position_2 = codes[opcode_position+2]
			output_position = codes[opcode_position+3]

			if codes[opcode_position] == 1:
				codes[output_position] = codes[input_position_1] + codes[input_position_2]
			elif codes[opcode_position] == 2:
				codes[output_position] = codes[input_position_1] * codes[input_position_2]
			else:
				print("An error has occurred. Opcode: {}. Opcode position: {}. Noun: {}. Verb: {}".format(codes[opcode_position], opcode_position, noun, verb))				return 1


def main_2():
	for noun in range(100):
		for verb in range(100):
			try:
				output = main(noun, verb)
				if output == 19690720 :
					print(100 * noun + verb)
				elif output == 1:
					return 1
			except:
				print("An error has occurred.")	

main_2()	