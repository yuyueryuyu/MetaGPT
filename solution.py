def rank_elements_by_threshold(values, threshold):
    above_threshold = [x for x in values if x > threshold]
    below_threshold = [x for x in values if x <= threshold]
    above_threshold.sort(reverse=True)
    below_threshold.sort()
    return above_threshold + below_threshold