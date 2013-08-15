import sys

s=0
for n in range(999):
  if   ( not((n+1) % 3) or  not((n+1) % 5) ):
    s += (n+1)

print s
