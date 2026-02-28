import hashlib
from datetime import datetime

class User:
    def __init__(self, username, password, privilege='guest'):
        self.__username = username
        self.__password_hash = self.__hash_password(password)
        self.__privilege = privilege
        self.__login_attempts = 0
        self.__status = 'active'
        self.__activity_log = []

    # -------- Private Methods --------
    def __hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def __log_activity(self, activity):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.__activity_log.append(f"{timestamp} - {activity}")

    # -------- Public Methods --------
    def authenticate(self, password):
        if self.__status == 'locked':
            self.__log_activity("Login attempt failed: account locked")
            return False

        if self.__password_hash == self.__hash_password(password):
            self.__login_attempts = 0
            self.__log_activity("Login successful")
            return True
        else:
            self.__login_attempts += 1
            self.__log_activity(f"Login attempt failed: incorrect password ({self.__login_attempts}/3)")
            if self.__login_attempts >= 3:
                self.lock_account()
            return False

    def check_privileges(self):
        return self.__privilege

    def lock_account(self):
        self.__status = 'locked'
        self.__log_activity("Account locked due to failed login attempts")

    def reset_login_attempts(self):
        self.__login_attempts = 0
        self.__log_activity("Login attempts reset")

    def elevate_privilege(self, new_privilege, authorizer):
        """Only an admin can elevate privileges"""
        if authorizer.check_privileges() == 'admin':
            self.__privilege = new_privilege
            self.__log_activity(f"Privilege elevated to {new_privilege} by {authorizer.__username}")
            return True
        else:
            self.__log_activity(f"Unauthorized privilege escalation attempt by {authorizer.__username}")
            return False

    def display_info(self):
        """Safely display user info without exposing sensitive data"""
        return {
            'username': self.__username,
            'privilege': self.__privilege,
            'status': self.__status,
            'login_attempts': self.__login_attempts
        }

    def get_activity_log(self):
        """Return a copy of the activity log"""
        return self.__activity_log.copy()

#test the system


# Create users
admin = User('admin_user', 'AdminPass123', 'admin')
guest = User('guest_user', 'GuestPass123', 'guest')

# Authenticate
print(guest.authenticate('wrongpass'))  # False
print(guest.authenticate('wrongpass'))  # False
print(guest.display_info())
print(guest.authenticate('wrongpass'))  # False, account locked

# Display info safely
print(guest.display_info())

# Admin elevates privilege
print(guest.elevate_privilege('standard', admin))  # True

# Print activity logs
print(guest.get_activity_log())