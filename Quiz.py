
def Square1(x):
    return SquareHelper(abs(x), abs(x))
    
    
def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
    
Square1(-5)
    

##  Problem 4 , quadratic calculation
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''

    return (a*x*x+b*x+c)

evalQuadratic(1, 2, 1, 5)


def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
 
    print (evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2))

twoQuadratics(4.61, -7.36, 3.79, 7.78, 5.46, -1.71, -6.79, 5.77)



## Problem 5
## return a list of prime numbers between 2 and N inclusive

def primesList(N): 
    '''
    N: an integer
    '''
    plist = [2]    
    for i in range(3,N+1,2):
        cnt = 0
        upper = int(i**0.5)+1
        for j in range(2,upper):
            if i%j==0:
                cnt+=1
        if cnt==0:
            plist.append(i)
    return plist
        
        
primesList(19)
 
       
                                  
## Problem 6
## Write a recursive Python function, given a non-negative integer N, 
## to count and return the number of occurrences of the digit 7 in N.
## for example : count7(717) -> 2; count7(1237123) -> 1; count7(8989) -> 0

def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    
    if N<10:
        if N==7:
            return 1
        else:
            return 0
           
    elif N%10==7:
        return 1+count7(int(N/10))
    else:
        return 0+count7(int(N/10))
        
## Problem 7
## Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). 
## The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)
## This function takes in a dictionary and returns a list.


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    unikeys = []
    univals = []
    valdic = {}
    for v in aDict.values():
        valdic[v] = valdic.get(v,0)+1 ## return a dictionary with aDict.values as key, cnt of aDict.values as value
    valis = valdic.values() ## obtain the values of valdic to see which aDict.values has only 1 cnt
    if 1 not in valis:
        return []
    else:
        for ind in range(0,len(valis)): ## locate the index of valdic.values ==1
            if valis[ind]==1:
                univals.append(valdic.keys()[ind]) ## Use the index to find the valdic.keys, aka, unique aDict.values
        for k in aDict.keys(): 
            if aDict[k] in univals: ## if aDict[k] values are within the list of univals, we would like to return the key
                unikeys.append(k)
    unikeys.sort() ## sort the key ascending order
    return unikeys
    
    
## Problem 8
## Write a Python function called satisfiesF that has the specification below. 
## Then make the function call run_satisfiesF(L, satisfiesF). 
## For example 

'''
def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print satisfiesF(L)
print L

should print out 

2
['a', 'a']
'''

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    Lcopy = L[:]
    for s in Lcopy:
        if f(s) == False:
            L.remove(s)
    return len(L)
    
run_satisfiesF(L, satisfiesF)


