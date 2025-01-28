from flask import Flask, request, jsonify, send_from_directory
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import jwt
import datetime
import os

# Create the Flask app
app = Flask(__name__, static_folder="frontend", static_url_path="")

# Initialize rate limiting
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per minute"],  # Default limit for all routes
)

# Secret key for JWT
SECRET_KEY = os.getenv("SECRET_KEY", "SuperSecret123")

# Fake user database
fake_users_db = {
    "test": "5g5KiSpZ8HRdkfAp3O3T*",
    "test2": "BE7BnEpqCuVuMbrYyQSH@"
}

# Function to generate a JWT
def generate_token(username):
    now = datetime.datetime.now(datetime.timezone.utc)
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

# Login route with rate limiting
@app.route("/login", methods=["POST"])
@limiter.limit("5 per minute")  # Rate limit specifically for login
def login():
    data = request.get_json()
    
    # Validate input
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid input format"}), 400
    
    username = data.get("username")
    password = data.get("password")

    # Validate user credentials
    if username in fake_users_db and fake_users_db[username] == password:
        token = generate_token(username)
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Protected route with input validation
@app.route("/post-auth", methods=["POST"])
@limiter.limit("10 per minute")  # Rate limit specifically for post-auth
def post_auth():
    # Get Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing or invalid token"}), 401

    token = auth_header.split(" ")[1]

    # Validate the token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        form_data = request.json.get("formData")

        # Validate and sanitize form data
        if not form_data or not isinstance(form_data, str) or not form_data.isalnum():
            return jsonify({"error": "Invalid form data"}), 400

        return jsonify({"message": f"Hello, {payload['sub']}! You submitted: {form_data}"}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)  # Debug mode disabled
