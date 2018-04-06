
import re

# def get_star_systems("event":"FSDJump") -> string:
def get_star_systems(content:"event":"FSDJump") -> string:
	pattern = starsystems.compile("\"StarSystems visited\":(\d+\.\d+)")
	result = pattern.findall(content)
	stars = 0
	if result:
		for s in result:
			stars+=string(s)
return stars
