from matplotlib import pyplot


# QUESTION 3 - KNOWLEDGE CHECK MODULE 9

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
denominator = sum((xi - mean_x) ** 2 for xi in x)

slope = numerator / denominator
intercept = mean_y - (slope * mean_x)

line = [slope * xi + intercept for xi in x]

pyplot.scatter(x, y, color='blue', label='Data Points')
pyplot.plot(x, line, color='red', label='Line of Best Fit')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.title('Simple Linear Regression')
pyplot.legend()
pyplot.show()
