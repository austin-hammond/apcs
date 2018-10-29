import math

n = int(input())
a = int( math.floor(n/60) )
b = float( ((n/60) % 1)*60 )

print(a, b)