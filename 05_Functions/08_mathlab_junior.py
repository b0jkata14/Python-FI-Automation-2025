def fact_recursive(n):
    if n == 0 or n == 1:
        return 1

    return n * fact_recursive(n - 1)


def fact_iterative(n):
    result = 1

    for i in range(2, n + 1):
        result *= i

    return result


n = int(input())

rec_val = fact_recursive(n)
it_val = fact_iterative(n)

print(f"recursive: {rec_val}")
print(f"iterative: {it_val}")

match_result = "yes" if rec_val == it_val else "no"
print(f"match: {match_result}")
