# Mean, Median, and Mode
import statistics

numbers = [3, 4, 2, 5, 5, 6, 3, 5, 2, 5]
numbers.sort()
print(numbers)


# To find the mean, median, mode, lower median, variance, and standard deviation of the given list.
a = statistics.mean(numbers)
print(a)
b = statistics.median(numbers)
print(b)
c =statistics.mode(numbers)
print(c)
d = statistics.median_low(numbers)
print(d)

e = statistics.variance(numbers,a)
print(e)

f = statistics.stdev(numbers)
print(f)
 


# To find the mean, median, and mode of a list of numbers.