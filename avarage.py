def average(array):
    # your code goes here
    array = set(array)
    r = sum(array)/len(array)
    print(sum(array))
    return r

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
