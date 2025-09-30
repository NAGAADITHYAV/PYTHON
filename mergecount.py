def process_string_optimized(s, k):
    stack = []
    count = 0

    for char in s:
        # If top of stack is same as current character, pop it (remove pair)
        if stack and stack[-1] == char:
            stack.pop()
            count += 1
            # Reset count when it reaches k
            if count == k:
                count = 0
        else:
            stack.append(char)

    return count + 1


# Example usage
s = "baabzzpq"
k = 4
result = process_string_optimized(s, k)
print(f"Result: {result}")
