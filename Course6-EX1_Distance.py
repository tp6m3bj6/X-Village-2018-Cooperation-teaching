p = 1
print('第10天之前剩1公尺')
for i in range(9, 0, -1):
    p = (p+1) * 2
    print('第%s天之前還有%s公尺' % (i, p))
print('一開始兩人相聚%s公尺' % p)
