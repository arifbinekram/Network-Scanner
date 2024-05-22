# Network Scanner

## Overview

The Network Scanner is a Python script designed to scan a network for active devices. It identifies devices connected to a network by sending ARP requests and compiling the responses into a neat and informative output.

## Features

- Scans the network for active devices.
- Displays IP addresses and MAC addresses of detected devices.
- Lightweight and easy to use.

## Requirements

- Python 3.x
- Scapy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/arifbinekram/Network-Scanner.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Network-Scanner
   ```

3. Install the required dependencies. You can install Scapy using pip:

   ```bash
   pip install scapy
   ```

## Usage

The network scanner script scans a specified IP range for active devices.

1. Run the network scanner script with root privileges:

   ```bash
   sudo python network_scanner.py -t <target_ip_range>
   ```

   Replace `<target_ip_range>` with the IP range you want to scan. For example, to scan the range `192.168.1.1/24`, you would run:

   ```bash
   sudo python network_scanner.py -t 192.168.1.1/24
   ```

## Example Output

When you run the script, you should see an output similar to the following:

```text
Scanning target 192.168.1.1/24
IP Address      MAC Address
-----------------------------------------
192.168.1.1     00:14:22:01:23:45
192.168.1.2     00:16:17:2A:3B:4C
192.168.1.3     00:19:DB:83:44:55
```

## Disclaimer

This project is intended for educational purposes only. Unauthorized scanning of networks is illegal and unethical. Use this tool responsibly and only on networks where you have explicit permission to test.

---

Feel free to contribute to this project by submitting issues or pull requests to the GitHub repository.
