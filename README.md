# README

Socket.IO module

## ENV

- Python 3.9
- Cython
- FastAPI
- python-socketio

## tags

- *asyncio*
- *fastapi* <https://github.com/tiangolo/fastapi>
- *socket.io* <https://github.com/miguelgrinberg/python-socketio>
- *websockets*

## 配置文件

```text
# the config for product env, refer to conf/product.toml
conf/product.local.toml

# the config for test env, refer to conf/test.toml, use CODE_ENV=tes
conf/test.local.toml

# the run shell scripts in container
docker-entrypoint.sh
```

```text
.
├── fastapi_tm_sockets
├── conf
│   └── fastapi_tm_sockets
│       └── product.local.toml
├── docker-compose.yml
└── logs
    └── fastapi_tm_sockets
        ├── x.log
        └── x-test.log
```
