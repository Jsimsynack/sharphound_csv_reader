#!/usr/bin/python3

import csv,sys,os

# Getting files in local directory
directory = os.listdir()

# Header - Version Warning
print('\n' + '[+] Make sure that you are running Python3.x.x')
print('[+] This function only takes *.csv files')

# Checks to see whether there is an argument called with this function
def check_file():
	global args
	global arguments
	global arg1
	args = sys.argv
	arguments = args[1:]
  
	if len(arguments) < 1:
    print('Error: No argument provided')
		print('Usage: python reader.py <file.csv>')
		sys.exit(1)
    
	else:
		
		# Get the command line arguments
		args = sys.argv
		# The first argument is the name of the script itself
		# so we will skip it
		arguments = args[1:]
		# Setting the first argument to a variable
		arg1 = arguments[0]

# Checking to see if *.csv file exists within our local directory
def file_exists(file):
  
	if file in directory:
		pass
  
	else:
		print(f"Error: the file {file} does not exist in this directory")
		sys.exit(1)

# Accessing values from arg1
def running(file):
	print(f'[+] Accessing values from {arg1}' + '\n')
  
	with open(file,'r') as header:
		line1 = header.readline()
		print(f'[+] Header row for {arg1}:' + '\n')
		print(line1 + '\n')
    
	with open(file, newline='') as domain_csv:
		domain_csv = csv.DictReader(domain_csv, delimiter='\n')
		print(f'[+] Values for {arg1}:' + '\n')
		for row in domain_csv:
			for key,value in row.items():
				print(value)
        
	sys.exit(1)

# Running functions 
check_file()
file_exists(arg1)
running(arg1)
