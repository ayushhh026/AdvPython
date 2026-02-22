import matplotlib.pyplot as plt
categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values = [300, 250, 275, 225]
colors=['red','blue','green','yellow']

plt.pie(values,labels=categories,autopct="%1.1f%%",colors=colors,shadow=True,explode=[0,0,0,0])
plt.title("New college")
plt.show()