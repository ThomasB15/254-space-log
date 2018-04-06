
import re

def get_star_systems("event":"FSDJump") -> string:
	pattern = re.compile("\"Star Systems visited\":(\d+\.\d+)")
	result = pattern.findall(content)
	stars = 0
	if result:
		for s in result:
			star+=string(s)
return star
