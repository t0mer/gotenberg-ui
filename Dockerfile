FROM techblog/fastapi:latest

LABEL maintainer="tomer.klein@gmail.com"

ENV GOTENBERG_API_ADDRESS=""

RUN mkdir -p /opt/gotenbergui

COPY gotenbergui /opt/gotenbergui

WORKDIR /opt/gotenbergui

EXPOSE 8080

ENTRYPOINT ["/usr/bin/python3", "gotenberg.py"]
