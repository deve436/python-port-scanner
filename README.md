# Multi-Threaded Network Port Scanner

## Project Description
This is a custom cybersecurity tool developed using Python. It is a network reconnaissance tool designed to scan a target IP address for open ports. By utilizing **Socket Programming** and **Multi-Threading**, this scanner can identify running services on a network much faster than a standard single-threaded script.

This project was built to demonstrate my understanding of:
*   **Networking Protocols:** How TCP connections work.
*   **Concurrency:** Using Python's `threading` module to run parallel tasks.
*   **Socket Programming:** Establishing connections between client and server.

## Features
*   **High Performance:** Uses 30 concurrent threads to speed up the scanning process.
*   **Port Range:** Scans ports 1 through 1000 (commonly used ports).
*   **Clean Output:** Uses thread locking to ensure the console output remains readable and organized.
*   **Error Handling:** Gracefully handles closed ports or connection timeouts.

## Technologies Used
*   **Language:** Python 3
*   **Modules:** `socket`, `threading`, `queue`, `datetime`

## How to Run
1.  Ensure you have Python installed.
2.  Clone this repository or download the `scanner.py` file.
3.  Open your terminal/command prompt.
4.  Run the script:
    ```bash
    python scanner.py
    ```
5.  When prompted, enter the IP address you wish to scan (e.g., `127.0.0.1` for your local machine).

## ⚠️ Legal Disclaimer
**For Educational Purposes Only.**
This tool is intended for security research and learning. Please only use this scanner on networks you own or have explicit permission to test. Unauthorized scanning of networks is illegal.
