import matplotlib
import matplotlib.pyplot as plt
import math

# Cofigure matplotlib to write PNG files
matplotlib.use('Agg')

# Get some x-values
xAxis = list(range(0,64))

#Make every number in xAxis a tenth of its size
xTenth = []
for x in xAxis:
  xTenth.append(x*0.1)
xAxis = xTenth

# Write a function to build our y-values
def parabola(xValues):
  # create an empty list to store results
  yValues = []
  # get each number in the given list of x-values
  for x in xValues:
    # compute the square of each value
    #y = x*x
    y = math.sin(x)
    # add the squared value to the list of results
    yValues.append(y)
  # give the resultant list of squared valuse to the caller of this function 
  return yValues

# Get some y-values (by calling our new function)
yAxis = parabola(xAxis)

# We don't have to use all the data we create. We 
# can "slice" out protions that we want.
sliceXAxis  = xAxis[:]
sliceYAxis  = yAxis[:]

# Plot data points as a red circle.
style = 'b-'

# Give matplotlib our data
plt.plot(sliceXAxis , sliceYAxis , style)

# Specify the region of the plot we wish to display
plt.axis([0, 6.4, -1, 1])

# Save our plot to the local disk drive
filename = 'graph.png'
plt.savefig(filename)