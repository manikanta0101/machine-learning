import pandas as pd

def candidate_elimination(data):
    specific_hypothesis = ['∅'] * (len(data.columns) - 1)
    general_hypothesis = [['?'] * (len(data.columns) - 1)]
    
    for i, row in data.iterrows():
        if row[-1] == 'Yes':
            for j in range(len(specific_hypothesis)):
                if specific_hypothesis[j] == '∅':
                    specific_hypothesis[j] = row[j]
                elif specific_hypothesis[j] != row[j]:
                    specific_hypothesis[j] = '?'
            
            general_hypothesis = [g for g in general_hypothesis if consistent(g, row[:-1])]
        else:
            new_general_hypothesis = []
            for g in general_hypothesis:
                for j in range(len(g)):
                    if g[j] == '?':
                        temp = g.copy()
                        temp[j] = specific_hypothesis[j]
                        new_general_hypothesis.append(temp)
            general_hypothesis = new_general_hypothesis

    return specific_hypothesis, general_hypothesis

def consistent(hypothesis, instance):
    return all(h == '?' or h == i for h, i in zip(hypothesis, instance))

# Load data from CSV
data = pd.read_csv("data.csv")
S, G = candidate_elimination(data)
print("Specific Hypothesis:", S)
print("General Hypothesis:", G)
