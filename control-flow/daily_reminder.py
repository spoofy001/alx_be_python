# daily_reminder.py

def process_task(task, priority, time_bound):
    message = match priority.lower():
        case 'high':
            f"'{task}' is a high priority task"
        case 'medium':
            f"'{task}' is a medium priority task"
        case 'low':
            f"'{task}' is a low priority task"
        case _:
            f"'{task}' has an unrecognized priority"

    if time_bound.lower() == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."
    
    return message

# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task and get the customized reminder
reminder = process_task(task, priority, time_bound)

# Print the customized reminder
print("Reminder:", reminder)
