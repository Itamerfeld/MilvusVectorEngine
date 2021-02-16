from fastapi import FastAPI, File, Form, Security, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.api_key import APIKeyQuery, APIKey
from starlette.status import HTTP_403_FORBIDDEN
import uvicorn
from classmilvus import ClassMilvus
import config

config = config.get_config()
app = FastAPI(title=config['APP_TITLE'], version=config['APP_VERSION'])
app.add_middleware(CORSMiddleware, allow_origins=[
                   '*'], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
milvus_utils = ClassMilvus()


async def get_api_key(api_key_query: str = Security(APIKeyQuery(name='key', auto_error=False))):
    if api_key_query == config['SECRET']:
        return api_key_query
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN,
                            detail="Could not validate credentials")


@app.get('/create_collection/{collection_name}')
async def create_collection(collection_name, api_key: APIKey = Depends(get_api_key)):
    return {"status": milvus_utils.create_collection(collection_name)}


@app.get('/drop_collection/{collection_name}')
async def drop_collection(collection_name, api_key: APIKey = Depends(get_api_key)):
    return {"status": milvus_utils.drop_collection(collection_name).message}


@app.get('/info_collection/{collection_name}')
async def info_collection(collection_name, api_key: APIKey = Depends(get_api_key)):
    return {"status": milvus_utils.info(collection_name)}


@app.post('/insert_collection/')
async def insert_collection(file: bytes = File(...), collection_name: str = Form(...), api_key: APIKey = Depends(get_api_key)):
    return {"status": milvus_utils.insert(collection_name, file).message}


@app.post('/search_collection/')
async def search_collection(file: bytes = File(...), collection_name: str = Form(...), api_key: APIKey = Depends(get_api_key)):
    return {"result": milvus_utils.search(collection_name, file)}

uvicorn.run(app, host=config['APP_HOST'], port=config['APP_PORT'])
