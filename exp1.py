import pandas as pd

def find_s_algorithm(data):
    # Initialize hypothesis with the first positive instance
    for i, row in data.iterrows():
        if row[-1] == 'Yes':  # Assuming 'Yes' is for positive instances
            hypothesis = row[:-1].tolist()
            break
    
    # Iterate over all instances to refine the hypothesis
    for i, row in data.iterrows():
        if row[-1] == 'Yes':
            for j in range(len(hypothesis)):
                if hypothesis[j] != row[j]:
                    hypothesis[j] = '?'
    
    return hypothesis

# Load data from CSV
data = pd.read_csv("data.csv")
hypothesis = find_s_algorithm(data)
print("Most specific hypothesis:", hypothesis)
