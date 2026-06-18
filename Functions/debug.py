security_status = "LOCKED"
alarm_sound = "SIREN"
def trigger_alarm():
    print(f"Alert! Sounding the {alarm_sound}")
def check_system():
    print("Checking home network stability...")
    if security_status == "LOCKED":
        print("All doors are secured.")
    else:
        trigger_alarm()


# PSEUDOCODE - Change the following pseudocode into code
# DEFINE a new function called reset_system
# INSIDE the function, print "System rebooting..."
def reset_system():
    print("System Rebooting")

def main():
    print(f"The current alarm sound is: {alarm_sound}")
    check_system()
    reset_system()
