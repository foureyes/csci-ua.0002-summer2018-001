def caesar_decrypt(s):
    """decrypts a string that was encrypted by rotating each letter 23 places
     to the right"""
    up_start, up_end = 65, 90
    low_start, low_end = 97, 122
    shift = 23
    translation = ''
    for c in s:
        code_point = ord(c)
        if code_point >= up_start + shift and code_point <= up_end:
            translation += chr(code_point - shift)
        elif code_point >= low_start + shift and code_point <= low_end:
            translation += chr(code_point - shift)
        elif code_point < up_start + shift and code_point >= up_start:
            translation += chr(code_point + 26 - shift)
        elif code_point < low_start + shift and code_point >= low_start:
            translation += chr(code_point + 26 - shift)
        else:
            translation += c
    return translation

print(caesar_decrypt('Ebiil tloia! www'))
print(caesar_decrypt('xyz uvw'))
expected = 'The quick brown fox jumps over the lazy dog.' 
observed = caesar_decrypt('Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.')
assert expected == observed, 'test decryption'
