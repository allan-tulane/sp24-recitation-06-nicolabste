# CMPS 2200 Recitation 06
## Answers

**Name:** Nicolas Labarca
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**

The work of the algorithm is defined by the recurrence W(n) = 1 + W(n-1) + W(n-2), leading to a complexity of O(2^n). This exponential time complexity arises because the algorithm recalculates the same Fibonacci numbers multiple times.

- **3)**

The span, or the longest path through the computation graph, follows the recurrence S(n) = 1 + S(n-1), resulting in a linear complexity, O(n). This reflects the longest chain of dependencies from F_0 to F_n.

- **4)**

When examining the counts array for the 9th Fibonacci number, a triangular pattern emerges, with initial rows starting from all zeros and incrementally changing the rightmost zero to a one until a one reaches the leftmost position. This pattern does not directly reflect the Fibonacci sequence but indicates the number of times each Fibonacci number is computed, showcasing the inefficiency of the recursive approach as many computations are repeated.

- **6)**

For the top-down dynamic programming approach, the maximum number of times the function for a specific Fibonacci number, fib_top_down(i), will be called is exactly once for each distinct i, leading to a total of n calls. Therefore, both the work and the span of this algorithm are linear, O(n), reflecting a significant efficiency improvement by avoiding redundant computations through memoization.

- **8)**

In the bottom-up approach, each Fibonacci number F_i is computed exactly once and read a maximum of two times during the calculation of F_{i+1} and F_{i+2}, except for the last two numbers which are read less. The work and span of this algorithm are both O(n), as it iteratively computes each Fibonacci number from the base cases up to the nth number without recursion, ensuring optimal efficiency with minimal reads and no redundant computations.
