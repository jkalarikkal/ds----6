import matplotlib.pyplot as mop

ages = [22,55,36,45,21,67,45,23,89,11,33,67,88,67,89,12,6,9,48,68,18]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

mop.hist(ages, bins, histtype = "bar", rwidth = 0.8)
mop.xlabel("ages")
mop.ylabel("frequency")
mop.title("ages of peoples")
mop.show()


x = [1,2,3,4,5,6,7,8,9,10]
y = [0,1,0,1,0,1,0,1,0,1]

mop.scatter(x,y, label = "Scatter plot", color = 'red', marker = '^', s = 40)
mop.xlabel("all num")
mop.ylabel("yay to nay")
mop.title(" numbers.")
mop.show()


activities = ["calling", "gaming", "going out", "locked in", "gym", "slepp"]
hours  = [3, 3, 5, 4, 2, 7]
colour = ['c', 'b', 'r', 'y', 'g', 'm']
mop.pie(hours, labels = activities, colors = colour, startangle = 90, shadow = True)
mop.title("Day Pie")
mop.show()


days  = [1,2,3,4,5,6,7]
eating = [0.5,7,2,0.2,3,4, 11]
gaming = [4,1,6,2,9,1,0.5]
sleeping = [4,9,12,3,8,11,7]
chilling = [16, 9, 4, 17, 4, 8, 1]

mop.plot([],[], color = 'm', label = "eating", linewidth = 4)
mop.plot([],[], color = 'r', label = "gaming", linewidth = 4)
mop.plot([],[], color = 'y', label = "sleeping", linewidth = 4)
mop.plot([],[], color = 'g', label = "chilling", linewidth = 4)

mop.stackplot(days, eating, gaming, sleeping, chilling, colors = ['m', 'r', 'y', 'g'])
mop.xlabel("days")
mop.ylabel("hours")
mop.title("day plot")
mop.legend()
mop.show()