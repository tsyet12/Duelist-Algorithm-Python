from solver.Duelist_Algorithm import DuelistAlgorithm

'''
Here we have a simple squared equation that we want to optimize (minimize). 
The equation is y=(x1)^2+(x2)^2
 x1 is bounded from -2 to 10 (-2 is min value of x1 and 10 is max value of x1)
 x2 is bounded from 10 to 15 (10 is min value of x2 and 15 is max value of x2)
'''


'''
First we define the function:
The equation is f=(x1,x2) = y = (x1)^2+(x2)^2
'''
def f(x1,x2):
	return x1*x1+x2*x2

'''
Secondly, we name the optimization variables and tell the solver how many variables to optimize.
We can do this by putting in the names of the variables as strings in an array.
'''
x=["x1","x2"]

'''
The thirds step is to specify the boundary for each variables
     "x1"   "x2"
min   -2	 5
max	  10	 15

This xmin and xmax array follows the position of the array you define at second step.
'''

xmin=[-2,5]
xmax=[10,15]

'''
DA.DuelistAlgorithm(function output=f,
					names of manipulated variables= x, 
					lower limit of manipulated variables= xmin,
					upper limit of manipulated variables = xmax,
					population size=pop (default=200),
					luck factor=luck (default=0.01),
					innovative/mutation factor= mut (default=0.1),
					learning probability= learn (default=0.8),
					maximum generation= max_gen (default=500),
					number of champions per selection=nc (default=5),
					is shuffling required before duel?=shuffle (default=False)
					)

You do not need to fill in variables with default values. They are for fine tuning the algorithm.
'''

#Increase the maximum generation for more precise answer
DA=DuelistAlgorithm(f,x,xmin,xmax,max_gen=1000)
DA.solve()

'''
You should see the answer, it should look something like the following:

Optimized using Duelist Algorithm. Answer is: [1.70085713e-03 5.00016813e+00] with fitness of 25.00168420123805
'''