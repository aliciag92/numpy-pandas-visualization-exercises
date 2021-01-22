#Use the following code for the questions below:
    a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
    import numpy as np
#1. How many negative numbers are there?
negative_numbers = len(a[a < 0])

negative_numbers #4

#or (a < 0).sum()
#or negative_numbers = a[a < 0]
#   len(negative_numbers)

#2. How many positive numbers are there?
positive_numbers = (a > 0).sum()

positive_numbers #5

#or positive_numbers = a[a > 0]
#   len(positive_numbers)

#3. How many even positive numbers are there?
pos_and_even_num = (a > 0) & (a % 2 == 0) #OR operation is a pipe '|' character*
print((pos_and_even_num).sum()) #3

#or positive_numbers = a[a > 0]
#   even_positives = positive_numbers[positive_numbers % 2 == 0]
#   len(even_positives)

#4. If you were to add 3 to each data point, how many positive numbers would there be?
add_three = (a + 3) 
print(add_three) #[ 7 13 15 26  1  2  3  3  3 -3  6 -4]

(add_three > 0).sum() #10

#or b = a + 3
#   len(b[b > 0])

#5. If you squared each number, what would the new mean and standard deviation be?
num_squared = (a**2)
print(num_squared) #[ 16 100 144 529   4   1   0   0   0  36   9  49]
                  
num_squared.mean(), num_squared.std() #(74.0, 144.0243035046516)

#or (a**2). mean(), a(**2).std()

#6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.
a - a.mean() #array([  1.,   7.,   9.,  20.,  -5.,  -4.,  -3.,  -3.,  -3.,  -9.,   0., -10.])
#double check:
centering = a - a.mean()
centering.mean() #0.0

#7. Calculate the z-score for each data point. Recall that the z-score is given by:

    # Z = x − μ / σ
(a - a.mean())/a.std() #array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367, -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261, 0.        , -1.24034735])

#8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.
import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)

sum_of_a #55

#numpy version:
#sum_of_a = np.array(a)
#sum_of_a.sum()

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
min_of_a #1

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
max_of_a #10

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a) / len(a)
mean_of_a #5.5

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1

for x in a:
    product_of_a = product_of_a * x

product_of_a #3628800

#another solution
#total = 1
#for n in a:
    #total += n
#total

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [a**2 for a in a]
squares_of_a #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [a for a in a if a % 2 != 0]
odds_in_a #[2, 4, 6, 8, 10]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [a for a in a if a % 2 == 0]
evens_in_a #[2, 4, 6, 8, 10]

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

b = np.array(b)
b.sum() #33

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

b.min() #3

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

b.max() #8

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

b.mean() #5.5

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

b.prod() #20160

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

b**2 #array([[ 9, 16, 25],
        #    [36, 49, 64]])

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

b[b % 2 != 0] #array([3, 5, 7])

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

b[b % 2 == 0] #array([4, 6, 8])

# Exercise 9 - print out the shape of the array b.
b.shape #(2, 3) #2 arrays, #each of the arrays has 3 elements

# Exercise 10 - transpose the array b.
np.transpose(b) #array([[3, 6],
                #       [4, 7],
                #       [5, 8]])

#another way: b.T

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
np.reshape(b, (1, 6)) #or: b.reshape(6)
#syntax: np.reshape(shape, (order you want *1 by 6*))

#another way: b.flatten()

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
np.reshape(b, (6, 1)) #or b.reshape(6,1)
#array([[3],
#       [4],
#       [5],
#       [6],
#       [7],
#       [8]])
## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
c = np.array(c)

# Exercise 1 - Find the min, max, sum, and product of c.
c.min(), c.max(), c.sum(), c.prod() 
#(1, 9, 45, 362880)

# Exercise 2 - Determine the standard deviation of c.
c.std()
#2.581988897471611

# Exercise 3 - Determine the variance of c.
np.var(c) #or c.var()
#6.666666666666667

# Exercise 4 - Print out the shape of the array c
c.shape
#(3, 3)

# Exercise 5 - Transpose c and print out transposed result.
c.T
#array([[1, 4, 7],
#       [2, 5, 8],
#       [3, 6, 9]])

# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c, c)
#array([[ 30,  36,  42],
#       [ 66,  81,  96],
#       [102, 126, 150]])

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
(c * c.T).sum()
#261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
(c * c.T).prod()
#131681894400

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)
#array([[ 0.89399666, -0.98803162,  0.85090352,  0.        ,  0.58061118,
#        -0.80115264],
#       [ 0.85090352, -0.89399666,  0.98803162, -0.17604595,  0.89399666,
#         0.        ],
#       [-0.30481062,  0.85090352, -0.85090352,  0.89399666, -0.85090352,
#        -0.80115264]])

# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)
#array([[-0.44807362,  0.15425145,  0.52532199,  1.        ,  0.81418097,
#        -0.59846007],
#       [ 0.52532199, -0.44807362,  0.15425145,  0.98438195, -0.44807362,
#         1.        ],
#       [-0.95241298,  0.52532199,  0.52532199, -0.44807362,  0.52532199,
#        -0.59846007]])

# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)
#array([[-1.99520041, -6.4053312 ,  1.61977519,  0.        ,  0.71312301,
#         1.33869021],
#       [ 1.61977519,  1.99520041,  6.4053312 , -0.17883906, -1.99520041,
#         0.        ],
#       [ 0.32004039,  1.61977519, -1.61977519, -1.99520041, -1.61977519,
#         1.33869021]])

# Exercise 4 - Find all the negative numbers in d
d = np.array(d)
d[d<0]
#array([-90, -30, -45, -45])

# Exercise 5 - Find all the positive numbers in d
d[d>0]
#array([ 90,  30,  45, 120, 180,  45, 270,  90,  60,  45,  90, 180])

# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)
#array([-90, -45, -30,   0,  30,  45,  60,  90, 120, 180, 270])

# Exercise 7 - Determine how many unique numbers there are in d.
np.unique(d).sum()
#630

# Exercise 8 - Print out the shape of d.
d.shape
#(3, 6)

# Exercise 9 - Transpose and then print out the shape of d.
d.T.shape
#(6, 3)

# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9,2)
#array([[ 90,  30],
#       [ 45,   0],
#       [120, 180],
#       [ 45, -90],
#       [-30, 270],
#       [ 90,   0],
#       [ 60,  45],
#       [-45,  90],
#       [-45, 180]])

#Awesome Bonus For much more practice with numpy, Go to https://github.com/rougier/numpy-100 and click the "Fork" icon in the upper-right of the screen to fork the repo. This makes a copy of the repo onto your own account. Next, clone your fork https://github.com/your-username/numpy-100 down to your machine. Work through, add, commit, and push your solutions to your own repo.