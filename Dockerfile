FROM caddy:2.10.2
WORKDIR /app
COPY freeze/ .
COPY Caddyfile .
ENTRYPOINT [ "caddy" ]
CMD [ "run" ]
