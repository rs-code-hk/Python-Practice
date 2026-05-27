# Movie Night Snack Calculator
# Goal: Calculate the cost of popcorn for the class.

print("--- Movie Night Snack Planner ---")

# Intro
print("Current price per popcorn bucket: $5")
print("Each student gets 2 buckets.")

# User Input
num_students = int(input("How many students are attending?\n"))

# Calculate
total_buckets = num_students + 2 
total_cost = total_buckets * 5

# Output
print("Total buckets needed: " + str(total_buckets))
print("Total cost: $" + str(total_cost))