'''Write an algorithm to find the largest sum of the continuous sequence from the given list
Kadane's Algorithm '''

def max_subarray_sum(nums):
    """
    Finds the largest sum of a continuous sequence in a given list and the subarray itself.
    
    :param nums: List of integers
    :return: Largest sum of the continuous subarray and the subarray
    """
    if not nums:
        return 0, []  # Handle empty list case

    # Initialize variables
    max_current = max_global = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        # Check if starting a new subarray gives a higher sum
        if nums[i] > max_current + nums[i]:
            max_current = nums[i]
            temp_start = i
        else:
            max_current += nums[i]

        # Update the global maximum and the indices for the subarray
        if max_current > max_global:
            max_global = max_current
            start = temp_start
            end = i

    # Extract the subarray
    max_subarray = nums[start:end + 1]
    return max_global, max_subarray

# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
largest_sum, subarray = max_subarray_sum(nums)
print("The largest sum of the continuous sequence is:", largest_sum)
print("The subarray contributing to this sum is:", subarray)

