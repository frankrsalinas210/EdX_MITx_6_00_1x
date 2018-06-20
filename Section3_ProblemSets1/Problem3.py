s = 'azcbobobegghakl'
string = s[0]
i = 0
while i < len(s):# < (len(s)-2):
    j = len(s)
    while j > i:
        temp = s[i:j]
        if temp == ''.join(sorted(temp)):
            if len(temp) > len(string):
                string = temp
        j -= 1
    s = s[i+1:]
print ("Longest substring in alphabetical order is:", string)