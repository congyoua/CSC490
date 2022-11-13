import torch
import torch.nn as nn
import monai.losses

class MonaiDiceFocalLoss(monai.losses.FocalLoss):
    def __init__(self, config, **args):
        super(MonaiDiceFocalLoss, self).__init__(to_onehot_y=False)
        self.config = config

