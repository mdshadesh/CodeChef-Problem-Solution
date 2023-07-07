def rotate(c, k):
    ascii_code = ord(c)
    new_code = ascii_code + k
    if new_code > ord('z'):
        new_code -= 26
    return chr(new_code)

def find_rot_k_cipher(n, s, t, u):
    rot_k_cipher = ""
    for i in range(n):
        k = (ord(t[i]) - ord(s[i])) % 26
        rotated_char = rotate(u[i], k)
        rot_k_cipher += rotated_char
    return rot_k_cipher

q = int(input())

for _ in range(q):
    n = int(input())
    s = input()
    t = input()
    u = input()

    cipher = find_rot_k_cipher(n, s, t, u)
    print(cipher)
