from flask import Flask, request, send_from_directory, jsonify
import socket

# Print your LAN IP
ip = socket.gethostbyname(socket.gethostname())
print(f"Server running at: http://{ip}:8000")

app = Flask(__name__)

# Serve HTML
@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('.', filename)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Example POST handler
@app.route("/update", methods=["POST"])
def update():
    data = request.json
    print("Received:", data)
    return jsonify({"status":"ok","echo":data})

# Run with debug (auto-reload)
app.run(host="0.0.0.0", port=8000, debug=True)
