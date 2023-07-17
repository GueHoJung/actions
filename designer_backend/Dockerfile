FROM python:3.9

# Configure python
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

ARG REQUIREMENT='requirements.txt'

RUN apt-get -y update && apt-get -y install vim && apt-get clean
RUN mkdir /backend_server
ADD . /backend_server

WORKDIR /backend_server

# get packages
COPY ./designer_backend/$REQUIREMENT $REQUIREMENT
RUN pip install --upgrade pip
# RUN pip install --upgrade django-rest-framework
RUN pip install --no-cache-dir -r ./$REQUIREMENT



COPY . /backend_server

# EXPOSE 8080 <= docker-compose.yml 에서 설정

# CMD ["python", "src/main.py"]
