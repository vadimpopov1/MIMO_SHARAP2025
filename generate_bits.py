import numpy as np

def generate_bits(num_bits: int) -> np.ndarray:
    array = []
    for i in range(num_bits):
        array.append(np.random.randint(0, 2))
    return array

def calculate_ber(original: np.ndarray, received: np.ndarray) -> float:
    berSum = 0
    for bit in range(len(original)):
        if original[bit] != received[bit]:
            berSum += 1
    numTrials = len(original)
    ber = berSum / numTrials
    return ber

if __name__ == "__main__":
    num_bits = int(input('Enter count of bits: '))
    random_bit = generate_bits(num_bits)
    print(f"Generated bit: " + " ".join(map(str, random_bit)))
    print(f"BER: {calculate_ber(random_bit, random_bit)}")