import numpy as npy


#NUMPY PRACTICEEEEEEEEEEEEEE



#AXES 
# common parameter is the axes

# axis = 1   <----- horizontal
# axis = 0   <----- vertical
# horizontal = 1 , vertical = 0


#----------

a = npy.array([1,2,3], dtype = 'int8') # int8 = 8 byte int aka 1 bit integer
b = npy.array([[1,2,3.4,3,2,3.23], [4.3,4.4,2,3,2,3],[2.4,2.32,3,4.4,3.3,4.4]]) 


#DESCRIBING THE DATA

print(a)
print("\tarray a has dimensions: ", a.ndim)
print("\tarray a datatype: ", a.dtype, '\n')

# 2 d array 



print(b)
print("\tdimensions: ", b.ndim)   #ndimension
print("\t(rows, columns): ", b.shape) #shape
print("\tdatatype: ", b.dtype, "\n\titem size: ", b.itemsize, "\n\t# of elements: ", b.size) #type, item size, total #
print("\tnumber of bytes total: ", b.nbytes)






#ACCESS, CHANGE SPECIFIC ELEMENTS, ROWS, COLUMNS, ETC
a = npy.array([1,2,3], dtype = 'int8') # int8 = 8 byte int aka 1 bit integer
b = npy.array([[1,2,3.4,3,2,3.23], [4.3,4.4,2,3,2,3],[2.4,2.32,3,4.4,3.3,4.4]]) 

#GET SPECIFIC ELEMENT : [row, column]

print('\telement in row 2, column 3 is: ', b[1,2]) # get element in row 2, column 3 (2)
print('\telement in row 2, column 3 is: ', b[1,-4]) # get element in row 2, column 3 (2) backwards
print('row 1: ', b[0, :]) #basic slice syntax similar to lists, gets the whole row
print('column 2: ', b[:, 1]) # gets the whole column


#IMPORTANT!!!!!!!!!!
#advanced stuff -> [startindex:endindex (exclusive):stepsize]


print('every other in middle 4 in row 1: ', b[0, 1:5:2]) #start at index 1 till index 4, iterate 2 indexes

b[1,2] = 32.3213
print('new num in row 2 column 3 is: ', b[1,2])

b[:, 1] = 5 # every element in column
print(b)
b[1,:] +=22 #adds to every element in row
print(b, '\n')

c = npy.array([[[1,2,3], [5,2,5]], [[4,3,5],[9,12,9]]])
print(c)
print(c[0,1,2]) #1st row, 2nd column, 3rd element





#INITIALIZING DIFFERENT TYPES OF ARRAYS


#MAKING EMPTY ZEROS ARRAYS
print(npy.zeros(5))
print(npy.zeros((22,22))) #rows, columns

#all ones
print(npy.ones((5,3), dtype='float64'))

#any other #
full = npy.full((5,3), 54.4)
full[:, 2] += 43

print(full)

#array of random #s

h = npy.random.rand(4,3) # row, column
print(h)   # 0 to 1, floats

h = npy.random.random_sample(b.shape)

h= h.round(2) #rounds each element to 2 places
print(h)

# random integer

h = npy.random.randint(3,33, size = (3,5)) #random ints 3 to 33
print(h)


#repeat array 

r1= npy.repeat(a,10) # repeats each element in the array 10 times
print(r1)
r1= npy.repeat([a],10, axis = 0) # converts array into 2d array n repeats on the vertical axis rather than horizontal
print(r1)



#BE CAREFUL WHEN COPYING ARRAYS

c = a   # variable c POINTS to the same thing a does , basically a pointer
#DONT DO THIS

#DO THIS
c = a.copy()   # copies the contents

c[0] = 100
print(a,c)


#MATHS TUFF

print((a-3).__abs__()**5) # substracts from all elements, absolute value, power
# adds, divides, multiplies, etc

print(npy.sin(a))

#more math stuff in documentation


#STATSSSS

print(npy.min(h, axis=0))
print(npy.sum(npy.min(h, axis=0)))

#REORGANIZING ARRAYS

before = b.copy()

print(before)

after = before.reshape((18,1))
print(after) #reshapes array to this many columns n rows

print(npy.vstack([b, npy.full(b.shape, 5)])) 
# vertically stacks all the arrays together (as long as same column #)
h2 =npy.hstack([after, npy.random.randint(3,523, size=(18,3))])
print(h2) 
# vertically stacks (as long as same row #)


#OTHER STUFF


#LOAD DATA FROM LIFE
