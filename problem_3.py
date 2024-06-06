def active_trading(stocks, investors):
    answer = []

    for time in investors:
        active_count = 0
        for start, end in stocks:
            if start <= time <= end:
                active_count += 1
        answer.append(active_count)
        print(f"Investor at time {time}: Active stocks count {active_count}")

    return answer

# Test cases
test_cases = [
    {
        "stocks": [[1, 4], [2, 3], [3, 5]],
        "investors": [2, 3, 5],
        "output": [2, 3, 1]
    },
    {
        "stocks": [[1, 6], [3, 7], [9, 12], [4, 13]],
        "investors": [2, 3, 7, 11],
        "output": [1, 2, 2, 2]
    },
    {
        "stocks": [[1, 10], [3, 3]],
        "investors": [3, 3, 2],
        "output": [2, 2, 1]
    },
    {
        "stocks": [[5, 8], [6, 7], [8, 10]],
        "investors": [6, 9, 10, 5],
        "output": [2, 1, 1, 1]  # Corrected expected output
    },
    {
        "stocks": [[1, 2], [2, 3], [3, 4]],
        "investors": [1, 2, 3, 4],
        "output": [1, 2, 2, 1]
    }
]

# Running the test cases
for i, test_case in enumerate(test_cases, 1):
    stocks = test_case["stocks"]
    investors = test_case["investors"]
    expected_output = test_case["output"]
    result = active_trading(stocks, investors)
    assert result == expected_output, f"Test Case {i} Failed: Expected {expected_output}, got {result}"
    print(f"Test Case {i} Passed: {result}")

# Printing the output arrays for each test case
for i, test_case in enumerate(test_cases, 1):
    stocks = test_case["stocks"]
    investors = test_case["investors"]
    result = active_trading(stocks, investors)
    print(f"Test Case {i} Output: {result}")
