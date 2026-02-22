import matplotlib.pyplot as plt

x = [0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8] # Hours studied
y = [55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]
x1 = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8] # Hours studied
y1 = [55, 58, 65, 70, 72, 78, 83, 88, 90, 95, 97]

plt.scatter(x,y,color="red",label='class A')
plt.scatter(x1,y1,color="blue",label='class B')
plt.legend()
plt.show()