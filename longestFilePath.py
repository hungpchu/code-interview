def lengthLongestPath( inp):
    maxLength = 0
    path = {0: 0}
    for line in input.splitlines():
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        path[depth + 1] = path[depth] + len(name) + 1
        if '.' in name:
            maxLength = max(maxLength, path[depth] + len(name))
    return maxLength      
    
inp = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

print lengthLongestPath(inp)

