import re

p=re.compile("([\d]+\.){3}\d*\/\d+")
print (p.match('1629.128.141/32'))