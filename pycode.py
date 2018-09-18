# Adding first function, adds two numbers together

def addingNumbers(a, b):
    c = a + b
    return c

a = 5
b = 10
c = addingNumbers(a, b)
print("My funtion returns the value", c)


# adding another function that sorts numbers
def sortNumbers(numbers):
    n = len(numbers)
    for i in range(0, n-1):
        m = i
        for j in range(i+1, n):
            if numbers[j] < numbers[m]:
                m = j
        temp = numbers[i]
        numbers[i] = numbers[m]
        numbers[m] = temp
    return numbers


numbers = [6, 5, 4, 3, 10, 90, 44]
print("Unsorted numbers were:", numbers)
sorted_numbers = sortNumbers(numbers)
print("Sorted numbers are:", sorted_numbers)
