import matplotlib.pyplot as plt
categories = ["Grains","Fruits","Vegetables","Protein","Diary","sweets"]
values=[4,3,2,5,3,1]

plt.barh(categories,values)
plt.title("Daily consumption")
plt.xlabel("Foods")
plt.ylabel("Quantity")
plt.show()