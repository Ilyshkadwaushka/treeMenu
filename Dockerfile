FROM python:3.10.5

EXPOSE 8000

SHELL ["/bin/bash", "-c"]

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir app
WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip &&  \
    apt update &&  \
    useradd -rms /bin/bash user  \
    && chmod 777 /opt /run &&  \
    pip install -r requirements.txt

COPY . .