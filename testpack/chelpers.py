import re
def countuppers(st):
    return len(re.findall(r'[A-Z]',st))

def countlowers(st):
    return len(re.findall(r'[a-z]',st))




