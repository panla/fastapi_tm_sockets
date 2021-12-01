#!/bin/bash

uvicorn server:app --host 0.0.0.0 --port 8000 --workers 2 --http httptools --loop uvloop --reload
