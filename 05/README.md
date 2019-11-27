# Assignment 5
---
### 1.	Pattern recognition

In this assignment, we are asked to design a pattern recognition neural network to recognize handwriting digits (0-9). For example, the following sample represents a handwriting 9.

    00000000000000000000000000000000
    00000000000001111100000000000000
    00000000000001111100000000000000
    00000000001111111110000000000000
    00000000011111111111111000000000
    00000000011111111111111100000000
    00000000111111111111111100000000
    00000000111111111111111110000000
    00000001111111100001111110000000
    00000001111111000001111111000000
    00000001111110000001111111000000
    00000001111110000000111111000000
    00000011111100000001111110000000
    00000001111111000001111110000000
    00000001111111110001111110000000
    00000001111111111111111110000000
    00000000001111111111111110000000
    00000000001111111111111110000000
    00000000000111111111111110000000
    00000000000000111001111110000000
    00000000000000000000111111000000
    00000000000000000000111100000000
    00000000000000000000111100000000
    00000000000000000000111100000000
    00000000000000000001111110000000
    00000000000000000001111110000000
    00000000001111100001111100000000
    00000000001111111111111100000000
    00000000001111111111111100000000
    00000000011111111111111000000000
    00000000000011111111111000000000
    00000000000000001111110000000000

The data file can be downloaded from

https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits-orig.windep.Z

The data file contains 1797 instances from 43 writers. The data is prepared by NIST to extract normalized bitmaps of handwritten digits from a preprinted form.

***Task 1***: Encoding (50 pts)

Unzip the data file from the link. Encode the data into input and target files for neural network training.

***Task 2***: Neural Network Training (50 pts)

Train the neural network (pattern net) based on your input/output files. Repeat with 10, 100, and 500 hidden nodes. Report your testing, training, and validation accuracy and provide analysis.

***Bonus***: (10 pts)

Using 1024 features for neural network is very cumbersome. Is there a way to reduce the number of features? If you have an idea, show me how effective it is.

### ***Solution***

***Task 1***

After manually analyzing the dataset file each digit takes around 33 lines.

The label of the image is given on 34th line.

cleaned the data, converted the image into vector using custom imagetovec function and saved the features in input_data.csv and label as target_data.csv.

Built a Neural Network Model using keras and tensor flow for 10,100,500 nodes. Analysis and report can be found in the "hpendyal-A5-cs580.ipynb" notebook.

The notebook is having the report as well as code in it.

***Pre-reqiuisites***

  - Python 3.7
  - Download tensorflow and keras using below commands.
    
    ***Using PIP***
      - pip install tensorflow #----- install tensorflow
      - pip install keras
    
    ***Using conda***
      - conda install -c anaconda keras
