import numpy as np
if __name__ == "__main__":
    persontype = np.dtype({
        'names':['name', 'age', 'chinese', 'math', 'english'],
        'formats':['S32','i', 'i', 'i', 'f']})
    peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
        ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
        dtype=persontype)
    ages = peoples[:]['age']
    chineses = peoples[:]['chinese']
    maths = peoples[:]['math']
    englishs = peoples[:]['english']
    
    pass