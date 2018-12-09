from matplotlib import pyplot

#1. Prepare data:
machine_details = [4, 5, 2]

#2. Prepare labels:
machine_names = ["male", "female", "nope"]

#3. Draw pie chart:
pyplot.pie(machine_details, labels = machine_names, autopct = "%.1f%%", shadow = True, explode = [0, 0.1, 0])
pyplot.axis("equal")
pyplot.title("Sex in the class")
#4. Show:
pyplot.show()