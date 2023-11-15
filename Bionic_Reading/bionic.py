def make_text_bold(text):
	return f"**{text}**"

input_file_name = "input.txt"
output_file_name = "output.txt"

with open(input_file_name, "r", encoding= 'utf-8', errors= 'ignore') as input_file, open(output_file_name, "w") as output_file:
	for line in input_file:
		words = line.split()
		bold_line = []

		for word in words:
			if len(word) == 1:
				pass   
			if len(word) <= 3:
				
				bold_word = make_text_bold(word[:1]) + word[1:]
				bold_line.append(bold_word)

			elif len(word) <= 5:
				bold_word = make_text_bold(word[:2]) + word[2:]
				bold_line.append(bold_word)

			elif len(word) == 6:
				bold_word = make_text_bold(word[:3]) + word[3:]
				bold_line.append(bold_word)
				
			elif len(word) >= 7:
				bold_word = make_text_bold(word[:4]) + word[4:]
				bold_line.append(bold_word)
			else:
				bold_line.append(word)

		output_file.write(" ".join(bold_line) + "\n")

print("Text processing complete. Bold text saved in", output_file_name)
