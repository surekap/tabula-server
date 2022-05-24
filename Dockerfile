FROM python:3

WORKDIR /app

RUN apt -y update \
&& apt -y install openjdk-11-jre-headless

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app

EXPOSE 8000
ENV VIRTUAL_HOST=tabula.hartex.in
ENV VIRTUAL_PORT=8000
ENV LETSENCRYPT_HOST=tabula.hartex.in
ENV LETSENCRYPT_EMAIL=surekap@gmail.com
ENTRYPOINT ["./run.sh"]
