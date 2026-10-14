import socket
import json
import random
import time

HOST, PORT = "127.0.0.1", 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    for part_id in range(1, 6):
        result = {"part_id": part_id, "status": random.choice(["PASS", "FAIL"])}
        client.sendall((json.dumps(result) + "\n").encode())
        reply = client.recv(1024).decode().strip()
        print("Sent:", result, "| Reply:", reply)
        time.sleep(0.5)