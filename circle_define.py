def circle_area(x):
    area = x**2 * 3.14
    return area

def circle_circum(x):
    circum = 2 * x * 3.14
    return circum

a = input('半徑: ')
print('面積: ',circle_area(int(a)))
print('周長: ',circle_circum(int(a)))
