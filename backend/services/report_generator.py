def generate_report(metrics):
    precision = metrics.get("precision", 0)
    recall = metrics.get("recall", 0)
    f1_score = metrics.get("f1_score", 0)

    if f1_score >= 0.85:
        overall = "The model is performing well overall."
    elif f1_score >= 0.65:
        overall = "The model has acceptable performance but still needs improvement."
    else:
        overall = "The model performance is weak and should be improved before production use."

    if precision < recall:
        issue = "Precision is lower than recall, which suggests the model may be producing too many false positives."
    elif recall < precision:
        issue = "Recall is lower than precision, which suggests the model may be missing some positive cases."
    else:
        issue = "Precision and recall are balanced."

    return f"{overall} {issue} The current F1-score is {f1_score}."
