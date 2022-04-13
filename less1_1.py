list = ['333', 1000, [], ()]
list[0] = 333
list[1] = '1000'
list[2].insert(0,2**8)
list[3] = ((2**10 % 2 == 0),)
print(list)