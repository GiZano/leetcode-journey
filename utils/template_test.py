# ============================================================================
# Local Test Runner
# Copy and append this block to the bottom of your solution file.
# Run with: python3 <file>.py
# ============================================================================

if __name__ == "__main__":
    sol = Solution()

    # ------------------------------------------------------------------------
    # Option A: Direct assertions (Quick & Simple)
    # ------------------------------------------------------------------------
    # Example:
    # assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    # print("Test 1: PASSED")

    # ------------------------------------------------------------------------
    # Option B: Table-driven test cases (Scalable for multiple inputs)
    # ------------------------------------------------------------------------
    """
    test_cases = [
        # ((args...), expected)
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
    ]

    for i, (args, expected) in enumerate(test_cases, 1):
        actual = sol.twoSum(*args)
        assert actual == expected, f"Test {i} FAILED: expected {expected}, got {actual}"
        print(f"Test {i}: PASSED (output: {actual})")
    """
