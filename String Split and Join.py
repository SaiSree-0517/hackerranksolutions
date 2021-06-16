#String Split and Join
def split_and_join(line):
    # write your code here
    x=line.split()
    a="-".join(x)
    return a
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
"""
Input (stdin)
this is a string
Expected Output
this-is-a-string
"""
