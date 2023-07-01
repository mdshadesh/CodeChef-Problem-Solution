t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    complementary_strand = ""
    for nucleotide in s:
        if nucleotide == 'A':
            complementary_strand += 'T'
        elif nucleotide == 'T':
            complementary_strand += 'A'
        elif nucleotide == 'C':
            complementary_strand += 'G'
        elif nucleotide == 'G':
            complementary_strand += 'C'

    print(complementary_strand)
