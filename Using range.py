#Range
my_range = range(10)
my_range
Output = range(0, 10)
list(my_range)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Full way to creating a range
list(range(1, 14, 2))
Output = [1, 3, 5, 7, 9, 11, 13]

#Creating a 'while' and 'for' loop with ranges
count = 1
while count <= 4:
    print("looping")
    count += 1
 
looping
looping
looping
looping

for _ in range(4):
    print("looping")
 
looping
looping
looping
looping