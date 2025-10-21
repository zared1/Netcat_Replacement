# Netcat Replacement

A tiny Python reimplementation of netcat’s simplest workflow: connect to a TCP host:port, allow interactive sending of lines, then receive and print the remote response. Minimal, educational, and useful for quick lab testing.

## Features

* Connects to a TCP server using a hostname/IP and port
* Interactive input mode — type lines to send; send an empty line to stop sending
* After sending, waits and prints any data received from the server
* Single-file, no external dependencies (only Python standard library)

## How to Run

1. Clone or save `netcat_replacement.py`.
2. Run the script with host and port:

```bash
python netcat_replacement.py <host> <port>
# Example:
python netcat_replacement.py localhost 9999
```

3. Type messages and press Enter to send each line.
4. Send an empty line (press Enter on an empty prompt) to finish sending; the script will then wait for the server’s response and print it.
5. When the server closes the connection or no more data arrives, the client exits.

## Notes

* This is a **very small** replacement — not a full netcat. It implements a basic send-then-receive flow.
* Behavior specifics:

  * Sending stops when you enter an empty line.
  * The code sleeps 3 seconds (`time.sleep(3)`) after sending to give the server time to respond; adjust/remove as needed.
* Limitations & safety:

  * No TLS/SSL, no authentication, no UDP support, no reverse/exec shells, and no advanced netcat flags.
  * Blocking I/O used — for bidirectional real-time sessions consider threading or `select`.
  * Use only on hosts you own or have permission to test.
