# The-perceptron-learning-rule
This is a simple implementation of The perceptron learning rule with a simple gui.
using the evaluate with deafault parameters button , program will use the points that were declared at the first of the python file to draw the line that saperates cluster A (red points) from cluster B(Blue points).
using start evaluation button the program will draw the line based on the inputs given.
A and B are vectors dnoted by [x1,x2] notation.
first entry gets the number of data in cluster A.
second entry gets number of data in cluster B.
third entry gets mean of x1 that is the first parameter in our notation and fourth entry gets STD of x1.
using STD , mean and number of data we generate a normal dist. using np.random.normal().
after that we do the same thing again for x2 witch is the second parameter in our notation.
at the end the program draws a line based on the calculated weights.
if the data that we have generated is linearly seprable , points in cluster A will be on one side of the line and points in cluster B will be on the other side ,Otherwise the line is not able to seprate the points . this is the case that our data is non-linearly seprable. fig. 1 and fig.2 represent both cases.
