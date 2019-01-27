import time


# how much time a function takes to run?
def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end=time.time()
        # func.__name__ function name
        print(func.__name__ + " took " + str((end - start) * 1000) + " mil sec")
        return result
    return wrapper


# decorator
@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result


# decorator
@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result


array = range(1, 100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
print (out_square[300])
print (out_cube[95293])