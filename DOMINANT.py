def check_dominant_army(T):
    for _ in range(T):
        N_A, N_B, N_C = map(int, input().split())
        if N_A > N_B + N_C:
            print("YES")
        elif N_B > N_A + N_C:
            print("YES")
        elif N_C > N_A + N_B:
            print("YES")
        else:
            print("NO")

T = int(input())
check_dominant_army(T)
