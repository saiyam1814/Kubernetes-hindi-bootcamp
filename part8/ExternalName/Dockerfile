FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Add files
ADD app.py /app/
ADD requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]
