s = "abcdef"
res = ""

for i in s:
    res += chr(ord(i) + 2)

s = res