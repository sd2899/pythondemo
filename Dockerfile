# Use a Python base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Flask application code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Expose the port that Flask app runs on
EXPOSE 5000

# Run tests
RUN pytest

# Run the Flask application
CMD ["python", "app.py"]


