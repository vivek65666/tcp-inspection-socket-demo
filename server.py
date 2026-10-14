import socket
import threading
import json

HOST, PORT = "127.0.0.1", 5000

def handle_client(conn, addr):
    print(f"[+] Connected: {addr}")
    with conn:
        buffer = ""
        while True:
            data = conn.recv(1024)
            if not data:
                break
            buffer += data.decode()
            while "\n" in buffer:                  # one JSON message per line
                line, buffer = buffer.split("\n", 1)
                try:
                    msg = json.loads(line)
                    print(f"[{addr[1]}] Part {msg['part_id']}: {msg['status']}")
                    reply = {"ack": True, "part_id": msg["part_id"]}
                except (json.JSONDecodeError, KeyError):
                    reply = {"ack": False, "error": "invalid message"}
                conn.sendall((json.dumps(reply) + "\n").encode())
    print(f"[-] Disconnected: {addr}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = server.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()