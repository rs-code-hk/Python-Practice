# =====================================================================
#  TASK: Change the code below to use cleaner print formatting
# =====================================================================

# User input
username = input("Enter friend's name: ").strip().upper()
messages_count = int(input("Number of unread text messages: "))
is_online = input("Are they online right now? (yes/no): ").strip().lower() == "yes"

# Output current status
status_message = f"[ {username} ] is typing a response..." 
print(status_message)

# Output message log
preview_message = f"You have {messages_count} unread messages waiting from {username}."
print(preview_message)


# Output friend list status
friend_message = f"USER: {username} | ONLINE STATUS: {str(is_online)} | SYNC COMPLETE."
print(friend_message)