import re

regex = r"(\d*) lbs"

test_str = "300 lbs"

m = re.match(regex, test_str)


print(m.group(1))