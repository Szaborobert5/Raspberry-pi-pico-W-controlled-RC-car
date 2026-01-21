from steering import steeringWheel
from trajectory import Trajectory
from webserver import WebServer

steering = steeringWheel()
trajectory = Trajectory()

server = WebServer(
    ssid = "7D654F",
    password = "ej7xatsve3",
    steering = steering,
    trajectory = trajectory
    )

server.start()
