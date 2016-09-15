import math
#ein kleiner Kommentar
a=0
b=1

for i in range(200):

  print (a+b)*a-b**2
  a,b=b,a+b
