from fastapi import FastAPI, File
import uvicorn
import milvus_utils

app = FastAPI()


@app.get('/create_collection/{collection_name}')
async def create_collection(collection_name):
    return {"status": milvus_utils.create_collection(collection_name)}


@app.get('/drop_collection/{collection_name}')
async def drop_collection(collection_name):
    return {"status": milvus_utils.drop_collection(collection_name).message}


@app.post('/insert_collection/')
async def insert_collection(file: bytes = File(...), collection_name: str = 'collection_name'):
    return {"status": milvus_utils.insert(collection_name, file).message}


@app.post('/search_collection/')
async def search_collection(file: bytes = File(...), collection_name: str = 'collection_name'):
    return {"result": milvus_utils.search(collection_name, file)}

uvicorn.run(app, host='0.0.0.0', port=5000)
