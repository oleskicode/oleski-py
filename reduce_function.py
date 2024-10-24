# reduce(function, iterable) = apply a function to an iterable and reduce it to a single cumulative value.
# performs function on first two elements and repeats process until 1 value remains
import functools

list1 = ["W", "H", "O", "A"]
word = functools.reduce(lambda x, y: x+y,list1)
print(word)

list2 = [5, 4, 3, 2, 1]
sum = functools.reduce(lambda a,b: a+b, list2)
print(sum)
