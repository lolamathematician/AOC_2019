with open("input.txt", "r") as f:
	codes = [int(i) for i in f.read().split(",")]

def main():
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
				print("An error has occurred. Opcode: {}. Opcode position: {}".format(codes[output_position], output_position))

print(main())
