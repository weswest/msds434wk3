# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application source code
COPY . .

# Expose the port on which the app will run
EXPOSE 8080

# Command to run the application
CMD ["python3", "wk3.py"]
