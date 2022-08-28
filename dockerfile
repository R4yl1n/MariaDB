FROM Python:3

WORKDIR /usr/src/app

COPY ./Flask .
RUN pip install Flask

RUN go build -v -o /usr/local/bin/app ./...

CMD ["Python3", "-m", "flask", "run","--host=0.0.0.0"]