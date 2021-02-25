import sys

# Read which input to choose
selectedInput = "a"
if len(sys.argv) > 1:
    candidate = sys.argv[1]
    if len(candidate) == 1 and candidate in "abcde":
        selectedInput = candidate
    else:
        print(f"! Invalid input {candidate}, using default")
print(f"Selected input: {selectedInput}")

# Read input
with open(f"input/{selectedInput}.in", "r") as file:
    firstLine = file.readline().strip()
    M, T2, T3, T4 = list(map(int, firstLine.split(" ")))
    pizzas = []
    for pizzaIdx in range(M):
        p = file.readline().strip()
        pizzas.append(p.split(" ")[1:])

# Solve
solution = []
i = 0
for team in range(T2):
    if i + 1 > M:
        break
    solution.append((2, i, i+1))
    i += 2
for team in range(T3):
    if i + 2 > M:
        break
    solution.append((3, i, i+1, i+2))
    i += 3
for team in range(T4):
    if i + 3 > M:
        break
    solution.append((4, i, i+1, i+2, i+3))
    i += 4

# Write output file
with open(f"{selectedInput}.out", "w") as file:
    file.write(str(len(solution)) + "\n")
    for s in solution:
        s = list(map(str, s))
        file.write(" ".join(s) + "\n")
