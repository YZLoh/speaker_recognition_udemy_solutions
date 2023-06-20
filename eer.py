'''
Equal error rate (EER) in Python
Given a list of cosine similarity scores on positive and negative trial pairs, can you compute the Equal Error Rate?

We will provide a CSV file. Each line of this CSV file is:

label,score

If label is 0, it is a negative trial; if label is 1, it is a positive trial.

The score is cosine similarity score of this trial.

Hint: You may want to follow these steps:

Parse the CSV file using the csv module;

Sweep through many threshold, and for each threshold, compute the FAR and FRR;

Find the threshold where the delta between FAR and FRR is minimal. The compute EER=(FAR+FRR)/2.
'''

import csv

SCORES = 'scores.csv'

def ComputeEER():
    """Compute the Equal Error Rate from the data in scores.csv
    
    Returns:
        a floating point number for the equal error rate (between 0 and 1)
    """
    labels = []
    scores = []
    with open(SCORES) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            labels.append(int(row[0]))
            scores.append(float(row[1]))

    # Add your code here
    # Sort scores and labels in descending order
    sorted_scores, sorted_labels = zip(*sorted(zip(scores, labels), reverse=True))

    total_positive = sum(sorted_labels)
    total_negative = len(sorted_labels) - total_positive

    false_positive = 0
    false_negative = total_positive

    eer = None  # Initialize EER

    for i in range(len(sorted_scores)):
        if sorted_labels[i] == 0:
            false_positive += 1
        else:
            false_negative -= 1

        current_fpr = false_positive / total_negative
        current_fnr = false_negative / total_positive

        if current_fnr <= current_fpr:
            eer = current_fpr
            break

    if eer is None:
        eer = current_fpr

    return eer