#get number of terraformable planets
import re

def get_terraformable_planets(content:str) -> float:
	pattern = re.compile("\"TerraformState\":(\S)")
	result = pattern.findall(content)
	count = 0
	if result:
		for r in result:
			if string(r):
				count+= 1
	return count
