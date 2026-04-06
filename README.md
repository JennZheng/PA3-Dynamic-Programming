# PA3-Dynamic-Programming
COP4533 Programming 3 Assignment

# Team
Jennifer Zheng: 52838059  
Srinitha Srikanth: 55178917

# Compile/Build
N/A

# How to Run
Run the program from the repository root using:

python src/main.py data/example.in

To verify the output matches the expected file:

python src/main.py data/example.in > my_output.out
diff my_output.out data/example.out

# Assumptions/Dependencies
The main algorithm uses Python Standard Library (sys). External libraries like matplotlib are only needed for the running the grapher to generate the graph in Question 1.  
  
  Input Files Format:
  ``` 
  K
  x1 v1
  x2 v2  
  ...
  xK vK
  A
  B
  ```
  Output files will have a single integer on one line which is the max value of common subsequence of A and B. On the next line is one optimal common subsequence that achieves this value.  
    
  Output file Format:  
  ```
9
cb
```


# Question 1: Empirical Comparison
![alt text](runtime_graph.png)

# Question 2: Recurrence Equation
dp[i][j] = maximum total value of a common subsequence of A[:i] and B[:j].

Base cases:
dp[0][j] = 0
dp[i][0] = 0

Recurrence:
if A[i-1] != B[j-1], then dp[i][j] = max(dp[i-1][j], dp[i][j-1])
if they match, then dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + value[A[i-1]])

# Question 3: Big-Oh
Pseudocode: 

HVLCS(A, B, value):
    let n = length(A), m = length(B)
    create array dp[0..n][0..m], init all to 0
    for i = 1 to n:
        for j = 1 to m:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if A[i-1] == B[j-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + value[A[i-1]])
    return dp[n][m]

The time and space complexity of the algorithm would be O(nm).
