# README

Socket.IO module

## ENV

- Python 3.8.12
- Cython
- FastAPI
- python-socketio

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
docker-compose.yaml
conf/
    sockets/
        product.local.toml
ftm_sockets/
    conf/
        product.local.toml
        test.local.toml
logs/
    sockets/
```
