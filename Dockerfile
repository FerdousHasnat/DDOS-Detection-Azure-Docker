# Use the base Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY score.py /app
COPY random_forest_ddos_model.pkl /app

# Ensure the model file has proper permissions
RUN chmod +r /app/random_forest_ddos_model.pkl

# Expose the port Flask will run on
EXPOSE 5000

# Run the Flask application
CMD ["python", "/app/score.py"]
