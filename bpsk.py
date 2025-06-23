import numpy as np
from generate_bits import generate_bits

def bpsk_modulate(bits: np.ndarray) -> np.ndarray:
    array = []
    for i in range(len(bits)):
        array.append(np.where(bits[i] == 0, 1, -1))
    return array

def bpsk_demodulate(bits: np.ndarray) -> np.ndarray:
    array = []
    for i in range(len(bits)):
        array.append(np.where(bits[i] < 0, 1, 0))
    return array

if __name__ == "__main__":
    num_bits = int(input('Enter count of bits: '))
    random_bit = generate_bits(num_bits)
    print(f"Generated bit: " + " ".join(map(str, random_bit)))
    mod = bpsk_modulate(random_bit)
    print(f"Modulated bit: " + " ".join(map(str, mod)))
    print(f"Demodulated bit: " + " ".join(map(str, bpsk_demodulate(mod))))
