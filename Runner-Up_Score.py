if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    i=n-1
    arr.sort()
    max_n = arr[-1]

    while i>=0:
        if max_n>arr[i]:
            max_n=arr[i]
            print(max_n)
            break
        i-=1
