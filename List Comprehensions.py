#List Comprehensions
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    # List Comprehensions in Python - Hacker Rank Solution START
    output = [];
    abc = [];
    for X in range(x+1):
        for Y in range(y+1):
            for Z in range(z+1):
                if X+Y+Z != n:
                    abc = [X,Y,Z];
                    output.append(abc);
print(output);
"""
Input (stdin)
1
1
1
2
Expected Output
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""
