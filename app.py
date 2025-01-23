from flask import Flask, request, jsonify, send_from_directory
import jwt
import datetime
import os

# Create the Flask app
app = Flask(__name__, static_folder="frontend", static_url_path="")

# Secret key for JWT (in a real app, store this securely)
SECRET_KEY = os.getenv("SECRET_KEY", "SuperSecret123")  # Use environment variable for security

# Fake user database
fake_users_db = {
    "john_doe": "password123",
    "alice": "mypassword"
}

# Function to generate a JWT
def generate_token(username):
    now = datetime.datetime.now(datetime.timezone.utc)  # Use timezone-aware UTC datetime
    payload = {
        "sub": username,
        "iat": now,
        "exp": now + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# Serve static HTML files
@app.route("/")
def serve_home():
    return send_from_directory(app.static_folder, "index.html")

# Login route
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    
    # Check for username and password
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Missing username or password"}), 400

    username = data["username"]
    password = data["password"]

    # Validate credentials
    if username in fake_users_db and fake_users_db[username] == password:
        token = generate_token(username)
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Protected route
@app.route("/post-auth", methods=["GET"])
def protected():
    # Get the Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing or invalid token"}), 401

    # Extract the token
    token = auth_header.split(" ")[1]

    # Validate the token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"message": f"Hello, {payload['sub']}! This is a protected route."}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

# Catch-all route for other static files (CSS, JS)
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
