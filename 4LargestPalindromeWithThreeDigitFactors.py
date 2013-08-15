'''
@author Shyam Ramachandran

Reverse approach. start from 999*999 down to 100*100
check if palindrome
  if so, check if it has 3 digit factors


Runtime calculation:

shyam@shyam-Inspiron-N5110:~/github/projectEuler$ time python 4LargestPalindrome.py 
Result 906609 Product of  913   993

real	0m0.382s
user	0m0.370s
sys	0m0.000s


'''

i=(999*999)
lower = (100*100)
while i >= lower:
  # get palindrom slices
  s = str(i)
  l = len(s)
  mid = l/2
  left = str()
  right = str()
  if (l&1) == 0: # even
    left = s[:mid]
    right = s[mid:l]
  else:
    left = s[:mid]
    right = s[mid+1:l]
  rightflip = right[::-1]

  it1=999
  q = 0
  # check if palindrome
  if left == rightflip:
    # check if it has 3 digit factors
    while it1 >= 100:
      q = int(s) / it1
      if (q*it1) == int(s):
        break
      it1 = it1-1
  if (q*it1) == int(s) and len(str(q)) == 3:
    print 'Result', s, 'Product of ',q,' ',it1
    break
  i = i-1
