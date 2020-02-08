#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because the running time depends on how many times n^2 fits into n^3. In other words the running time, depends on n^3/n^2, which reduces to n.


b) O(n^2) because the outer loop loops n times and the inner loop loops n - 1 times for every step of the inner loop. Hence, runtime is dependant on n(n - 1) or in other words effectively n^2


c) O(n) because the function runs once for every n where n > 0

## Exercise II

1. Start at the top of the building.
2. Drop an egg.
3. If it doesn't break, you know that no matter where you drop the egg from, it will not break. You are done.
4. If it does break, go halfway down the building.
5. Drop an egg.
6. If it does break, note where you are as the current minimum unsafe height to drop the egg from.
7. Otherwise, note where you are as the current maximum safe height to drop the egg from.
8. If the difference between the current minimum unsafe height and the current maximum safe height is more than 1, go to the midpoint between the current minimum unsafe height and the current maximum safe height and repeat the process from step 5.
9. Otherwise, the current maximum safe height is the actual maximum safe height. You are done.

Runtime Complexity: O(log(n))