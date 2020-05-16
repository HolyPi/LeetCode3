s = "egg"
t = "add"

def isIsomorphic(s, t):
    isomorphic = []
    for char in s:
        isomorphic.append(s.index(char))
    return isomorphic


print(isIsomorphic(s, t))

#Time complexity: 0(n)
#Space complexity: 0(n)