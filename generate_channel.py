import numpy as np

def generate_channel_gain() -> complex:
    std_dev = 1.0 / (2 ** 0.5)
    real = np.random.normal(0, std_dev)
    imag = np.random.normal(0, std_dev)
    return complex(real, imag)

def generate_channel_matrix():
    matrix_size = (2, 2)
    matrix = np.empty(matrix_size, dtype=complex)
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            matrix[i, j] = generate_channel_gain()
    return matrix

if __name__ == "__main__":
    print(generate_channel_matrix())
