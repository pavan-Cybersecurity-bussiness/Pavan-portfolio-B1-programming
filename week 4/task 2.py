devices = [ ("192.168.1.10", [22, 80, 443]),
("192.168.1.11", [21, 22, 80]), ("192.168.1.12", [23,
80, 3389])]
risky_ports = [21, 23, 3389]
risk_counter =0
for device in devices :
    ip =device[0]
    for port in device[1]:
        if port in risky_ports :

            print(f"{ip} has risky port {port} ")
            risk_counter += 1

print("Scan complete: " + str(risk_counter) + " has been found")
