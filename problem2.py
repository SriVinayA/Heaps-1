# time complexity: O(N log k), where N is the total number of nodes across all lists, and k is the number of linked lists.
# space complexity: O(N + k): O(N) for the output list, and O(k) for the heap used during merging.
# Approach:
# - We'll push the first node of each list into the min-heap (priority queue).
# - For each extracted minimum node, we add it to the merged linked list.
# - After extracting, we push the next node from that list (if it exists) into the heap.
# - Continue until the heap is empty.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []

        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(minheap, (head.val, idx, head))
        
        dummy = ListNode(0)
        current = dummy

        while minheap:
            value, idx, node = heapq.heappop(minheap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(minheap, (node.next.val, idx, node.next))
        
        return dummy.next