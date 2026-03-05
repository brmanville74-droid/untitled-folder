# Variables to test
age = 25
has_student_id = True
is_holiday = False

# 1. Using 'and' with comparison operators
# Must be at least 18 AND have a student ID
if age >= 18 and has_student_id:
    print("Eligible for the Student Discount.")

# 2. Using 'or' with comparison operators
# Eligible if younger than 12 OR older than 65
if age < 12 or age > 65:
    print("Eligible for the Junior/Senior rate.")
else:
    print("Standard ticket rate applies.")

# 3. Using 'not' to reverse logic
# Only proceed if it is NOT a holiday
if not is_holiday:
    print("Regular weekday pricing is active.")

# 4. Combining all three
# Eligible for a special promotion if:
# (Age is between 18 and 30 inclusive) AND (It is not a holiday)
if (age >= 18 and age <= 30) and not is_holiday:
    print("You qualify for the 'Young Adult' weekday special!")
    