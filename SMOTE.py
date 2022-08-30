from imblearn.over_sampling import SMOTE

over = SMOTE(sampling_strategy=1.00)

X, y = over.fit_resample(X, y)
