# CSC490 Capstone Project Repo - Cataract surgery segmentation using Transformers

## Dataset

CaDIS: a Cataract Dataset for Image Segmentation is a dataset for semantic segmentation created by Digital Surgery Ltd. on top of the CATARACTS dataset. CaDIS consists of 4670 images sampled from the 25 videos on CATARACTS' training set. Each pixel in each image is labeled with its respective instrument or anatomical class from a set of 36 identified classes. More details about the dataset could be found in the paper (https://arxiv.org/pdf/1906.11586.pdf).

The dataset consists of 4670 images in total and includes 36 classes: 29 surgical instrument classes, 4 anatomy classes and 3 classes of other object appearing in the scene. The following table gives an overview of the classes included in the dataset with their respective class ID per category.  The training, validation and test sets contain 3550, 534 (Videos 5, 7 and 16) and 586 (Videos 2, 12 and 22) images respectively.

![Dataset Tools Image](https://user-images.githubusercontent.com/76748797/206267246-50f9de15-7c9c-44c9-a72d-40cbadca9c65.png)

Reference: https://cataracts.grand-challenge.org/CaDIS/


## SOTA method
Pissas et al [1] proposed a publicly available state-of-the-art approach for the CaDis dataset, which uses ResNet50 as the backbone and OCRNet by Yuan et al. [2] as the head, while we seek to make improvement based on their method.

![OCRNet](https://github.com/HRNet/HRNet-Semantic-Segmentation/blob/HRNet-OCR/figures/OCR.PNG)


## Data augmentation
### SOTA method data augmentation
The original augmentation method used by the SOTA method is applying “Pad”, “Flip”, “GaussianBlur” and “ColorJitter” in a sequential order.

### TrivialAugment
Our method uses a new augmentation method called TrivialAugment [3]. It randomly selects one augmentation method from the set and apply to one image with random strength.

![TrivialAugment example](https://user-images.githubusercontent.com/76748797/206269730-c9b17c07-2e63-4af9-8517-b32ee8fd6f94.png)

## Loss function
### Lovász-Softmax loss
Lovász-Softmax loss is a method for direct optimization of the mIoU loss in the context of semantic image segmentation, based on the convex Lovász extension of submodular losses.


## Methods
### Segformer
- SegFormer is a simple, efficient and powerful semantic segmentation framework proposed by Xie et al. [4], which unifies Transformers with a lightweight MLP decoder.
- Utilizes a novel hierarchically structured Transformer encoder without the need for positional encoding.
- Avoids complex decoding by using an MLP decoder that can aggregate multi-level features from different layers.

![Segformer](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/segformer_architecture.png)

### Repeat Factor Sampling
- Repeated factor sampling is a sampling method for alleviating the long-tailed class distribution, i.e., data imbalance issue, proposed by Gupta et al. [5] from FAIR.
- In brief, this sampling technique has a class-level repeat factor as $r_c = max(1,\sqrt{t \over f_c})$ where $f_c$ is the frequency of image-level occurrence of the class and t is a hyper-parameter.
- Then the number of times repeated for an image during one epoch is defined as 𝑟𝑖 = 𝑚𝑎𝑥𝑐∈𝐼 𝑟𝑐 for each image 𝑖.
- In addition to the repetition factor of 0.15 used in the original SOTA, we used a repetition factor of 0.2 and used it on the new model.

## Result
We implemented the model with the original method by Pissas et al. [1] as well as our improved model, where we also tried 2 different data augmentation methods.

![Segmentation result](https://user-images.githubusercontent.com/76748797/206273552-6e3cdad3-e014-434b-92cc-a40ef50cd5ac.png)

| Architecture  | Data Augmentation | mIoU (All classes) | mIoU (Anatomy) | mIoU (Instruments) | mIoU (Others) |
| --- | --- | --- | --- | --- | --- |
| ResNet+OCRNet | Original | 0.748 | **0.860** | 0.759 | 0.716 |
| Ours | Original | **0.755** | 0.859 | 0.771 | 0.749 |
| Ours | Trivial | 0.752 | 0.850 | **0.773** | **0.751** |

## Reference
[1] Pissas, C. (2021). Effective Semantic Segmentation in Cataract Surgery: What Matters Most?. In Medical Image Computing and Computer Assisted Intervention – MICCAI 2021 (pp. 509–518). Springer International Publishing.

[2] Yuhui Yuan, Xiaokang Chen, Xilin Chen, Jingdong Wang(2019), Segmentation Transformer: Object-Contextual Representations for Semantic Segmentation

[3] Samuel G. Müller, Frank Hutter(2021), TrivialAugment: Tuning-free Yet State-of-the-Art Data Augmentation

[4] Enze Xie, Wenhai Wang, Zhiding Yu, Anima Anandkumar, Jose M. Alvarez, & Ping Luo (2021). SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers. CoRR, abs/2105.15203.

[5] Agrim Gupta, Piotr Dollár, & Ross B. Girshick (2019). LVIS: A Dataset for Large Vocabulary Instance Segmentation. CoRR, abs/1908.03195.
