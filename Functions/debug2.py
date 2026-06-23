def burn_calories(current_total, activity_mins):
    calories_burned = activity_mins * 8.5
    new_total = current_total - calories_burned
    return new_total

def log_meal(base_calories, meal_weight):
    total_calories = base_calories + meal_weight
    return total_calories

def main():
    daily_calories = 2000.0
    log_meal(daily_calories, 450.0)
    print(f"Calories after breakfast: {daily_calories}")
    remaining_calories = burn_calories(daily_calories, 30)
    print(f"Remaining calories after workout: {remaining_calories}")
    
main()