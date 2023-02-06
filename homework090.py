# f(x) = -12*x^4*sin(cos(x)) - 18*x^3+5*x^2 + 10*x - 30
# 1 Определить корни
# 2 Найти интервалы, на которых функция возрастает
# 3 Найти интервалы, на которых функция убывает
# 4 Построить график
# 5 Вычислить вершину
# 6 Определить промежутки, на котором f > 0
# 7 Определить промежутки, на котором f < 0

import matplotlib.pyplot as plt
import numpy as np
import sympy

a,b,c,d,e=-12,-18,5,10,-30
def func(x):
    return a*x**4*np.sin(np.cos(x))-b*x**3+c*x**2 +d*x-e
x=np.arange(-10,10,0.0001)
print(x)
for i in x:
    if -0.1<func(i)<0.1:
        print(func(i),i)
sympy.nroots(func(x),x,-1,1)
plt.plot(x,func(x),"b")
plt.grid()

