from flask import Flask, request, jsonify
import jwt
import datetime

# Create the Flask app
app = Flask(__name__)

# Secret key for JWT (in a real app, store this securely)
SECRET_KEY = "SuperSecret123"

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

# Homepage route
@app.route("/")
def home():
    return "Welcome to the Basic JWT App!"

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

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
 