import numpy as np

def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    mini = np.min(x)
    maxi = np.max(x)

    # x = np.array(x)
    # x = (x - mini)/(maxi - mini)
    res = [ (v - mini)/(maxi - mini) for v in x]
    return res