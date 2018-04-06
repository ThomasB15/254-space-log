
import starsystems

def get_star_systems("event":"FSDJump") -> string:
	pattern = starsystems.compile("\"StarSystems visited\":(\d+\.\d+)")
	result = pattern.findall(content)
	stars = 0
	if result:
		for s in result:
			stars+=string(s)
return stars
