FROM python:3 AS api-base

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install "uvicorn[standard]"

FROM api-base AS api-image
WORKDIR /usr/src/app
COPY . .
