checked_user = []
login_attempts = [
("alice", "success"),
("bob", "failed"),
("bob", "failed"),
("charlie", "success"),
("bob", "failed"),
("alice", "failed")]

for attempt in login_attempts:
    name = attempt[0]

    if name not in checked_user:
        failed_attempts = 0  # Reset counter for this specific person

        # Now we scan the whole list again for THIS name
        for check in login_attempts:
            if check[0] == name and check[1] == "failed":
                failed_attempts += 1


        # After counting, check if they are a threat
        if failed_attempts >= 3:
         print(f"""Checking login attempts...ALERT: User:" {name} "has 3 failed login attemptsSecurity check
complete  and {name} is a threat!""")

        # Make sure we don't check this person again
        checked_user.append(name)