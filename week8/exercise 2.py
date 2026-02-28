import hashlib
from datetime import datetime, timedelta
from execrise_1 import User

class Device:
    def __init__(self, device_id, device_type, firmware_version, owner):
        # Validation
        if not device_id or not isinstance(device_id, str):
            raise ValueError("device_id must be a non-empty string")
        if firmware_version.count('.') != 2:
            raise ValueError("firmware_version must be in 'X.Y.Z' format")

        self.__device_id = device_id
        self.__device_type = device_type
        self.__firmware_version = firmware_version
        self.__owner = owner
        self.__compliance_status = True
        self.__last_security_scan = datetime.now()
        self.__is_active = True
        self.__activity_log = []

        self.__log_activity(f"Device {device_id} created and assigned to {owner.display_info()['username']}")

    # -------- Private Methods --------
    def __log_activity(self, activity):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.__activity_log.append(f"{timestamp} - {activity}")

    # -------- Public Methods --------
    def authorise_access(self, user):
        self.check_compliance()
        if not self.__is_active:
            self.__log_activity(f"Access denied to {user.display_info()['username']}: device inactive")
            return False
        if self.__compliance_status or user.check_privileges() == 'admin':
            if user.display_info()['username'] == self.__owner.display_info()[
                'username'] or user.check_privileges() == 'admin':
                self.__log_activity(f"Access granted to {user.display_info()['username']}")
                return True
        self.__log_activity(f"Access denied to {user.display_info()['username']}")
        return False

    def update_firmware(self, new_version, user):
        if user.display_info()['username'] != self.__owner.display_info()[
            'username'] and user.check_privileges() != 'admin':
            self.__log_activity(f"{user.display_info()['username']} attempted firmware update without permission")
            return False
        self.__firmware_version = new_version
        self.__log_activity(f"Firmware updated to {new_version} by {user.display_info()['username']}")
        return True

    def run_security_scan(self):
        self.__last_security_scan = datetime.now()
        self.check_compliance()
        self.__log_activity(f"Security scan run; compliance status: {self.__compliance_status}")

    def check_compliance(self):
        if datetime.now() - self.__last_security_scan > timedelta(days=30):
            self.__compliance_status = False
            self.__log_activity("Device marked as non-compliant: scan overdue")
        return self.__compliance_status

    def quarantine(self, user):
        if user.check_privileges() != 'admin':
            self.__log_activity(
                f"{user.display_info()['username']} attempted to quarantine device without admin privileges")
            return False
        self.__is_active = False
        self.__log_activity(f"Device quarantined by admin {user.display_info()['username']}")
        return True

    def display_info(self):
        return {
            'device_id': self.__device_id,
            'device_type': self.__device_type,
            'firmware_version': self.__firmware_version,
            'compliance_status': self.__compliance_status,
            'owner': self.__owner.display_info()['username'],
            'is_active': self.__is_active
        }

    def get_activity_log(self):
        return self.__activity_log.copy()


class DeviceManager:
    def __init__(self):
        self.__devices = []

    def add_device(self, device):
        self.__devices.append(device)
        print(f"Device {device.display_info()['device_id']} added to system.")

    def remove_device(self, device_id):
        for device in self.__devices:
            if device.display_info()['device_id'] == device_id:
                self.__devices.remove(device)
                print(f"Device {device_id} removed from system.")
                return True
        print(f"Device {device_id} not found.")
        return False

    def generate_security_report(self):
        report = []
        for device in self.__devices:
            info = device.display_info()
            report.append(info)
        return report

### testing


# Assume User class from Lab 1 is available
admin = User('admin_user', 'AdminPass123', 'admin')
user1 = User('alice', 'AlicePass', 'standard')
user2 = User('bob', 'BobPass', 'standard')

# Create devices
device1 = Device('dev001', 'camera', '1.0.0', user1)
device2 = Device('dev002', 'sensor', '1.0.1', user2)

# Device manager
manager = DeviceManager()
manager.add_device(device1)
manager.add_device(device2)

# Access checks
print(device1.authorise_access(user1))  # True
print(device2.authorise_access(user1))  # False

# Firmware updates
device1.update_firmware('1.1.0', user1)
device2.update_firmware('1.1.0', admin)

# Run security scans
device1.run_security_scan()

# Quarantine a device
device2.quarantine(admin)

# Generate report
for info in manager.generate_security_report():
    print(info)