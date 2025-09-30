import socket
import struct

esp_ip = "192.168.4.1"  # ESP32 softAP IP
esp_port = 3333         # Port to match the ESP32 server

# Connect to ESP32 TCP server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((esp_ip, esp_port))
print(" Connected to ESP32")

print("Type 1–6 to control speed, 'x' to stop, 'q' to quit.")

pwm = 0
while True:
    key = input("Enter: ")

    if key in ['1', '2', '3', '4', '5', '6']:
        pwm = 15 + 15 * int(key)
    elif key == 'x':
        pwm = 0
    elif key == 'q':
        pwm = 0
        data = struct.pack('<i', pwm)
        sock.sendall(data)
        break
    else:
        print("Invalid input")
        continue

    data = struct.pack('<i', pwm)
    sock.sendall(data)

sock.close()
print("🔌 Disconnected")
