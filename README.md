# Duelist-Algorithm-Python [![Build Status](https://travis-ci.com/tsyet12/Duelist-Algorithm-Python.svg?branch=master)](https://travis-ci.com/tsyet12/Duelist-Algorithm-Python)
A Python implementation of the paper : 
Duelist Algorithm: An Algorithm Inspired by How Duelist Improve Their Capabilities in a Duel (2015) <b>
Totok Ruki Biyanto, Henokh Yernias Fibrianto, Gunawan Nugroho, Erny Listijorini, Titik Budiati, Hairul Huda <b>
https://arxiv.org/abs/1512.00708

I would like to clarify that various figures of this README.md document is taken from the original artical as shown above.


# Theory (From Biyanto et al., 2015)
Duelist Algorithm is a metaheuristic for mathematical optimization problems. Metaheuristic are a higher-level procedure or heuristic designed to find, generate, or select a heuristic (partial search algorithm) that may provide a sufficiently good solution to an optimization problem, especially with incomplete or imperfect information or limited computation capacity. Examples for metaheuristics include genetic algorithm, particle swarm optimization, etc. Many of these metaheuristics rely on population-based search, which utilizes many "searchers" (also refered to as "particles" or "swarms") to simultaneously search the solution space.

The procedure of Duelist Algorithm is shown in the figure below (see Fig 1). Quoting from the authors:
>The Duelist Algorithm starts with an initial set of duelists. The duel is to determine the winner and loser. The loser learns from the winner, while the winner try their new skill or technique that may improve their fighting capabilities. A few duelists with highest fighting capabilities are called as champion. The champion train a new duelists such as their capabilities. The new duelist will join the tournament as a representative of each champion. All duelist are re-evaluated, and the duelists with worst fighting capabilities is eliminated to maintain the amount of duelists. 

![flowchart](images/flowchart.PNG) <b>
  
*Fig 1. Flowchart of Duelist Algorithm*

In the Duelist Algorithm, the best solutions in a population are chosen as the champions, while worst solutions are eliminated (see Fig 2). Winner mutates themselves and attempts to improve, while losers learns from winner (has a chance to copy traits of winner).

![champion selection and elimination](images/cham.PNG) <b>
  
*Fig 2. Champion selection and worst elimination*

In the original paper, Duelist Algorithm was shown to out-perform a few state-of-art metaheuristic algorithm for some specific tasks (see Fig 3). Therefore, it is very interesting.

![performance](images/performance.PNG) <b>
  
*Fig 3. Performance of Duelist Algorithm from original paper*

# Dependencies
This algorithm is fully implemented in Python. It is recommended to use Python 3.X. Library dependencies: <b>
- numpy 1.15.4
```
$ pip install numpy
```

<b>

# How to Use
First download the git repository. You can do this by clicking the download button or using the git command:
```
$ git pull https://github.com/tsyet12/Duelist-Algorithm-Python
```
<b>
  
Move to the directory:
  
```
$ cd (directory of Duelist-Algorithm-Python)
```

Run setup. The following command installs all files in directory:

```
$ pip install -e .
```

Move to examples and run the examples

```
$ cd examples
```

# Short Tutorial

**There are four simple steps to run an optimization problem using Duelist Algorithm**

(Example 2 from example folder)

** Prerequisites **

```
from solver.Duelist_Algorithm import DuelistAlgorithm
```

** 1. Define your function. Say you want to minimize the equation f=(x1,x2) = (x1)^2+(x2)^2 **

```
def f(x1,x2):
	return x1*x1+x2*x2
```

** 2. Define the variables that can be *manipulated* for optimization. Define their names as string and put them in an array. **

```
x=["x1","x2"]
```

** 3. Define the boundaries for the manipulated variables:**

 Say:

 x1 is bounded from -2 to 10 (-2 is min value of x1 and 10 is max value of x1)

 x2 is bounded from 10 to 15 (10 is min value of x2 and 15 is max value of x2)

 We can arrange this in a table that can be easily read:

 Variables  |  "x1"  | "x2"    |

 Min. bound |  -2    |  5      |

 Max. bound |  10    |  15     |


```
> xmin=[-2,5]
> xmax=[10,15]
```

> 4. Setup the solver and start the solve procedure.

```
DA=DuelistAlgorithm(f,x,xmin,xmax,max_gen=1000)
DA.solve()
```

# Version

Currently Version 1.0

# To-do
- [X] Setup algorithm and show optimized solution

- [X] Create Tutorials

- [X] Update ReadMe

- [ ] Add plot functions

- [ ] Add a modified feature for faster convergence

- [ ] Add result loging
