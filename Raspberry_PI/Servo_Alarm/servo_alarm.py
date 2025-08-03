import network
import socket
import json
import time
from machine import Pin, PWM
from machine import Timer
import ntptime
import base64
import hashlib

# WiFi configuration
WIFI_SSID = "PAL 5.0"
WIFI_PASSWORD = "ManDunn123"

# Initialize WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Connect to WiFi
print("Starting WiFi connection...")
print(f"Connecting to {WIFI_SSID}...")
wlan.connect(WIFI_SSID, WIFI_PASSWORD)

# Wait for connection with timeout
max_wait = 10
while max_wait > 0:
    if wlan.isconnected():
        break
    max_wait -= 1
    print('Waiting for connection...')
    time.sleep(1)

if not wlan.isconnected():
    print('WiFi connection failed')
    raise Exception('WiFi connection failed')

print("Connected to WiFi")
print(f"IP address: {wlan.ifconfig()[0]}")
print(f"Subnet mask: {wlan.ifconfig()[1]}")
print(f"Gateway: {wlan.ifconfig()[2]}")
print(f"DNS: {wlan.ifconfig()[3]}")

# Initialize servo
servo = PWM(Pin(15), freq=50)
servo.duty_u16(1638)  # 0 degrees position

# Initialize LED
led = Pin("LED", Pin.OUT)
led.value(1)  # Turn on LED to indicate system is running

def get_websocket_key(headers):
    for line in headers.split('\r\n'):
        if line.startswith('Sec-WebSocket-Key:'):
            return line.split(': ')[1].strip()
    return None

def create_websocket_response(key):
    GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
    accept_key = base64.b64encode(hashlib.sha1((key + GUID).encode()).digest()).decode()
    return (
        "HTTP/1.1 101 Switching Protocols\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        f"Sec-WebSocket-Accept: {accept_key}\r\n"
        "\r\n"
    )

def handle_websocket_handshake(client_socket):
    try:
        data = client_socket.recv(1024).decode()
        if "Upgrade: websocket" in data:
            key = get_websocket_key(data)
            if key:
                response = create_websocket_response(key)
                client_socket.send(response.encode())
                return True
    except Exception as e:
        print(f"Error during handshake: {e}")
    return False

def start_websocket_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind(('0.0.0.0', 8080))
        s.listen(1)
        print("WebSocket server started on port 8080")
        return s
    except Exception as e:
        print(f"Error starting server: {e}")
        raise

def handle_client(client_socket):
    print(f"New client connected from {client_socket.getpeername()}")
    
    # Perform WebSocket handshake
    if not handle_websocket_handshake(client_socket):
        print("WebSocket handshake failed")
        client_socket.close()
        return

    print("WebSocket handshake successful")
    
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("Client disconnected")
                break
            
            # Print raw data for debugging
            print(f"Received raw data: {data}")
            
            # Parse the received data
            try:
                message = json.loads(data.decode())
                print(f"Parsed message: {message}")  # Debug print
                if message.get('type') == 'setAlarm':
                    alarm_time = message.get('time')
                    print(f"Alarm set for {alarm_time}")
                    # Store alarm time and start checking
                    check_alarm(alarm_time)
                elif message.get('type') == 'moveServo':
                    direction = message.get('direction')
                    print(f"Moving servo {direction}")  # Debug print
                    if direction == 'clockwise':
                        servo.duty_u16(4915)  # Move to 90 degrees
                        time.sleep(0.5)  # Wait for movement
                        servo.duty_u16(1638)  # Return to 0 degrees
                    elif direction == 'counterclockwise':
                        servo.duty_u16(1638)  # Move to 0 degrees
                        time.sleep(0.5)  # Wait for movement
                        servo.duty_u16(4915)  # Return to 90 degrees
            except ValueError as e:
                print(f"Invalid JSON received: {data.decode()}")  # Print the invalid data
                
        except Exception as e:
            print(f"Error handling client: {e}")
            break
    
    client_socket.close()
    print("Client connection closed")

def check_alarm(alarm_time):
    while True:
        try:
            # Get current time from NTP server
            ntptime.settime()
            current_time = time.localtime()
            current_time_str = f"{current_time[3]:02d}:{current_time[4]:02d}"
            
            if current_time_str == alarm_time:
                # Trigger servo movement
                servo.duty_u16(4915)  # Move to 90 degrees
                time.sleep(2)  # Wait for movement
                servo.duty_u16(1638)  # Return to 0 degrees
                break
                
            time.sleep(30)  # Check every 30 seconds
            
        except Exception as e:
            print(f"Error checking alarm: {e}")
            time.sleep(60)  # Wait a minute before retrying

# Start the server
print("Starting WebSocket server...")
server_socket = start_websocket_server()

# Main loop
print("Entering main loop...")
while True:
    try:
        print("Waiting for client connection...")
        client_socket, addr = server_socket.accept()
        print(f"Client connected from {addr}")
        handle_client(client_socket)
    except Exception as e:
        print(f"Server error: {e}")
        time.sleep(1) 