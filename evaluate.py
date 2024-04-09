import os
import pandas
import numpy as np
from sklearn.metrics import r2_score


def compute_r2_score(values_a, values_b):
    r2_scores = []
    
    subset_a = []
    subset_b = []

    for j in range(len(values_a)):
        if values_a[j] != None and values_b[j] != None:
            subset_a.append(values_a[j])
            subset_b.append(values_b[j])

    r2 = r2_score(subset_a, subset_b)

    return r2

# Read values from text files A and B
with open('prepare_output.txt', 'r') as file_prepare:
    values_prepare = [float(value.strip()) for value in file_prepare.readlines()]

with open('process_output.txt', 'r') as file_process:
    values_process = [float(value.strip()) for value in file_process.readlines()]


# Compute R2 scores
r2 = compute_r2_score(values_prepare, values_process)
print("R2 score : ", r2)