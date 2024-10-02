FROM caddy:2 AS caddy
WORKDIR /app
COPY freeze/ .
COPY Caddyfile .
ENTRYPOINT [ "caddy" ]
CMD [ "run" ]
