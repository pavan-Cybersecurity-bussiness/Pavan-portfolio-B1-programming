correct_pin = "5896" # choose a random Number
Current_attempts = 0
max_attempts = 3
login_successful = False
while Current_attempts < max_attempts:
 print(f"Attempt {Current_attempts + 1} of {max_attempts}")
 entered_pin = input("Enter your PIN: ")
 if entered_pin == correct_pin:
  print("PIN accepted! Welcome.")
  login_successful = True
  break # Exit the loop if the PIN is correct
 else:
  print("Incorrect PIN.")
  Current_attempts += 1
# the following works if login_successful is false
if not login_successful:
 print("Too many incorrect attempts. Your Account is locked.")
