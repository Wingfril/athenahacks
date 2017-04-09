# Displays dictionary
def display(di):
	for key in di.keys():
		print(key + ": " + str(di[key]))

# Creates dictionary of the form state: {[year, avg temp, production], [year, avg temp, production], ...}
# Example: WA: {[2006, 50, 1000], [2007, 55, 990], ...}
def makeDictionary():
	states_dict = {}
	data = {}
	fullToAbbr = {}
	list_of_states = []
	states = open("../data/Abbreviated states.txt", 'r')
	states2 = open("../data/States full name.txt", 'r')
	for line in states:
		data[line[:-1]] = []
		list_of_states.append(line[:-1])
		fullName = states2.readline()[:-1]
		fullToAbbr[fullName] = line[:-1]
	states.close()
	states2.close()

	for state in list_of_states:
		state_data = open('../data/' + state + '.txt', 'r')
		for line in state_data:
			if "Date" in line:
				break
		for line in state_data:
			data[state].append(line.split(","))
			data[state][-1][0] = data[state][-1][0][:-2]
			data[state][-1][1] = float(data[state][-1][1])
			data[state][-1][2] = 'no data'
			

	i = 0
	while i + 2008 < 2018:
		bee_data = open('../data/' + str(i + 2008) + '.txt', 'r')
		for line in bee_data:
			if ("1,000 Dollars" in line) or ("1,000 dollars" in line):
				bee_data.readline()
				break
		for line in bee_data:
			if "Oth" in line:
				break
			try:
				line_array = line.split()
				abbr = ''
				if line_array[0] in fullToAbbr.keys():
					abbr = fullToAbbr[line_array[0]]
				elif (line_array[0] + ' ' + line_array[1]) in fullToAbbr.keys():
					abbr = fullToAbbr[line_array[0]+ ' ' + line_array[1]]
					line_array.remove(line_array[1])
				elif line_array[0] in fullToAbbr.values():
					abbr = line_array[0] 
				else:
					continue
				data[abbr][i][2] = float(line_array[4].replace(',', ''))
			except:
				continue
		i += 1
		bee_data.close()
	display(data)
	return data

if __name__ == '__main__': makeDictionary()
