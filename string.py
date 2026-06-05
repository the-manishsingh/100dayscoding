def print_formatted(number):
     for i in range(1,number+1) :
        d = str(i)
        o = oct(i)[2:]
        h = hex(i)[2:]
        b = bin(i)[2:]
        print(d , o , h , b)
     return ""
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)