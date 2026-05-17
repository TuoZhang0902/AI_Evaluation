def safe_divide(numerator, denominator):
    if denominator == 0:
        return 0.0
    return numerator / denominator


def calculate_metrics(true_positive, false_positive, false_negative, true_negative):
    tp = true_positive
    fp = false_positive
    fn = false_negative
    tn = true_negative

    precision = safe_divide(tp, tp + fp)
    recall = safe_divide(tp, tp + fn)
    f1_score = safe_divide(2 * precision * recall, precision + recall)
    accuracy = safe_divide(tp + tn, tp + fp + fn + tn)

    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1_score": round(f1_score, 4),
        "accuracy": round(accuracy, 4),
    }
