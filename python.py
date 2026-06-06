import textwrap

def wrap(string, max_width):
    l = len(string)/max_width
    for i in range(0,int(l+1)):
        s = string[0:max_width]
        
        string = string.removeprefix(s)
        print(s)
    return ""

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)