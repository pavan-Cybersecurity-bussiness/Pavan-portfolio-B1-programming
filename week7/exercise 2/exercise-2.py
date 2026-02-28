import re
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('analysis_audit_analysis.log'),
        logging.StreamHandler()
    ]
)

class AuditLogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.total_entries = 0
        self.security_incidents = []
        self.errors = []

        # Patterns to extract info from audit.log lines
        self.patterns = {
            'forbidden': re.compile(r'Forbidden access attempt: (\S+) -> (\S+)'),
            'sql_injection': re.compile(r'Potential SQL injection: (\S+) -> (\S+)'),
            'brute_force': re.compile(r'Brute force attempt from (\S+) - (\d+) failed attempts'),
            'error': re.compile(r'ERROR - (.+)')
        }

    def process_logs(self):
        try:
            with open(self.log_file, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    self.total_entries += 1
                    matched = False

                    # Forbidden access
                    m = self.patterns['forbidden'].search(line)
                    if m:
                        ip, url = m.groups()
                        incident = f"Forbidden access attempt: {ip} -> {url}"
                        self.security_incidents.append(incident)
                        logging.warning(incident)
                        matched = True

                    # SQL injection
                    m = self.patterns['sql_injection'].search(line)
                    if m:
                        ip, url = m.groups()
                        incident = f"Potential SQL injection: {ip} -> {url}"
                        self.security_incidents.append(incident)
                        logging.warning(incident)
                        matched = True

                    # Brute force
                    m = self.patterns['brute_force'].search(line)
                    if m:
                        ip, attempts = m.groups()
                        incident = f"Brute force attempt from {ip} - {attempts} failed attempts"
                        self.security_incidents.append(incident)
                        logging.warning(incident)
                        matched = True

                    # Any errors
                    m = self.patterns['error'].search(line)
                    if m:
                        error_text = m.group(1)
                        self.errors.append(error_text)
                        logging.error(f"Line {line_num}: {error_text}")
                        matched = True

                    if not matched:
                        # Optionally handle unknown lines
                        pass

            logging.info(f"Processing complete: {self.total_entries} entries checked")

        except FileNotFoundError:
            logging.error(f"Log file '{self.log_file}' not found")
            raise
        except PermissionError:
            logging.error(f"Permission denied reading '{self.log_file}'")
            raise

    def generate_security_report(self):
        """Write security incidents to security_incidents.txt"""
        try:
            with open('security_incidents.txt', 'w') as f:
                f.write("SECURITY INCIDENTS REPORT\n")
                f.write("="*70 + "\n")
                f.write(f"Total security incidents: {len(self.security_incidents)}\n\n")
                for incident in self.security_incidents:
                    f.write(f"{incident}\n")
            logging.info("Security report generated")
        except PermissionError:
            logging.error("Cannot write security_incidents.txt")

    def generate_error_log(self):
        """Write errors to error_log.txt"""
        try:
            with open('error_log.txt', 'w') as f:
                f.write("ERROR LOG\n")
                f.write("="*70 + "\n")
                f.write(f"Total errors: {len(self.errors)}\n\n")
                for e in self.errors:
                    f.write(f"{e}\n")
            logging.info("Error log generated")
        except PermissionError:
            logging.error("Cannot write error_log.txt")

def main():
    analyzer = AuditLogAnalyzer('analysis_audit.log')
    analyzer.process_logs()
    analyzer.generate_security_report()
    analyzer.generate_error_log()

    print("\nAnalysis Complete!")
    print(f"Total entries processed: {analyzer.total_entries}")
    print(f"Security incidents found: {len(analyzer.security_incidents)}")
    print(f"Errors found: {len(analyzer.errors)}")
    print("\nReports generated:")
    print(" - security_incidents.txt")
    print(" - error_log.txt")
    print(" - analysis_audit_analysis.log")

if __name__ == "__main__":
    main()