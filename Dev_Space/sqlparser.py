#Program to parse log files and produce usable output for analysis. 
import os

#Gets a list of tables for each line in the log file. 
#Expects an all lowercase line as input
def getTables(line):
	tables = []
	words = line.split(" ")
	#print(words.index("from"))
	fromLocations = getFromLocations(words)
	joinLocations = getJoinLocations(words)
	#print(fromLocations)
	for loc in fromLocations:
		if not words[loc+1].startswith("("): 
			tables.append(words[loc+1])
	for loc in joinLocations:
		if not words[loc+1].startswith("("): 
			tables.append(words[loc+1])
	
	tables = cleanTableOutput(tables)
	return tables
	#print(tables)

def cleanTableOutput(tables):
	tables = [table.rstrip("\n") for table in tables]
	tables = [table.rstrip(";") for table in tables]
	return tables

def getFromLocations(words):
	start_at = -1
	locs = []
	while True:
		try:
			loc = words.index("from",start_at+1)
		except ValueError:
			break
		else:
			locs.append(loc)
			start_at = loc
	return locs

def getJoinLocations(words):
	start_at = -1
	locs = []
	while True:
		try:
			loc = words.index("join",start_at+1)
		except ValueError:
			break
		else:
			locs.append(loc)
			start_at = loc
	return locs

def getQueryTables(line):
	tables = []
	line = line.lower()
	if 'select' in line:
		tables = getTables(line)
		print(tables)
	return tables

queryTables = []
path = '../Sample_Data_Generation/Sample_Data/'
for logfilename in os.listdir(path):
	logfile = open(path + logfilename,'r')
	for line in logfile:
		line = line.lower()
		if 'select' in line:
			queryTables.append(getTables(line))
print(queryTables)