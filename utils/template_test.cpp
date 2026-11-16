// ============================================================================
// Local Test Runner
// Copy and append this block to the bottom of your solution file.
// Compile with: g++ -std=c++20 -DLOCAL <file>.cpp -o runner && ./runner
// ============================================================================

#ifdef LOCAL
#include <iostream>
#include <vector>
#include <string>
#include <cassert>

int main() {
    Solution sol;

    // ------------------------------------------------------------------------
    // Option A: Direct assertion / print tests (Quick & Simple)
    // ------------------------------------------------------------------------
    {
        // Example:
        // std::vector<int> input1 = {1, 0, 0, 0, 1};
        // int arg1 = 1;
        // auto expected1 = true;
        // auto actual1 = sol.canPlaceFlowers(input1, arg1);
        // std::cout << "Test 1: " << (actual1 == expected1 ? "PASSED" : "FAILED") << "\n";
    }

    // ------------------------------------------------------------------------
    // Option B: Table-driven test cases (Scalable for multiple inputs)
    // ------------------------------------------------------------------------
    /*
    struct TestCase {
        std::vector<int> input;
        int arg;
        bool expected;
    };

    std::vector<TestCase> testCases = {
        {{1, 0, 0, 0, 1}, 1, true},
        {{1, 0, 0, 0, 1}, 2, false},
    };

    int passed = 0;
    for (size_t i = 0; i < testCases.size(); ++i) {
        auto& tc = testCases[i];
        auto inputCopy = tc.input; // copy if method modifies vector in-place
        auto actual = sol.canPlaceFlowers(inputCopy, tc.arg);

        if (actual == tc.expected) {
            std::cout << "Test " << (i + 1) << ": PASSED\n";
            passed++;
        } else {
            std::cout << "Test " << (i + 1) << ": FAILED (Expected: " 
                      << tc.expected << ", Got: " << actual << ")\n";
        }
    }
    std::cout << "Results: " << passed << "/" << testCases.size() << " passed.\n";
    */

    return 0;
}
#endif
