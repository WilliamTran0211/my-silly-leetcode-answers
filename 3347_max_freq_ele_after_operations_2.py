from typing import List
from collections import defaultdict

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # Count frequency of each number in the original array
        frequency_count = defaultdict(int)
      
        # Track range contributions using sweep line technique
        # For each number x, we can change values in range [x-k, x+k] to become x
        range_contributions = defaultdict(int)
      
        for num in nums:
            # Count original frequency
            frequency_count[num] += 1
          
            # Initialize the contribution at this number's position
            range_contributions[num] += 0
          
            # Mark the start of the range where this number can contribute
            # (we can change num to any value in [num-k, num+k])
            range_contributions[num - k] += 1
          
            # Mark the end of the range (exclusive)
            range_contributions[num + k + 1] -= 1
      
        max_frequency = 0
        current_sum = 0
      
        # Process all positions in sorted order to calculate running sum
        for position, contribution_delta in sorted(range_contributions.items()):
            # Update running sum of how many numbers can be changed to this position
            current_sum += contribution_delta
          
            # Calculate max frequency at this position:
            # - Original frequency: frequency_count[position]
            # - Plus operations: min of available numbers and allowed operations
            max_frequency = max(
                max_frequency, 
                min(current_sum, frequency_count[position] + numOperations)
            )
      
        return max_frequency
