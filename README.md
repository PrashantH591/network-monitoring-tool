# 🌐 Network Monitoring Tool

A Python-based network monitoring and troubleshooting tool designed to check host availability, DNS resolution, TCP connectivity and response times.

The project demonstrates practical network troubleshooting and automation techniques relevant to IT support and infrastructure operations.

---

## 🎯 Objectives

- Monitor network connectivity
- Test DNS resolution
- Check TCP connectivity
- Measure response times
- Monitor multiple targets
- Generate monitoring reports
- Identify potential connectivity problems

---

## 🛠️ Technologies

- Python 3
- TCP/IP
- DNS
- Sockets
- Networking
- Command-line troubleshooting

---

## 🔍 Monitoring Tests

The tool performs:

### DNS Resolution

Checks whether a hostname can be resolved.

### TCP Connectivity

Tests whether a TCP connection can be established to a specified port.

### Response Time

Measures how long the connection attempt takes.

### Multiple Hosts

Allows multiple hosts to be monitored from a configuration file.

---

## 📁 Project Structure

```text
network-monitoring-tool/
│
├── README.md
│
├── src/
│   └── network_monitor.py
│
├── config/
│   └── targets.txt
│
├── reports/
│   └── monitoring-report.txt
│
├── evidence/
│   └── test-results.md
│
└── screenshots/
