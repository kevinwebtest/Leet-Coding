class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        i = 0
        j = len(height)-1
        while i < j:
            water = max(water, (j-i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return water
      
# Helped by StefanPochmann
# Variables i and j define the container under consideration. We initialize them to first and last line, meaning the widest container. Variable water will keep track of the highest amount of water we managed so far. We compute j - i, the width of the current container, and min(height[i], height[j]), the water level that this container can support. Multiply them to get how much water this container can hold, and update water accordingly. Next remove the smaller one of the two lines from consideration, as justified above in "Idea / Proof". Continue until there is nothing left to consider, then return the result.

