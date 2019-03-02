import os

# print(os.getcwd())
# print(os.listdir(os.getcwd()))

def get_num_leading_white_spaces(line):
	return len(line) - len(line.lstrip(' '))

code_indent = 4

for file in os.listdir(os.getcwd()):
	if file.endswith(".ipynb"):
		print(file)

		## Create new file
		dev_file = open(file, "r")
		new_file = open("../"+file,"w+")

		## Copy appropriate lines  new file
		should_skip = False
		for line in dev_file:
			if '## YOUR CODE HERE' in line:
				# print(line[:-2]) 
				should_skip = True
				new_file.write(line[:-2])  # We don't wan't the ',' at hte end of the line

			if not code_indent == get_num_leading_white_spaces(line):
				should_skip = False

			if not should_skip:
				new_file.write(line)

		## Close file
		new_file.close()
		dev_file.close()


