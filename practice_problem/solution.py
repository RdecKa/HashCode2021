with open("a_example", "r") as file:
    firstLine = file.readline().strip()
    M, T2, T3, T4 = list(map(int, firstLine.split(" ")))
    pizzas = []
    for pizzaIdx in range(M):
        p = file.readline().strip()
        pizzas.append(p.split(" ")[1:])
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
        solution.append((2, i, i+1, i+2, i+3))
        i += 4

    print(solution)

with open("a_solution", "w") as file:
    file.write(str(len(solution)) + "\n")
    for s in solution:
        s = list(map(str, s))
        file.write(" ".join(s) + "\n")
