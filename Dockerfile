FROM python:3.8-alpine

WORKDIR /python-docker

COPY req.txt req.txt

RUN pip3 install -r req.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD ["server.py" ]
