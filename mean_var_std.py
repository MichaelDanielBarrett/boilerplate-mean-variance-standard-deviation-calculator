import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    else:
        

        mtrx = np.array([
            list[:3],
            list[3:6],
            list[6:]
        ])

        calculations = dict()
        calculations['mean'] = [
            mtrx.mean(axis=0).tolist(),
            mtrx.mean(axis=1).tolist(),
            mtrx.mean()
        ]
        calculations['variance'] = [
            mtrx.var(axis=0).tolist(),
            mtrx.var(axis=1).tolist(),
            mtrx.var()
        ]
        calculations['standard deviation'] = [
            mtrx.std(axis=0).tolist(),
            mtrx.std(axis=1).tolist(),
            mtrx.std()
        ]
        calculations['max'] = [
            mtrx.max(axis=0).tolist(),
            mtrx.max(axis=1).tolist(),
            mtrx.max()
        ]
        calculations['min'] = [
            mtrx.min(axis=0).tolist(),
            mtrx.min(axis=1).tolist(),
            mtrx.min()
        ]
        calculations['sum'] = [
            mtrx.sum(axis=0).tolist(),
            mtrx.sum(axis=1).tolist(),
            mtrx.sum()
        ]

        return calculations
