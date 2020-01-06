FROM ubuntu:18.04

RUN apt-get update -y \
&& apt-get install -y python3.6 \
&& apt-get install -y python3-pip \
&& apt-get install -y wget \
&& apt-get install -y locales \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* \
&& cd /usr/local/bin \
&& ln -s /usr/bin/python3 python \
&& pip3 install --upgrade pip

# locale setting
RUN locale-gen en_US.UTF-8
ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    PYTHONIOENCODING=utf-8

STOPSIGNAL SIGINT
WORKDIR /home/test
COPY . /home/test/
RUN chmod +x start.sh
ENTRYPOINT ["./start.sh"]
#ENTRYPOINT ["python", "-u", "main.py"]
#CMD ["/usr/local/bin/python -u main.py"]
