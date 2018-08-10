sentence = "Love"  #欲輸入字串
allChar = [] #創建接受愛心的空矩陣
for y in range(12, -12, -1): #印列數，共24列
    lst_con = ''
    for x in range(-30, 30):
        formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
        if formula <= 0:
            lst_con += sentence[(x) % len(sentence)]        
        else:
            lst_con += ' '
        print(formula)
    allChar.append(lst_con)
print(allChar)  #list_con堆疊到allchar
print('\n'.join(allChar))



