rows=int(input('number of rows:'))
#上三角形
tri=[]
for i in range(rows):
    tri.append('*'*(i+1))
# print(tri)

#下三角形
for i in range(rows):
    tri.append('*'*(rows-i))
print(tri)
print('\n'.join(tri))