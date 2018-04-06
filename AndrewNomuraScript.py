# Andrew Nomura

import re

def get_star_systems("event":"FSDJump"):
	pattern = re.compile("\"Star Systems visited\"")
	result = pattern.findall(content)
	stars = 0

	return result
