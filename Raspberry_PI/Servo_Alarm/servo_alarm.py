import network
import socket
import json
import time
from machine import Pin, PWM
from machine import Timer
import ntptime

# WiFi configuration
WIFI_SSID = "PAL 5.0"
WIFI_PASSWORD = "ManDunn123"

# Initialize WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Connect to WiFi
print(f"Connecting to {WIFI_SSID}...")
wlan.connect(WIFI_SSID, WIFI_PASSWORD)
while not wlan.isconnected():
    time.sleep(1)
print("Connected to WiFi")
print(f"IP address: {wlan.ifconfig()[0]}")

# Initialize servo
servo = PWM(Pin(15), freq=50)
servo.duty_u16(1638)  # 0 degrees position

# WebSocket server
def start_websocket_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 8080))
    s.listen(1)
    print("WebSocket server started on port 8080")
    return s

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Parse the received data
            try:
                message = json.loads(data.decode())
                if message.get('type') == 'setAlarm':
                    alarm_time = message.get('time')
                    print(f"Alarm set for {alarm_time}")
                    # Store alarm time and start checking
                    check_alarm(alarm_time)
            except json.JSONDecodeError:
                print("Invalid JSON received")
                
        except Exception as e:
            print(f"Error handling client: {e}")
            break
    
    client_socket.close()

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
server_socket = start_websocket_server()

# Main loop
while True:
    try:
        client_socket, addr = server_socket.accept()
        print(f"Client connected from {addr}")
        handle_client(client_socket)
    except Exception as e:
        print(f"Server error: {e}")
        time.sleep(1) 