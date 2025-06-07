import numpy as np

def topsis_rank(matrix, weights, impacts):
    norm_matrix = matrix / np.sqrt((matrix**2).sum())
    weighted = norm_matrix * weights
    ideal_best = np.where(np.array(impacts) == '+', weighted.max(), weighted.min())
    ideal_worst = np.where(np.array(impacts) == '+', weighted.min(), weighted.max())

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))
    scores = dist_worst / (dist_best + dist_worst)
    ranks = scores.rank(ascending=False)
    return ranks
