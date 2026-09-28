numbers=[4,2,4,3,2,4]
counts={}
for number in numbers:
    counts[number]=counts.get(number,0)+1

print (counts)