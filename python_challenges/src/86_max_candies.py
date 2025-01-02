'''Write an algorithm to find the mac num of chocolates that can be picked from the jars in such a way that the chocolates are not picked from jars next to each other
There is a set of N jars containing chocolates. Some of them may be empty. Determine the maximum number of chocolates one can pick from the jars given that one cannot pick from jars next to each other.'''

def max_chocolates(jars):
    """
    Finds the maximum number of chocolates that can be picked from jars without picking from adjacent jars.

    :param jars: List of integers representing chocolates in each jar
    :return: Maximum chocolates that can be picked
    """
    n = len(jars)
    if n == 0:
        return 0
    if n == 1:
        return jars[0]
    
    # Initialize DP array
    dp = [0] * n
    dp[0] = jars[0]
    dp[1] = max(jars[0], jars[1])

    # Fill the DP array
    for i in range(2, n):
        dp[i] = max(dp[i - 1], jars[i] + dp[i - 2])

    return dp[-1]

# Example usage
jars = [3, 2, 5, 10, 7]
print("The maximum chocolates that can be picked:", max_chocolates(jars))
