# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /signup

# Copy the current directory contents into the container at /app
COPY . .

# Get the dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 5000 for the Flask app to listen on
EXPOSE 3000

# Define environment variables for InfluxDB client configuration
ENV INFLUXDB_HOST=localhost \
    INFLUXDB_PORT=8086 \
    INFLUXDB_USERNAME=myusername \
    INFLUXDB_PASSWORD=mypassword \
    INFLUXDB_DATABASE=mydatabase

# Run app.py when the container launches
CMD ["python", "src/app.py"]

