
i = 4000000L
first = 1
second = 1
result = 0L

while True:
  if first+second > i:
    break
  temp = first
  first = second
  second = temp + second
  if not (second & 1):
    result += second

print "Result " + str(result)
