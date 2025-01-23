# JWT Authentication App

This is a small Flask-based web application that implements **JWT** for user authentication. The app is designed to showcase a secure login system and protected routes, and it is containerized with Docker.

---

## **Features**
1. **User Authentication**:
   - `/login` endpoint for username/password authentication.
   - JWT is generated for valid users.
2. **Protected Routes**:
   - `/post-auth` endpoint requires a valid JWT to access.
3. **Dockerized**:
   - The app runs inside a Docker container for consistent deployment.

---

## **Tech Stack**
- **Backend**: Flask (Python)
- **Authentication**: PyJWT
- **Containerization**: Docker

---

## **Getting Started**

### **Prerequisites**
- Docker installed on your system.


### Docker Hub

The app is available as a Docker image on Docker Hub:

Link: florinbuzea/basic-jwt-app
To run the container directly from Docker Hub:

docker run -p 5000:5000 florinbuzea/basic-jwt-app


### **Running the App Locally**
1. Clone the repository:
   git clone https://github.com/acceptallcookies1/Basic_jwt_app.git
   cd Basic_jwt_app

2. Build the Docker image:
 docker build -t basic-jwt-app .

3. Run the Docker contasiner: 
docker run -p 5000:5000 basic-jwt-app

4. Access the app in your browser or API tool at:
- Homepage: http://127.0.0.1:5000
- Login Endpoint: http://127.0.0.1:5000/login
- Protected Route: http://127.0.0.1:5000/post-auth

-------------------------------------------------------------------------------------

### Using the API

# Login Endpoint:
- URL: /login
- Method: POST
- Request Body (json):
{
  "username": "john_doe",
  "password": "password123"
}

# You get: 

{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}

# Protected Route
- URL: /post-auth
- Method: GET
- Headers:
 Authorization: Bearer <your_JWT_token>


- Response(Valid token):
{
  "message": "Hello, john_doe! This is a protected route."
}



### Future Enhancements
1. Add a frontend for user interaction (HTML/CSS/JS).
2. Integrate a database for user management.
3. Deploy to a cloud platform (e.g., Heroku or AWS).
4. Implement HTTPS and secure secrets management.


License
This project is open-source and available under the MIT License.

Contributors
Florin Buzea
