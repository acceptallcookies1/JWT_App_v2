# Flask JWT App

A simple Flask-based application demonstrating user authentication, JWT (JSON Web Tokens), and secure API interactions. The app includes a login page, post-authentication form, and rate limiting to prevent abuse.

---

## **Features**
- User authentication with JWT tokens.
- Protected `/post-auth` endpoint for form submissions.
- Input validation and sanitization to prevent injection attacks.
- Rate limiting to prevent brute-force attacks.
- Fully containerized with Docker for easy deployment.

---

## **Requirements**
- Python 3.10+
- Flask
- Flask-Limiter
- Docker (optional)

---

## **Getting Started**

### **1. Clone the Repository**
git clone https://github.com/your-repo-name.git
cd your-repo-name


### **2. Install Dependencies
pip install -r requirements.txt


### **3. Run the Application Locally
python app.py


## Run with Docker

### 1. Build the Docker image
docker build -t flask-jwt-app .

## 2. Run the container
docker run -p 5000:5000 flask-jwt-app

Access the app at http://localhost:5000.


## Deploy to Heroku
This app can be deployed freely to Heroku for testing purposes.

### Steps to Deploy

1. Install the Heroku CLI.
2. Log in to your Heroku account:
heroku login

3. Create a new Heroku app:
heroku create

4. Deploy the app:
git push heroku main

5. Open your app in the browser:
heroku open

You can access the app on Heroku to test authentication and endpoints without additional infrastructure costs.

##E ndpoints
### 1. Login
URL: /login
Method: POST
Payload:
{
  "username": "test",
  "password": "5g5KiSpZ8HRdkfAp3O3T*"
}

Response:
200 OK: Returns a JWT token.
401 Unauthorized: Invalid credentials.

### 2. Post Authentication
URL: /post-auth
Method: POST
Headers:

{
  "Authorization": "Bearer <your-token>"
}


Payload: 
{
  "formData": "example-data"
}


Response:
200 OK: Form data submitted successfully.
400 Bad Request: Invalid or missing form data.
401 Unauthorized: Missing or invalid token.


## Security Measures
1. Input Validation and Sanitization:
- Ensures only valid data is accepted.
- Alphanumeric check for form inputs.

2. Rate Limiting:
- Login attempts: 5 per minute.
- Post-auth interactions: 10 per minute.

3. Debug Mode Disabled:
- Prevents sensitive information from being exposed in production.


## Project Structure
.
├── app.py               # Main application code
├── requirements.txt     # Python dependencies
├── frontend/
│   ├── index.html       # Frontend HTML
│   ├── style.css        # Styling
│   └── script.js        # Frontend logic
├── Dockerfile           # Docker configuration
└── README.md            # Project documentation


## Future Improvements
1. Adding a Database:
- Replace the current dictionary-based user database with a real database (e.g., PostgreSQL or MySQL).
- Enhance user authentication with hashed passwords and user roles.

2. Migrating to AWS Infrastructure:
- Deploy the app to AWS services for better scalability and integration with other AWS tools (RDS for database, API Gateway, Lambda).
