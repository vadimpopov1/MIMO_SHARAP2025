from generate_channel import *
from bpsk import *
from generate_bits import *
from mimo_channel import *
from ber_theor import *

test_count = 10000

num_bits = int(input('Enter count of bits: '))
snr_db_list = [0.0, 1.0, 5.0, 10.0, 15.0] # Децибелы (Шум)
for snr_db in snr_db_list:
    ber_sum = theoretical_ber_siso(snr_db)
    ber_mimo_sum = 0
    for _ in range(test_count): # Проводим тесты
        mimo_bits = generate_bits(2 * num_bits)
        mimo_symbols = bpsk_modulate(mimo_bits)
        h_mimo = generate_channel_matrix()
        mimoY = mimo_channel(mimo_symbols, h_mimo, snr_db)
        h_mimo_back = np.linalg.inv(h_mimo)
        mimo_xhat = zf_demodulate(mimoY, h_mimo_back)
        mimo_bits_hat = bpsk_demodulate(mimo_xhat)
        ber_mimo_sum += calculate_ber(mimo_bits, mimo_bits_hat)
    ber_mimo = ber_mimo_sum / test_count # Среднее значение потери из-за шумов и иных факторов
    print(f"Практическое MIMO: {ber_mimo}, Теоретическое: {ber_sum}")