import heapq

nums = [1, 3, 6, 5, 9, 8]
print(heapq.nlargest(3, nums))

print(heapq.nsmallest(3, nums))

# heapify(x) - Transform list x into a heap, in-place, in linear time.
heapq.heapify(nums)
print(nums)
# heappush(heap,item) - Push the value item onto the heap,
#  maintaining the heap invariant.
heapq.heappush(nums, 3)
print(nums)

# heappop(heap)
print(heapq.heappop(nums))
