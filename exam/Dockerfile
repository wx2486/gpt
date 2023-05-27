# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Copy the app.py, cert.pem, key.pem and any other necessary files
COPY /etc/letsencrypt/live/gpt.wx2486.me/fullchain.pem /etc/letsencrypt/live/gpt.wx2486.me/privkey.pem ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir flask

# Make port 443 available to the world outside this container
EXPOSE 443

# Run app.py when the container launches
CMD ["python", "app.py"]
