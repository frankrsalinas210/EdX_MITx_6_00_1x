bob = 0
s = 'azcbobobegghakl'
i = 0
while i < (len(s)-2):
    if s[i:i+3] == 'bob':
        bob += 1
    i += 1
print ("The Number of times bob occures is:", bob)