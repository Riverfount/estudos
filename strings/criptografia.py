def criptografia(text):
    aux_list = []
    for c in text:
        if c.isalpha():
            aux_list.append(chr(ord(c) + 3))
        else:
            aux_list.append(c)
    aux_str = ''.join(aux_list)[::-1]
    aux_list = []
    for i, c in enumerate(aux_str):
        if i >= (len(aux_str) // 2):
            aux_list.append(chr(ord(c) - 1))
        else:
            aux_list.append(c)
    return ''.join(aux_list)


if __name__ == '__main__':
    assert criptografia('Texto #3') == '3# rvzgV'
    assert criptografia('abcABC1') == '1FECedc'
    assert criptografia('vxpdylY .ph') == 'ks. \\n{frzx'
    assert criptografia('vv.xwfxo.fd') == 'gi.r{hyz-xx'
