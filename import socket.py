import socket

esp_ip = "192.168.4.1"  # ESP32 AP IP
esp_port = 3333         # Match server port

# Connect to ESP32 TCP server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((esp_ip, esp_port))
print("Connected to ESP32")

print("Type W/A/S/D then Enter to send, Q to quit.")

while True:
    key = input("Enter: ").lower()
    if key in ['w', 'a', 's', 'd']:
        sock.send(key.encode())
        print(f"Sent: {key}")
    elif key == None:
        pass
    elif key == 'x':
        sock.send(b'x')
    elif key == 'q':
        sock.send(b'x')
        break
    else:
        print("Invalid input")

sock.close()
print("Disconnected")