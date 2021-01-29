# Milvus x FastAPI x React 
*Using milvus engine to perform vector similarity search.*

### Milvus CPU container
```bash
sudo docker run -d --name milvus \
-p 19530:19530 \
-p 19121:19121 \
-v /Users/korenhamra/Documents/Milvus/milvus/db:/var/lib/milvus/db \
-v /Users/korenhamra/Documents/Milvus/milvus/conf:/var/lib/milvus/conf \
-v /Users/korenhamra/Documents/Milvus/milvus/logs:/var/lib/milvus/logs \
-v /Users/korenhamra/Documents/Milvus/milvus/wal:/var/lib/milvus/wal \
milvusdb/milvus:0.9.1-cpu-d052920-e04ed5
```

### Dependencies

```bash 
pip install pymilvus==0.2.12 fastapi
conda install --quiet --yes pytorch torchvision -c pytorch

cd client 
npm install
```

### Run Server

```bash
python server.py
```

### Run Client

```bash
npm start
```