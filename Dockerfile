# 1. Base image with Python
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency file & install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the project
COPY . .

# 5. Expose the Flask port
EXPOSE 5000

# 6. Command to run the app
CMD ["python", "app.py"]
