from __future__ import print_function

def wrapper1(a=3):
    return(lambda f: f(a)) 

# def wrapper2(a=5):
#     f = lambda x: 
#     return()

@wrapper1(5)
def mytestfunc(x):
    return(5*x)


# print(wrapper1(5)(mytestfunc))
print(mytestfunc)
print(wrapper1(a=5)(lambda x: 5*x))
# print((lambda x: x**5)(wrapper1(a=5)))
# print((lambda x: x ** 2)(wrapper1(7)))
wrapper1()(lambda x: print(x))
# print(mytestfunc)

######################################################
######################################################
######################################################
######################################################
######################################################
######################################################


def mytestfunc(x):
    return(5*x)

print(wrapper1(5)(mytestfunc))

###############
# equivalent to
###############

@wrapper1(5)
def mytestfunc(x):
    return(5*x)

print(mytestfunc)


