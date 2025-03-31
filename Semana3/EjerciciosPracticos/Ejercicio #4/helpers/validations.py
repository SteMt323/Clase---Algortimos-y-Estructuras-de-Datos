def int_evaluation(num):
    if num is None:
        return True
    return isinstance(num, int)
    
def float_evaluation(num):
    if num is None:
        return True
    return isinstance(num, float)
