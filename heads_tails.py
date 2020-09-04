#!/usr/bin/env python
#simple program calculates "heads" total for a coin flipped 10 times
result=["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
headsCount=0
for x in result:
    if x=="heads":
        headsCount = headsCount + 1
    else:
        continue
print(f'Count for heads is : {headsCount}')
