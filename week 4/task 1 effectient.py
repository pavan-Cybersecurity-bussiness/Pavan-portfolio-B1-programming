failed_counts = {} #dictonary is used
login_attempts = [
("alice", "success"),
("bob", "failed"),
("bob", "failed"),
("charlie", "success"),
("bob", "failed"),
("alice", "failed")]

for name, status in login_attempts:
    if status == "failed":
        if name not in failed_counts:
            failed_counts[name] = 1  # First failure found
        else:
            failed_counts[name] += 1

for user in failed_counts :
    score = failed_counts[user]
    if score >2 :
        print(f"""Checking login attempts...ALERT: User:" {user} "has {score} failed login attempts """)
print("Security check complete """)

1