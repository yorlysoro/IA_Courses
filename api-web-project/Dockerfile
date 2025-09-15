FROM python:3.11-slim-bullseye

WORKDIR /app

# Install security updates
RUN apt-get update && apt-get upgrade -y && apt-get clean

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]