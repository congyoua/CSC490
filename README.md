# CSC490 Capstone Project Repo

The dataset consists of 50 videos of cataract surgeries performed in Brest University Hospital. 

Patients were 61 years old on average (minimum: 23,maximum: 83,standard deviation: 10). Each surgery was recorded in two videos: the microscope video and the surgical tray video. The frame definition was 1920x1080 pixels (full HD resolution) for both types of videos. The frame rate was approximately 30 frames per second for the tool-tissue interaction videos and 50 frames per second for the surgical tray videos. Microscope videos had a duration of 10 minutes and 56 s on average (minimum: 6 minutes 23 s, maximum: 40 minutes 34 s, standard deviation:6 minutes 5 s).

Surgical tray videos had a duration of 11 minutes and 3 s on average (minimum: 6 minutes 30 s, maximum: 40 minutes 48 s, standard deviation: 6 minutes 3 s). 

In total, more than nine hours of surgery (for each video type) have been video recorded. For more details about the dataset and the different tasks proposed. For CATARACTS 2018, in addition to the videos, we provide the images (images.zip) used in the challenge and the ground truth.

Reference: https://ieee-dataport.org/open-access/cataracts



# Presentation steps

1. Data
    - Background
    - CADIS Dataset(image sampled from cataract surgery with segmentation) 
    - Data sample
      - Original img, segmented img
    - Classes
      - anatomical, instrument, others
2. Model
    - Model we are using
      - Encoder - Decoder
    - Data preprocessing : transformations (fenda)
    - Model they have and performance
    - Loss function
    - Current update: CEL-Dice
      - Performance
    - Our trained result 
      - DLV3, OCR, OCR + CEL-Dice
      - Accuracy table
      - Confusion matrix (zijin liao)
      - What's the problem with current method?
3. Next step:
   - Change decoder
   - Change backbone
   - Focus on the class with not enough label
- 
   


# Current steps


## 1. FWIoU
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9871673

## 2. CEL-Dice
https://arxiv.org/pdf/1909.10360v3.pdf

## 3. New model - RAUNet
https://github.com/nizhenliang/RAUNet