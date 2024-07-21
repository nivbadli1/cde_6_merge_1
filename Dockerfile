FROM ubuntu:22.04
WORKDIR /app
COPY script.sh .
RUN chmod +x script.sh
ENTRYPOINT ["/app/script.sh"]