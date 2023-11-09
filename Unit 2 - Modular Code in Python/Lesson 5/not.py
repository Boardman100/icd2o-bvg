def not_string(s):
    if s[0:3] != 'not':
        s = 'not'+s
    return s
print(not_string('hello'))