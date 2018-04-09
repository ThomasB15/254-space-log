#!/usr/bin/env python3
#
# Use like `./space_log.py elite.log -s|-p|-t|-d|-f 

from sys import argv
import fuel
import LightYears
import starsystems
import planets
import terraformable

master
# Opens the log file and grabs the contents.
try:
	fh = open(argv[1], 'r')
	content = fh.read()
	fh.close()
except IndexError:
	exit("Missing name of log file.")
except:
	exit("Couldn't open file \""+argv[1]+"\".")

# Uncomment, and add your work in the appropriate spots.
argSwitcher = {

	'-d': LightYears.get_total_light_years,
	'-f': fuel.get_total_fuel,
	'-s': starsystems.get_star_systems,  # NAMES OF STAR SYSTEMS VISITED
	'-p': planets.names_of_planets,
 	'-t': terraformable.get_terraformable_planets,

 
}

try:
	func = argSwitcher.get(argv[2], lambda x: "Incorrect search argument.")
except IndexError:
	exit("Missing search argument.")

output = func(content)
if type(output) is list:
	for l in output:
		print(l)
else:
	print(output)
