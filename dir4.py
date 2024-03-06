import codecs

f = codecs.open(r'/Users/kasymhan2005/Documents/PP2/row.txt', 'r')
cnt = 0
for x in f:
    cnt += 1

print(cnt)