#!/usr/bin/env sh
gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:${APP_PORT} -w 4 app.main:app