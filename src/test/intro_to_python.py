import numpy as np


if __name__ == "__main__":
    matrix1 = np.identity(3).astype("int32")
    matrix2 = np.where(matrix1 == 1,matrix1,3)
    matrix3 = matrix2[:,:2]

    print(matrix1)
    print()
    print(matrix2)
    print()
    print(matrix3)