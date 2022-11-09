a = ord(input())
b = ord(input())
st = []
def strin(a, b):
    for i in range(a+1, b):
        st.append(chr(i))
    return st
print(*strin(a, b))