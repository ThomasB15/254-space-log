//get number of terraformable planets
import re

def get_total_fuel(content:str) -> float:
	pattern = re.compile("\"TerraformState\":(\S)")
	result = pattern.findall(content)
	count = 0
	if result:
		for r in result:
			if (string(r))
				count++
	return count
