import os


def get_config():
    return{
        "APP_HOST": "0.0.0.0",
        "APP_PORT": 5000,
        "APP_TITLE": "MVC",
        "APP_VERSION": "1.0",
        "SECRET": "secret",
        "MILVUS_HOST": "localhost",
        "MILVUS_PORT": "19530",
        "MILVUS_PS": 10,
        "AUTH_ERROR_STRING": 'Could not validate credentials'
    }


def get_config_environment():
    return{
        "APP_HOST": os.environ.get('APP_HOST'),
        "APP_PORT": os.environ.get('APP_PORT'),
        "APP_TITLE": os.environ.get('APP_TITLE'),
        "APP_VERSION": os.environ.get('APP_VERSION'),
        "SECRET": os.environ.get('SECRET'),
        "MILVUS_HOST": os.environ.get('MILVUS_HOST'),
        "MILVUS_PORT": os.environ.get('MILVUS_PORT'),
        "MILVUS_PS": os.environ.get('MILVUS_PS'),
        "AUTH_ERROR_STRING": os.environ.get('AUTH_ERROR_STRING'),
    }
