import matplotlib.pyplot as plt

x=[2020,2023,2025,2026]
y=[15,44,55,69]
y1=[22,32,46,59]

plt.plot(x,y,marker='o',markersize=10,markerfacecolor='cyan',markeredgecolor='black')
plt.plot(x,y1)
plt.show()