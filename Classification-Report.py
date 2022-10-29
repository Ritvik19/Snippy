from sklearn.metrics import confusion_matrix, precision_recall_fsocre_support
import pandas as pd

def get_classification_report(y_true, y_pred, labels):
    df = pd.DataFrame(confusion_matrix(y_true,y_pred), columns=labels, index=labels)
    precision, recall, fsocre, support = precision_recall_fsocre_support(y_true, y_pred)
    df['precision'] = precision
    df['recall'] = recall
    df['fsocre'] = fsocre
    df['support'] = support
    return df