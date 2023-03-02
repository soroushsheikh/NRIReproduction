# Unofficial Implementation of Neural Relational Inference for Interacting Systems

This is an unofficial implementation of the Neural Relational Inference (NRI) model for learning representations of interacting systems using neural networks and relational reasoning. The original model is described in the paper "Neural Relational Inference for Interacting Systems" by Kipf et al.

## Overview

We have reproduced the results of the original paper using Pytorch, and analyzed the model's performance on more general datasets. Our findings show that the methodology does not generalize well to problems involving conventional trajectories and is only useful for specific cases like repetitive phenomena. 

Additionally, we found that the method is not easily scalable and requires a significant amount of resources for training. We were only able to perform the method on at most 5 particles to achieve consistent results. Therefore, it is not possible to perform the method on rich datasets such as pedestrians in the city or vehicle traffic with our current infrastructure.

Full report is available [here](https://github.com/soroushsheikh/NRIReproduction/blob/main/NRI%20final%20report.pdf "Final Report")

## Requirements

- Pytorch 0.2 (0.3 breaks simulation decoder)
- Python 2.7 or 3.6

## Data Generation

To replicate the experiments on simulated physical data, generate training, validation, and test data by running:

```
cd data
python generate_dataset.py
```
This generates the springs dataset. Use `--simulation charged` for charged particles.

## Training

To train the NRI model on the springs dataset, run:

```
python train.py
```


You can specify a different dataset by modifying the `suffix` argument. For example, `--suffix charged5` will run the model on the charged particle simulation with 5 particles (if it has been generated).

To train the encoder or decoder separately, run:

```
python train_enc.py
```


You can specify a different dataset by modifying the `suffix` argument. For example, `--suffix charged5` will run the model on the charged particle simulation with 5 particles (if it has been generated).

To train the encoder or decoder separately, run:

```
python train_enc.py
```

or

```
python train_dec.py
```


respectively. We provide a number of training options which are documented in the respective training files.

## Disclaimer

This implementation is not an official implementation of the Neural Relational Inference (NRI) model, and is provided for educational purposes only. We do not claim any ownership of the original model, only synthetic dataset is added by us.

