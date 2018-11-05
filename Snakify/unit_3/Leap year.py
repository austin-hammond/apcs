# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)

year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('LEAP')
else:
    print('COMMON')