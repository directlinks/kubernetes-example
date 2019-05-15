FROM ubuntu

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN pip install -U flask && pip install -U textblob
RUN python -m textblob.download_corpora
RUN mkdir -p /example/templates

ADD templates /example/templates
ADD backend.py /example
EXPOSE 8080
CMD ["python","/example/backend.py"]
