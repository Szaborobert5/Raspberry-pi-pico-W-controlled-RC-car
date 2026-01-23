from steering import steeringWheel
from trajectory import Trajectory
from webserver import WebServer

steering = steeringWheel()
trajectory = Trajectory()

server = WebServer(
    ssid = "",
    password = "",
    steering = steering,
    trajectory = trajectory
    )

server.start()

