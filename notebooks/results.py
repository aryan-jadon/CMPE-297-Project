import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

results = pd.read_csv("Results.csv")
print(classification_report(results["actuals"],
                            results["predictions"]))