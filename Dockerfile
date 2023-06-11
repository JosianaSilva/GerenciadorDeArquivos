# Use the alpine base image
FROM alpine

# Set the working directory
WORKDIR /home/app

# Copy the project files to the container
COPY . /home/app

# Install Python and pip
RUN apk add --no-cache python3 py3-pip

# Install the project dependencies
RUN pip3 install -r /home/app/requirements.txt

# Set the default command to run the application
CMD ["python3", "/home/app/source/app.py"]
# CMD ["sh"]
