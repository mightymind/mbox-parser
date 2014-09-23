#! /usr/bin/python3
import sys

#print(sys.argv[0])

#res=input('Input str\n')
#print(res)

emails={}
#f_mbox=open('mbox.txt', 'r')
#f_mbox=sys.stdin.read()
f_mbox=sys.__stdin__
for line in f_mbox:
    if line[:6]=='From: ':
        from_str=line.strip().split(' ')
        em=from_str[-1][1:-1].lower()
        if em in emails:
            emails[em]=emails[em]+1
        else:
            emails[em]=1
#f_mbox.close()



alias={}
if '-a' in sys.argv:
    f_alias=open(sys.argv[sys.argv.index('-a')+1], 'r')
    for line in f_alias:
        words=line.strip().split(' ')
        for word in words:
            alias[word]=words[0]
    f_alias.close()



result={}
for key, value in emails.items():
    if key in alias:
        if alias[key] in result:
            result[alias[key]]=result[alias[key]]+value
        else:
            result[alias[key]]=value
    else:
        if key in result:
            result[key]=result[key]+value
        else:
            result[key]=value


b = list(result.items())
b.sort(key=lambda item: item[1])
for item in b:
    print(item[0]+': '+str(item[1]))


#input('Press any key to exit')

