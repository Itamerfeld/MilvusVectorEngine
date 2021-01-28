from milvus import Milvus, IndexType, MetricType, Status
import torch.nn as nn
import torchvision.models as models
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from torch.autograd import Variable
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import torch


class ClassVector(object):
    def __init__(self):
        self.model = models.resnet18(pretrained=True)
        self.model.eval()
        self.layer = self.model._modules.get("avgpool")
        self.cos = nn.CosineSimilarity(dim=1, eps=1e-6)
        self.transform_pipeline = transforms.Compose([transforms.Resize((224, 224)),
                                                      transforms.ToTensor(),
                                                      transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                                           std=[0.229, 0.224, 0.225])])

    def normalize(self, img):
        t_img = Variable(self.transform_pipeline(img)).unsqueeze(0)
        feat_vec = torch.zeros(512)

        def copy_data(m, i, o):
            feat_vec.copy_(o.data.squeeze())

        h = self.layer.register_forward_hook(copy_data)
        self.model(t_img)
        h.remove()

        return feat_vec


feat_vec = ClassVector()
milvus = Milvus('localhost', '19530', pool_size=10)
collection_name = 'koren_example'
images = [
    Image.open('./images/test1.jpg'),
    Image.open('./images/test2.jpg'),
    Image.open('./images/test3.jpg'),
]

vectors = [feat_vec.normalize(i).tolist() for i in images]

milvus.create_collection(
    param={'collection_name': collection_name, 'dimension': 512})

milvus.insert(collection_name=collection_name, records=vectors)
milvus.flush([collection_name])

status, results = milvus.search(**{
    'collection_name': collection_name,
    'query_records': [vectors[0]],
    'top_k': 10,
    'params': {
        "nprobe": 16
    },
})
if status.OK():
    print(results)

milvus.drop_collection(collection_name)
