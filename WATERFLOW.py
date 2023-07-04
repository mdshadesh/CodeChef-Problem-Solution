def bucket_status(T):
    for _ in range(T):
        W, X, Y, Z = map(int, input().split())
        total_inflow = W + (Y * Z)
        if total_inflow > X:
            print("overflow")
        elif total_inflow == X:
            print("filled")
        else:
            print("unfilled")

T = int(input())
bucket_status(T)
