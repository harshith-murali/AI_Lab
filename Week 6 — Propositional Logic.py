print("Harshith M : 1BM24CS113")

import ast
import itertools
import re


def pl_true(expr, model):
    """Evaluate a propositional formula in one model."""
    node = ast.parse(expr, mode="eval").body

    def evaluate(node):
        if isinstance(node, ast.Name):
            return model[node.id]

        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Invert):
            return not evaluate(node.operand)

        if isinstance(node, ast.BinOp):
            left = evaluate(node.left)
            right = evaluate(node.right)

            if isinstance(node.op, ast.BitAnd):
                return left and right
            if isinstance(node.op, ast.BitOr):
                return left or right
            if isinstance(node.op, ast.RShift):
                return not left or right

        if isinstance(node, ast.Compare):
            if len(node.ops) == 1 and isinstance(node.ops[0], ast.Eq):
                return evaluate(node.left) == evaluate(node.comparators[0])

        raise ValueError("Invalid logical expression")

    return evaluate(node)


def tt_check_all(kb, query, symbols, model):
    if not symbols:
        if all(pl_true(sentence, model) for sentence in kb):
            return pl_true(query, model)
        return True

    p = symbols[0]
    rest = symbols[1:]

    true_model = model.copy()
    true_model[p] = True

    false_model = model.copy()
    false_model[p] = False

    return (
        tt_check_all(kb, query, rest, true_model)
        and tt_check_all(kb, query, rest, false_model)
    )


def tt_entails(kb, query, symbols):
    return tt_check_all(kb, query, symbols, {})


n = int(input("Enter number of propositions: "))
symbols = input("Enter proposition names: ").split()

m = int(input("Enter number of KB sentences: "))
kb = []

for i in range(m):
    sentence = input(f"Enter KB sentence {i + 1}: ")
    kb.append(sentence)

query = input("Enter query: ")

if (n != len(symbols) or len(set(symbols)) != n
        or any(not s.isidentifier() for s in symbols)):
    print("Invalid proposition names.")
else:
    print("\nTruth Table:")
    print(*symbols, "KB", "Query", sep="\t")

    for values in itertools.product([False, True], repeat=n):
        model = dict(zip(symbols, values))

        kb_value = all(pl_true(s, model) for s in kb)
        query_value = pl_true(query, model)

        print(*[int(v) for v in values],
              int(kb_value), int(query_value), sep="\t")

    result = tt_entails(kb, query, symbols)

    print("\nKB entails Query:", result)
