# Pull base image
FROM python:3


# Set environment varibles

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

# Copy project
COPY . /code/
RUN pip install -r requirements.txt
EXPOSE 8000
