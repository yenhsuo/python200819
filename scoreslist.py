scores = []
maxsc = 0
minsc = 100
total = 0
maxna = ""
minna = ''
for i in range(5):
    na = input('名子: ')
    n = int(input('分數: '))
    scores.append(n)
    if n > maxsc:
        maxsc = n
        maxna = na
    if n < minsc:
        minsc = n
        minna = na
    total = total + n
print('總分: ',total)
print('最高分: ',maxna,maxsc)
print('平均: ',total/len(scores))
print('最低分: ',minna,minsc)