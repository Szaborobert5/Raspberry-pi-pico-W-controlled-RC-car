import network
import socket
import time
from HTMLpage import HTML_PAGE

class WebServer:
    def __init__(self, ssid, password, steering, trajectory):
        self.ssid = ssid
        self.password = password
        self.steering = steering
        self.trajectory = trajectory

    def connectWifi(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.password)

        while not wlan.isconnected():
            time.sleep(0.3)

        print("Connected at http://", wlan.ifconfig()[0])

    def start(self):
        self.connectWifi()

        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", 80))
        s.listen(1)

        while True:
            client, _ = s.accept()
            request = client.recv(1024).decode()

            # --- STEERING ---
            if "/steer?dir=" in request:
                direction = request.split("dir=")[1].split(" ")[0]

                if direction == "left":
                    self.steering.steerLeft()
                elif direction == "right":
                    self.steering.steerRight()
                elif direction == "middle":
                    self.steering.steerMiddle()

            # --- TRAJECTORY ---
            elif "/trajectory?dir=" in request:
                traj_dir = request.split("dir=")[1].split(" ")[0]

                if traj_dir == "forward":
                    self.trajectory.forward()
                elif traj_dir == "backward":
                    self.trajectory.backward()
                elif traj_dir == "stop":
                    self.trajectory.stop()
                    
            elif "/speed?value=" in request:
                value = request.split("value=")[1].split(" ")[0]
                try:
                    speed = int(value)
                    self.trajectory.set_speed(speed)
                except:
                    pass

            # --- RESPONSE ---
            client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
            client.send(HTML_PAGE)
            client.close()

