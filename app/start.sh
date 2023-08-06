#!/usr/bin/env sh
gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 -w 4 app.main:app