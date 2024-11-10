# time complexity: O(nlogk) where n is the number of elements in the array and k is the kth largest element.
# space complexity: O(k) where k is the kth largest element.
# Approach: I will use minHeap to store the kth largest element. I will iterate through the array and if the length of the minHeap is less than k, I will push the element to the heap. If the length of the heap is equal to k, I will check if the root of the heap is less than the current element, if it is then I will replace the root of the heap with the current element. At the end, I will return the root of the heap which is the kth largest element.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        
        for num in nums:
            
            if len(minHeap)<k:
                heapq.heappush(minHeap, num)
            elif minHeap[0]<num:
                heapq.heapreplace(minHeap, num)
        return minHeap[0]
    
def test_case():
    solution = Solution()
    
    assert solution.findKthLargest([3,2,1,5,6,4], 2) == 5, "test case1 failed"
    assert solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4, "test case2 failed"
    
test_case()