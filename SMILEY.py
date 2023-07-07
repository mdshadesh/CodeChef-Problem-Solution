def solve():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if s[i] == ':':
                if s[j] == ')':
                    if s[j + 1] == ')':
                        continue
                    elif s[j + 1] == ':':
                        cnt += 1
                else:
                    break
            else:
                break
    print(cnt)


def main():
    t = int(input())
    while t > 0:
        solve()
        t -= 1


if __name__ == "__main__":
    main()
