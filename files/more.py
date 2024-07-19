def more(text, num_of_lines):
	lines = text.splitlines()
	while lines:
		chunk = lines[:num_of_lines]
		lines = lines[num_of_lines:]
		for line in chunk: print(line)
		if lines and input('More? ') not in ['y', 'Y']: break

if __name__ == '__main__':
    import sys
    more(sys.__doc__, 5)
