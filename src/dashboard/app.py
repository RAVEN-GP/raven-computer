from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'raven_secret'
socketio = SocketIO(app, cors_allowed_origins="*")

# Mock State for Display
telemetry = {
    "speed": 0.0,
    "steer": 0.0,
    "battery": 100,
    "state": "IDLE"
}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('command')
def handle_command(cmd):
    """Receive command from UI and (simulated) send to Brain"""
    print(f"Command received: {cmd}")
    # In a real scenario, this would publish to ROS or send via TCP to RPi
    if cmd == "emergency_stop":
        telemetry["speed"] = 0.0
        telemetry["state"] = "EMERGENCY"
    elif cmd == "start":
        telemetry["state"] = "DRIVE"
    socketio.emit('telemetry_update', telemetry)

def bg_thread():
    """Simulate incoming telemetry from RPi"""
    while True:
        socketio.sleep(1)
        # Mock data updates
        if telemetry["state"] == "DRIVE":
            telemetry["speed"] = 15.0
            telemetry["steer"] = 0.5
            telemetry["battery"] -= 1
        
        socketio.emit('telemetry_update', telemetry)

if __name__ == '__main__':
    socketio.start_background_task(bg_thread)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
