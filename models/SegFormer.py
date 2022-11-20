import torch
from torch import nn
from torch.nn import functional as F
from utils.utils import CLASS_INFO
from torchvision.models._utils import IntermediateLayerGetter
from models.Projector import Projector
from transformers import AutoFeatureExtractor, AutoModelForSemanticSegmentation
from utils.defaults import  classes_exp0, classes_exp1, classes_exp2, classes_exp3

class SegFormer(nn.Module):

    def __init__(self, config, experiment, device):
        super().__init__()

        self.config = config
        self.device = device
        self.num_classes = len(CLASS_INFO[experiment][1]) - 1 if 255 in CLASS_INFO[experiment][1].keys() \
            else len(CLASS_INFO[experiment][1])
        # chop off fully connected layers from the backbone + load pre-trained weights
        # we replace stride with dilation in resnet layer4 to make output_stride = 8 (instead of 32)
        task_map = {1: classes_exp1, 2: classes_exp2, 3: classes_exp3}
        current_map = task_map[experiment]
        self.feature_extractor = AutoFeatureExtractor.from_pretrained("nvidia/mit-b0", reduce_labels=True)
        self.model = AutoModelForSemanticSegmentation.from_pretrained("nvidia/mit-b0", id2label={i: j for i, j in current_map.items() if i != 0}, label2id={i: j for j, i in current_map.items() if j != 0})
        self.model =  self.model.to(device)
        self.projector_model = None

    def forward(self, x):
        lst = []
        for i in range(len(x)):
            lst.append(x[i, ...].cpu())
        encoding = self.feature_extractor(lst, return_tensors="pt").to(self.device)
        outputs = self.model(**encoding)
        return nn.functional.interpolate(
            outputs.logits,
            size=[544, 960],
            mode="bilinear",
            align_corners=False,
        )


if __name__ == '__main__':
    config = dict()
    import pathlib
    a = torch.ones(size=(1, 3, 540, 960))

    model = SegFormer(config, 2)
    # model.print_params()
    b = model.forward(a)
    print(b.shape)
