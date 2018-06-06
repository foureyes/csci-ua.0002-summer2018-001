def caesar_encrypt(s):
    """encrypts a string by rotating each letter 23 places to the right"""
    up_start, up_end = 65, 90
    low_start, low_end = 97, 122
    shift = 23
    translation = ''
    for c in s:
        code_point = ord(c)
        if code_point >= up_start and code_point <= up_end - shift:
            translation += chr(code_point + shift)
        elif code_point >= low_start and code_point <= low_end - shift:
            translation += chr(code_point + shift)
        elif code_point > up_end - shift and code_point <= up_end:
            translation += chr(code_point - 26 + shift)
        elif code_point > low_end - shift and code_point <= low_end:
            translation += chr(code_point - 26 + shift)
        else:
            translation += c
    return translation

print(caesar_encrypt('Hello world! zzz'))
print(caesar_encrypt('abc xyz'))
expected = 'Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.'
observed = caesar_encrypt('The quick brown fox jumps over the lazy dog.')
assert expected == observed, 'test encryption'

