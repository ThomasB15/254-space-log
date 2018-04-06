# THomas Brenner 
import re
def names_of_planets(content:str) -> char:
		pattern = re.compile("\"Bodyname\":(\d+\.\d+)")
		result = patter.findall(content)
		
		return fuel
