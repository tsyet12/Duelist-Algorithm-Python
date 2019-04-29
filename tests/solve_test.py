from solver.Duelist_Algorithm import DuelistAlgorithm
def f(x):
	return x*0.5
x=["x1"]
xmin=[-2]
xmax=[10]
DA=DuelistAlgorithm(f,x,xmin,xmax,max_gen=100)
DA.solve()

print("test sucessful")