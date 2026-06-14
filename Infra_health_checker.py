import os

class BaseCheck():
    def __init__(self, check_name):
        self.check_name = check_name

class PingChecker(BaseCheck):
    def __init__(self, check_name, ip_address):
        super().__init__(check_name)
        self.ip_address = ip_address

    def run(self):
        command = f"ping -c 1 {self.ip_address}"
        os.system(command)

class ServiceChecker(BaseCheck):
    def __init__(self, check_name, service_name):
        super().__init__(check_name)
        self.service_name = service_name

    def run(self):
        command = f"systemctl is-active --quiet {self.service_name}"
        os.system(command)

google_bot = PingChecker("Google Server", "8.8.8.8")
docker_bot = ServiceChecker("Docker_Service", "docker")

all_checks = [google_bot, docker_bot]

for check in all_checks:
    print(f"---Running: {check.check_name} ---")
    check.run()
