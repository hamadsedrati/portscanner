# Multi-threaded Port Scanner

A simple multi-threaded Python port scanner that scans all TCP ports (1–65535) on a given target host and prints the open ones.

## Features
- Scans all TCP ports on a given target.
- Multi-threaded for faster scanning.
- Gracefully handles errors and interruptions.
- Displays start time and target information.

## Requirements
- Python 3.x

No external libraries are required, only Python's standard library.

## Usage

```bash
python portscanner.py <target>
```

**Example:**

```bash
python portscanner.py example.com
```

**Output:**

```
--------------------------------------------------
Scanning target: 93.184.216.34
Time started: 2025-08-13 12:34:56.789012
--------------------------------------------------
Port 80 is open
Port 443 is open
...
Port scanning completed!
```

## How It Works

1. Resolves the hostname to an IP address.
2. Starts a thread for each port in the range `1–65535`.
3. Attempts to connect to each port using a TCP socket.
4. Prints ports that are open.

## Important Notes

* Running a full scan on all ports will take time and system resources.
* Scanning hosts without permission is **illegal** in many jurisdictions.
* Only scan systems you own or have explicit authorization to test.

## License

This project is licensed under the MIT License, see the [LICENSE](LICENSE) file for details.
