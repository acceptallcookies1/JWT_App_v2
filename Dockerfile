# Use the official Python image
FROM python:3.13.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application source code to the container
COPY . /app

# Install system dependencies for psycopg2 and other libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV PORT=5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
