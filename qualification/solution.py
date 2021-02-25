from Street import *
from Car import *
import sys

# Read which input to choose
selectedInput = "a"
if len(sys.argv) > 1:
    candidate = sys.argv[1]
    if len(candidate) == 1 and candidate in "abcdef":
        selectedInput = candidate
    else:
        print(f"! Invalid input {candidate}, using default")
print(f"Selected input: {selectedInput}")

# Read input
with open(f"input/{selectedInput}.in", "r") as file:
    firstLine = file.readline().strip()
    D, I, S, V, F = list(map(int, firstLine.split(" ")))
    allStreets = {}
    for s in range(S):
        street = Street.fromString(file.readline().strip())
        allStreets[street.name] = street
        print(street)
    for v in range(V):
        car = Car.fromString(file.readline().strip(), allStreets)
        print(car)

# Solve


# Write output file
# with open(f"{selectedInput}.out", "w") as file:
#     file.write(str(len(solution)) + "\n")
#     for s in solution:
#         s = list(map(str, s))
#         file.write(" ".join(s) + "\n")
