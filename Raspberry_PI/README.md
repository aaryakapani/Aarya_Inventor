# Aarya_Inventor
Intent of this Repo is for Aarya's personal projects

Activating my venv to get ampy to work, which is what is used to connect to the Rapsberry -> source myenv/bin/activate
Help detect your devices -> Desktop % ls /dev/tty.*

Raspberry pi Pico -> /dev/tty.usbmodem2101 (Or something like that, can change depending on which port its connected to)

IP Address of the Pico W: 192.168.1.2

Once in the venv, run this while in your python directory -> ampy --port /dev/tty.usbmodem2101 run led.py

To run the web app:
- Cd into servo-alarm-webapp
write "npm run dev"