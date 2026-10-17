print("Harshith M : 1BM24CS113")

from itertools import product


def implies(a, b):
    return not a or b


def entails(kb, query, variables):
    print("\nTruth Table:")
    print(*variables, "KB", "Query", sep="\t")

    result = True

    for values in product([False, True], repeat=len(variables)):
        model = dict(zip(variables, values))

        kb_value = kb(model)
        query_value = query(model)

        print(*[int(v) for v in values],
              int(kb_value), int(query_value), sep="\t")

        if kb_value and not query_value:
            result = False

    return result


print("1. KB: Q->P, P->~Q, Q|R")
print("2. KB: ~(S|T)")
print("3. KB: (R->S) & (S->R)")

choice = int(input("Choose problem (1/2/3): "))

if choice == 1:
    variables = ["P", "Q", "R"]

    def kb(m):
        p, q, r = m["P"], m["Q"], m["R"]
        return implies(q, p) and implies(p, not q) and (q or r)

    queries = {
        "R": lambda m: m["R"],
        "R -> P": lambda m: implies(m["R"], m["P"]),
        "Q -> R": lambda m: implies(m["Q"], m["R"])
    }

elif choice == 2:
    variables = ["S", "T"]

    def kb(m):
        return not (m["S"] or m["T"])

    queries = {
        "S & T": lambda m: m["S"] and m["T"],
        "T | ~T": lambda m: m["T"] or not m["T"]
    }

elif choice == 3:
    variables = ["R", "S"]

    def kb(m):
        r, s = m["R"], m["S"]
        return implies(r, s) and implies(s, r)

    queries = {
        "R <-> S": lambda m: m["R"] == m["S"],
        "(R & S) | (~R & ~S)":
            lambda m: (m["R"] and m["S"]) or
                      (not m["R"] and not m["S"])
    }

else:
    print("Invalid choice")
    exit()

print("\nAvailable queries:")
names = list(queries)

for i, name in enumerate(names, 1):
    print(i, name)

q = int(input("Choose query number: "))

if 1 <= q <= len(names):
    name = names[q - 1]
    result = entails(kb, queries[name], variables)
    print("\nQuery:", name)
    print("KB entails Query:", result)
else:
    print("Invalid query")
