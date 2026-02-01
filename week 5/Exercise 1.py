#this is a password validation tool aiming to teach fuction and import statements
# create multiple sub moduel and then integrate all of them into a single moduel

import random

# part a
def check_min_length(password,min_lenght=8):
    if len(password) >= min_lenght:
        return True
    else:
        return False
"""
def NEhas_uppercase(password): #NE -not effecient
    Upper = False
    for char in password:
        if (char.isupper()):
            Upper = True
    return Upper

def NE1has_uppercase(password): # #NE1 -not effecient
     upper = False
     upper = any(char.isupper() for char in password )
     return upper

"""
def has_uppercase(password):
    return any(char.isupper() for char in password)
# how to check it works
"""def has_uppercase(password):
    def check_char(c):
        print(f"Checking: {c}")   # Trace each character
        return c.isupper()         # Return True/False for any()

    return any(check_char(c) for c in password)
    # works by chacking each chara if it is true then we stop using the any If any is true."""

def has_lowercase(password):
    return any(char.islower() for char in password)
def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_char(password):
    return any(not char.isalnum() for char in password)

##  master validation fuction validation function

def validate_password(password):
    results = {
        "min_length": {
            "passed": check_min_length(password),
            "true_msg": "Minimum length requirement met",
            "false_msg": "Password is too short (minimum 8 characters)"
        },
        "uppercase": {
            "passed": has_uppercase(password),
            "true_msg": "Contains an uppercase letter",
            "false_msg": "Must contain at least one uppercase letter"
        },
        "lowercase": {
            "passed": has_lowercase(password),
            "true_msg": "Contains a lowercase letter",
            "false_msg": "Must contain at least one lowercase letter"
        },
        "digit": {
            "passed": has_digit(password),
            "true_msg": "Contains a digit",
            "false_msg": "Must contain at least one digit"
        },
        "special": {
            "passed": has_special_char(password),
            "true_msg": "Contains a special character",
            "false_msg": "Must contain at least one special character"
        }
    }

    results["is_valid"] = all(
        rule["passed"] for rule in results.values()
    )
    for rule, data in results.items():
        if rule == "is_valid":
            continue

        if data["passed"]:
            print(f"{rule}: {data['true_msg']} ")
        else:
            print(f"{rule}: {data['false_msg']} ")




    if results["is_valid"]:
       print(" STRONG PASSWORD")
    else:
       print(" WEAK PASSWORD")
    return ""

print(validate_password("hello"))
print(validate_password("HelLo22@"))
"""def validate_password(password):
    results = {
        "min_length": check_min_length(password),
        "uppercase": has_uppercase(password),
        "lowercase": has_lowercase(password),
        "digit": has_digit(password),
        "special": has_special_char(password)
    }

    results["is_valid"] = all(results.values())
    if not results["is_valid"]:
        pass
    return results["is_valid"]

"""



"""def validate_password(password):
    lengt_ok =check_min_length(password)
    upper_ok = has_uppercase(password)
    lower_ok = has_lowercase(password)
    digit_ok = has_digit(password)
    special_ok = has_special_char(password)

    return lengt_ok, upper_ok,lower_ok, digit_ok, special_ok
"""
print("password validator")
print("-"*30)
passw =input("please enter your password : ")
validate_password(passw)
