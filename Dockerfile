FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY ./app ./app

# Start API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
