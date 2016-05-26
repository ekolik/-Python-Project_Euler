import re

romans = open("89-input.txt").read()
print(len(romans) - len(re.sub('VIIII|IIII|LXXXX|XXXX|DCCCC|CCCC', '  ', romans)))
