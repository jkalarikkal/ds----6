import matplotlib.pyplot as mop
import pandas as pan
data = pan.read_csv("titanic.csv")
gender = data ['Sex'].value_counts()
print(gender)

x = gender.index
y = gender.values

mop.bar(x, y, color = ['blue', 'pink'])
mop.title("Titanic bar")
mop.show()



