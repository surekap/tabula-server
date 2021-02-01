FROM python:3

WORKDIR /app

RUN apt -y update \
&& apt -y install openjdk-11-jre-headless

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app

EXPOSE 8000

ENTRYPOINT ["./run.sh"]