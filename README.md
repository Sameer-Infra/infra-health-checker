# infra-health-checker

# DevOps Infrastructure Health Checker

A lightweight, object-oriented Python automation tool to check network connectivity and system service status using terminal commands.

## 🚀 Features
- **Network Ping Checker:** Automatically pings target servers (e.g., Google DNS) to check connectivity.
- **Service Status Checker:** Uses `systemctl` to verify if critical background services (like Docker) are running.
- **Polymorphic Execution:** Uses Python OOPs concepts to execute different types of infrastructure checks seamlessly in a single loop.

## 🛠️ How to Run
```bash
python infra_health_checker.py
