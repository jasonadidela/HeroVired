lt1 = [1, 2, [3, 4], 5, [6, 7]]
for i in lt1:
    if isinstance(i, list):
        for j in i:
               print(j)
    else:
         print(i)