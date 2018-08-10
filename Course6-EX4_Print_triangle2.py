#EX4.列印等腰三角形(挑戰題)
rows=int(input('number of rows:'))

for i in range(rows):
     for j in range(rows-i):
         print ("   ",end='')
     for k in range(2*i+1):
             print(" * ",end='')
     print('\n')



