import numpy as np
from generate_bits import generate_bits
from bpsk import bpsk_modulate
from bpsk import bpsk_demodulate
from generate_channel import generate_channel_matrix

def mimo_channel(mimo_symbols, h_mimo, SNRdb):
    snr_times = 10 ** (SNRdb / 10)
    noise_std = np.sqrt(1 / snr_times)
    array = []
    SNR = noise_std * (np.random.normal(0, 1 / np.sqrt(2), len(mimo_symbols)) + 1j * np.random.normal(0, 1 / np.sqrt(2), len(mimo_symbols)))
    for i in range(0, len(mimo_symbols), 2):
        array.append(h_mimo[0][0] * mimo_symbols[i] + h_mimo[0][1] * mimo_symbols[i + 1] + SNR[i])
        array.append(h_mimo[1][0] * mimo_symbols[i] + h_mimo[1][1] * mimo_symbols[i + 1] + SNR[i + 1])
    return array

def zf_demodulate(mimoY, h_mimo):
    array = []
    for i in range(0, len(mimoY), 2):
        array.append(h_mimo[0][0] * mimoY[i] + h_mimo[0][1] * mimoY[i + 1])
        array.append(h_mimo[1][0] * mimoY[i] + h_mimo[1][1] * mimoY[i + 1])
    return array

if __name__ == "__main__":
    h_mimo = generate_channel_matrix()
    h_mimo_back = np.linalg.inv(h_mimo)
    mimo_symbols = bpsk_modulate(generate_bits(10))
    print(mimo_symbols)
    mimoY = mimo_channel(mimo_symbols, h_mimo, 0)
    print(mimoY)
    mimo_xhat = zf_demodulate(mimoY, h_mimo_back)
    print(mimo_xhat)
    demod = bpsk_demodulate(mimo_xhat)
    print(demod)