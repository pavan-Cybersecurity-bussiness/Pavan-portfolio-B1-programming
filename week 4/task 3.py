# this is a password validator
passwords = [ "Pass123",
"SecurePassword1", "weak",
"MyP@ssw0rd", "NOLOWER123","aaaasSsdd"]
compliant = 0
non_compliant =0
#check for minimum length
for password in passwords:
 if len(password) >= 8: # checks for length of password
     has_upper = any(char.isupper() for char in password)
     if has_upper :
         has_lower = any(char .islower() for char in password )
         if has_lower :
             has_digit = any(char .isdigit() for char in password )
             if has_digit :
                 compliant += 1
                 print(f"{password} meets all validation requirements")
             else:
                 print(f""" failed password :{password} , because it does NOT contain a number""")
                 non_compliant += 1
         else:
             print(f""" failed password :{password} , because it has NO lowercase letters""")
             non_compliant += 1
     else:
         print(f""" failed password :{password} , because it has NO uppercase letters""")
         non_compliant += 1
 else:
     print(f""" failed password :{password} , because it is too short""")
     non_compliant += 1

print(f"summary:{compliant} Compliant passwords ")
print(f" {non_compliant} NON-Compliant passwords")