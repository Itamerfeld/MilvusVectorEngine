from milvus import Milvus, Status
from PIL import Image
from io import BytesIO
import config
from classvector import ClassVector

config = config.get_config()


class ClassMilvus(object):
    def __init__(self):
        self.milvus = Milvus(
            config['MILVUS_HOST'], config['MILVUS_PORT'], pool_size=config['MILVUS_PS'])
        self.feat_vec = ClassVector()

    def create_collection(self, collection_name):
        status, ok = self.milvus.has_collection(collection_name)
        if not ok:
            self.milvus.create_collection(
                param={'collection_name': collection_name, 'dimension': 512})
            return 'Succesfully created'
        return 'Already exist'

    def info(self, collection_name):
        return self.milvus.get_collection_stats(collection_name)

    def drop_collection(self, collection_name):
        return self.milvus.drop_collection(collection_name)

    def insert(self, collection_name, file):
        image = [Image.open(BytesIO(file))]
        vectors = [self.feat_vec.normalize(i).tolist() for i in image]
        self.milvus.insert(collection_name=collection_name, records=vectors)
        return self.milvus.flush([collection_name])

    def search(self, collection_name, file):
        results_list = []
        image = [Image.open(BytesIO(file))]
        vectors = [self.feat_vec.normalize(i).tolist() for i in image]
        status, results = self.milvus.search(**{
            'collection_name': collection_name,
            'query_records': [vectors[0]],
            'top_k': 10,
            'params': {
                "nprobe": 16
            },
        })
        if status.OK():
            for obj in results:
                for n in obj:
                    results_list.append({"id": n.id, "distance": n.distance})
            return results_list
