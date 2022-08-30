import re

re.findall(r"\w", "http://www.hackerrank.com/")
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

import re

re.finditer(r"\w", "http://www.hackerrank.com/")
# <callable-iterator object at 0x0266C790>
list(map(lambda x: x.group(), re.finditer(r"\w", "http://www.hackerrank.com/")))
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
