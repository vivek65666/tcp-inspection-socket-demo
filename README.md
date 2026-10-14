# TCP Inspection Socket Demo

A Python TCP client-server that exchanges JSON inspection results (PASS/FAIL),
simulating machine-to-software communication in an industrial inspection setup.

## Features
- Multithreaded TCP server (one thread per client)
- Newline-delimited JSON messages (message framing over TCP)
- Acknowledgement reply for every message, with error handling for invalid input

## Run
```
python server.py
python client.py
```

## Tech
Python, socket, threading, json

## Output

**Server**

![Server output](server-output.png)

**Client**

![Client output](client-output.png)
