from hamming_code import hamming as hm
from reedsolo import RSCodec

CHUNK_LENGTH = hm.CHUNK_LENGTH
CHECK_BITS = hm.CHECK_BITS


def task1():
    print('---------Task1--------')
    source = input('Укажите текст для кодирования/декодирования:')
    print('Длина блока кодирования: {0}'.format(CHUNK_LENGTH))
    print('Контрольные биты: {0}'.format(CHECK_BITS))
    encoded = hm.encode(source)
    print('Закодированные данные: {0}'.format(encoded))
    decoded = hm.decode(encoded)
    print('Результат декодирования: {0}'.format(decoded))
    encoded_with_error = hm.set_errors(encoded)
    print('Допускаем ошибки в закодированных данных: {0}'.format(encoded_with_error))
    diff_index_list = hm.get_diff_index_list(encoded, encoded_with_error)
    print('Допущены ошибки в битах: {0}'.format(diff_index_list))
    decoded = hm.decode(encoded_with_error, fix_errors=False)
    print('Результат декодирования ошибочных данных без исправления ошибок: {0}'.format(decoded))
    decoded = hm.decode(encoded_with_error)
    print('Результат декодирования ошибочных данных с исправлением ошибок: {0}'.format(decoded))


def task2():
    print('---------Task2--------')
    rsc = RSCodec(10)  # 10 ecc symbols
    print(rsc.encode(b'hello world'))
    tampered_msg = b'heXXX world\xed%T\xc4\xfdX\x89\xf3\xa8\xaa'
    print(tampered_msg)
    decoded_msg, decoded_msgecc, errata_pos = rsc.decode(tampered_msg)
    print(decoded_msg)  # decoded/corrected message
    print(decoded_msgecc)  # decoded/corrected message and ecc symbols
    print(errata_pos)  # errata_pos is returned as a bytearray, hardly intelligible
    print(list(errata_pos)[::-1])  # convert to a list to get the errata positions as integer indices

    rsc = RSCodec(12)  # using 2 more ecc symbols (to correct max 6 errors or 12 erasures)
    print(rsc.encode(b'hello world'))
    print(rsc.decode(b'hello worXXXXy\xb2XX\x01q\xb9\xe3\xe2=')[0])  # 6 errors - ok, but any more would fail
    print(rsc.decode(b'helXXXXXXXXXXy\xb2XX\x01q\xb9\xe3\xe2=', erase_pos=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16])[
              0])  # 12 erasures - OK
    maxerrors, maxerasures = rsc.maxerrata(verbose=True)
    print(maxerrors, maxerasures)


def task3():
    """Need take code from task1"""
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    task1()
    task2()
    task3()
