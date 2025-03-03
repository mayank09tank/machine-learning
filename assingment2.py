'****************************************************************************************************************************************************************************************************'
'****************************************************************************************************************************************************************************************************'

# 1.	Write a function pascals_triangle(rows) that prints the first rows of Pascal’s Triangle using nested for loops. pascals_triangle(5)   Output: 
#     1 
#    1 1 
#   1 2 1 
#  1 3 3 1 
# 1 4 6 4 1 
def pascals_triangle(rows):
    for i in range(rows):
        num = 1
        print(" " * (rows - i - 1), end="")  # Print leading spaces for formatting
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)  # Calculate next value
        print()  # Move to the next line

pascals_triangle(5)

'**************************************************************************************************************************************************************************************************'

# 2. Explanation of continue Statement
# The continue statement in Python is used inside loops to skip the remaining code in the current iteration and move to the next iteration. It is beneficial in cases where you want to ignore specific values without breaking out of the loop completely.
# Scenarios Where continue is Beneficial:
# Filtering data (e.g., skipping negative numbers when processing a list of numbers).
# Skipping unwanted inputs in user input validation.
# Optimizing performance by avoiding unnecessary computations.
#  Coding Challenge: Print Numbers Divisible by 3

numbers = [10, 15, 22, 33, 40, 45, 50]
for num in numbers:
    if num % 3 != 0:
        continue  # Skip numbers not divisible by 3
    print(num)

'****************************************************************************************************************************************************************************************************'

# 3.	Use list comprehension to generate all Pythagorean triplets (a, b, c) where a² + b² = c² and a, b, c ≤ 50. 
triplets = [(a, b, c) for a in range(1, 51) for b in range(a, 51) for c in range(b, 51) if a**2 + b**2 == c**2]
print(triplets)

'****************************************************************************************************************************************************************************************************'


# 4.	Write a function max_consecutive_sum(nums, k) that finds the maximum sum of k consecutive elements in a list. 
def max_consecutive_sum(nums, k):
    if len(nums) < k:
        return None  # Not enough elements for k-sized window
    max_sum = sum(nums[:k])
    current_sum = max_sum
    for i in range(len(nums) - k):
        current_sum = current_sum - nums[i] + nums[i + k]
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_consecutive_sum([2, 3, 5, 1, 6, 4, 2, 8], 3))  # Output: 14 (6+4+2)

'****************************************************************************************************************************************************************************************************'


'''5.	Write a function that takes a list as an argument and modifies it by appending a new item.
  Demonstrate how changes to the list inside the function affect the list outside the function'''

def modify_list(lst):
    lst.append("New Item")  # Modify the original list

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 'New Item']

'****************************************************************************************************************************************************************************************************'

# 6.	Take a number as input and print the Fibonacci sequence up to that many terms using User-defined functions.  

def fibonacci(n):
    if n <= 0:
        print("Enter a positive integer.")
        return
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

num_terms = int(input("Enter the number of Fibonacci terms: "))
fibonacci(num_terms)
