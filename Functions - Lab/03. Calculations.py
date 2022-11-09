action = ["multiply", "divide", "add", "subtract"]
calc = input()
n1 = int(input())
n2 = int(input())
def calculator(n1, n2):
    if calc == "multiply":
        return n1*n2
    elif calc == "divide":
        return n1/n2
    elif calc == 'add':
        return n1+n2
    elif calc == "subtract":
        return n1-n2
print(int(calculator(n1, n2)))