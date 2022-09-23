# ChangeLog

[toc]

## 0.2

### 0.2.4

- update/optimize
  - update log config

- deploy
  - update Dockerfile remove install gcc

- requirements
  - upgrade fastapi from 0.78.0 to 0.85.0
  - upgrade httptools from 0.4.0 to 0.5.0
  - upgrade pydantic from 1.9.1 to 1.10.2
  - upgrade starlette from 0.19.1 to 0.20.4
  - upgrade uvicorn from 0.18.2 to 0.18.3
  - upgrade uvloop from 0.16.0 to 0.17.0
  - upgrade upython-engineio from 4.3.2 to 4.3.4
  - upgrade upython-socketio from 5.6.0 to 5.7.1

### 0.2.3

update/optimize

- upgrade image from python:3.9-slim-buster to python:3.9-slim-bullseye

### 0.2.2

require packages

- upgrade requirement
  - fastapi==0.78.0
  - Cython==0.29.30
  - pytomlpp==1.0.11
  - python-engineio==4.3.2
  - python-socketio==5.6.0
  - websockets==10.3

### 0.2.1

require packages

- upgrade requirement
  - fastapi==0.75.0
  - uvicorn==0.17.6

### 0.2.0

require packages

- upgrade requirement
  - Cython==0.29.28
  - fastapi==0.74.1
  - httptools==0.4.0
  - loguru==0.6.0
  - python-socketio==5.5.2
  - uvicorn==0.17.5

### 0.1.0

require package

- upgrade
  - Cython==0.29.26
  - fastapi==0.72.0
  - uvicorn==0.17.0
  - pytomlpp==1.0.10
  - pydantic==1.9.0

update/optimize

- update config
- update response schema, error schema, exception, middleware, extensions
