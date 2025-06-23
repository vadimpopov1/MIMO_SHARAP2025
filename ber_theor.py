import numpy as np
from generate_bits import generate_bits

def theoretical_ber_siso(SNRdB: float) -> float:
    snr_times = 10 ** (SNRdB / 10)
    ber_siso = 0.5 * (1 - np.sqrt(snr_times / (1 + snr_times)))
    return ber_siso

if __name__ == "__main__":
    num_bits = int(input('Enter count of bits: '))
    random_bit = generate_bits(num_bits)
    SNR = float(input('Enter level of noise: '))
    ber_siso = theoretical_ber_siso(SNR)
    print(ber_siso)