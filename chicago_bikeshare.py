
# coding: utf-8
# Co-Author, Kelvin Maués
# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
data_list_len = len(data_list)
print(data_list_len)

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

# Let's change the data_list to remove the header from it.
header_list = data_list[0]
data_list = data_list[1:]

for row in range(0, 20):
    print(row + 1, data_list[row])
# This prints the index and row

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")
gender_col_index = header_list.index('Gender')
for line in data_list[:20]:
    print(line[gender_col_index])

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order


def column_to_list(data, index):
    """
    Transfor a column from a CSV into a list.
    Args:
        data: the dataset.
        index: the index column to tranform
    Returns:
        Returns a list of the choosen column
    """
    column_list = []
    for row in data:
        column_list.append(row[index])
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    return column_list


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)
            ) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)
           ) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(
    data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0

# Using Generator Expression
genders = [row[gender_col_index] for row in data_list]

# A loop to count the genders by incrementing
# the variables 'male' and 'female'
for gender in genders:
    if gender == 'Male':
        male += 1
    if gender == 'Female':
        female += 1

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)


def count_gender(data_list):
    """
    Counts the number of a gender in a list.
    Args:
        data_list: a list.
    Returns:
        Returns a list with the male and female appearance counted
    """
    genders_list = [row[gender_col_index] for row in data_list]
    in_male, in_female = 0, 0
    for gender in genders_list:
        if gender == 'Male':
            in_male += 1
        if gender == 'Female':
            in_female += 1
    return [in_male, in_female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)
            ) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(
    data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.


def most_popular_gender(data_list):
    """
    Verifies the most popular gender in a list.
    Args:
        data_list: a list.
    Returns:
        Returns a string with the most popular gender
    """
    answer = ""
    in_male, in_female = count_gender(data_list)
    if in_male > in_female:
        answer = "Male"
    elif in_male < in_female:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)
            ) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(
    data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.

def count_user_types(user_list):
    """
    Counts the number of users in a list.
    Args:
        user_list: a list.
    Returns:
        Returns a list with the two types of users, 'Subscriber' and 'Customer'
    """
    subscriber, customer = 0, 0
    for user_type in user_list:
        if user_type == 'Subscriber':
            subscriber += 1
        if user_type == 'Customer':
            customer += 1
    return [subscriber, customer]

print("\nTASK 7: Check the chart!")
users_list = column_to_list(data_list, -3)
user_types = ['Subscriber', 'Customer']
subscriber, customer = count_user_types(users_list)
quantity = [subscriber, customer]
print(quantity)
y_pos = list(range(len(user_types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User')
plt.xticks(y_pos, user_types)
plt.title('Quantity by User')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
diff_gender = [row[gender_col_index] for row in data_list].count("")
answer = "If the total amount of genders are not qual to the length it is because some values in the gender column are null or undefined. And this difference is: {}".format(str(diff_gender))
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().

# Function to sort a list of numbers


def sort_list(arr=[]):
    """
    Sort a list.
    Args:
        arr: a list.
    Returns:
        Returns a list ordered
    """
    print("Sorting the list. It can take some time... e,e ")
    # repeating loop len(a)(number of elements) number of times
    for index in range(len(arr)):
        # initially swapped is false
        swap = False
        i = 0
        while i < len(arr) - 1:
            # comparing the adjacent elements
            if arr[i] > arr[i+1]:
                # swapping
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # Changing the value of swapped
                swap = True
            i = i + 1
        # if swapped is false then the list is sorted
        # we can stop the loop
        if swap == False:
            break
    print("The sorted list is: ", arr)
    return arr

# Function to calculate the median of a list


def calculate_median(arr=[], sorted_list=[]):
    """
    Calculate the median of a list.
    Args:
        arr: a list.
        sorted_list: an ordered list.
    Returns:
        Returns median value
    """
    length = len(arr)
    # Empty list
    if length < 1:
        return None
    # length of the list is odd
    if length % 2 == 1:
        return sorted_list[length//2]
    # lengh of the list is even
    else:
        return sum(sorted_list[length//2-1:length//2+1])/2.0


trip_duration_list = column_to_list(data_list, 2)
# Converting the time values from string to int
trip_duration_list = [int(time) for time in trip_duration_list]

min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

def calculate_total_amount(some_list):
    """
    Sum the total amount of all numbers in a list.
    Args:
        some_list: a list.
    Returns:
        Returns the total amount with number type

    """
    amount = 0
    for value in some_list:
        amount += value
    return amount

# new values
sorted_trip_list = sort_list(trip_duration_list)
min_trip = sorted_trip_list[0]
max_trip = sorted_trip_list[-1]
trip_total_duration = calculate_total_amount(trip_duration_list)
mean_trip = int(trip_total_duration/len(trip_duration_list))
median_trip = calculate_median(trip_duration_list, sorted_trip_list)

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip,
      "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
user_types = set(column_to_list(data_list, 3))

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
    Example function with annotations.
    Args:
        param1: The first parameter.
        param2: The second parameter.
    Returns:
        List of X values

    """

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "no"


def count_items(column_list):
    item_types = []
    count_items = []
    return item_types, count_items


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
