#! /usr/bin/python
import sys

emails = {}
alias = {}
result = {}
f_mbox = sys.__stdin__
xf_mbox = []

for line in f_mbox:
    xf_mbox.append(line)

for i in range(len(xf_mbox) - 1):
    if xf_mbox[i].startswith("From:"):
        from_str = xf_mbox[i].strip().split(' ')
        if len(from_str) > 1:
            em = from_str[-1][1:-1].lower()
            if em in emails:
                emails[em] = emails[em] + 1
            else:
                emails[em] = 1
        else:
            from_str = xf_mbox[i + 1].strip().split(' ')
            em = from_str[-1][1:-1].lower()
            if em in emails:
                emails[em] = emails[em] + 1
            else:
                emails[em] = 1

if '-a' in sys.argv:
    f_alias = open(sys.argv[sys.argv.index('-a') + 1], 'r')
    for line in f_alias:
        words = line.strip().split(' ')
        for word in words:
            alias[word] = words[0]
    f_alias.close()

for key, value in emails.items():
    if key in alias:
        if alias[key] in result:
            result[alias[key]] = result[alias[key]] + value
        else:
            result[alias[key]] = value
    else:
        if key in result:
            result[key] = result[key] + value
        else:
            result[key] = value

b = list(result.items())
b.sort(key = lambda item: item[1])
for item in b:
    print(item[0] + ': ' + str(item[1]))
