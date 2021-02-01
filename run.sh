#!/bin/sh
gunicorn --chdir . --workers 2 --threads 2 -b 0.0.0.0:8000 app:app