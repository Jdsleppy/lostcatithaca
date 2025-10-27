#!/usr/bin/env bash
 
set -euo pipefail
 
ssh personal 'cd /apps/lostcatithaca && \
    git fetch && \
    git reset --hard origin/main && \
    docker compose build && \
    docker compose up -d --remove-orphans && \
    docker compose logs -f'
