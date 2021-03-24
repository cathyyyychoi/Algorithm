inputN = input()
inputNs = inputN.split()

n1 = inputNs[0]
n2 = inputNs[1]

n1reverse = n1[::-1]
n2reverse = n2[::-1]

print(max(n1reverse, n2reverse))
