import heapq

nums = [1, 3, 6, 5, 9, 8]
print(heapq.nlargest(3, nums))
#[9, 8, 6]


print(heapq.nsmallest(3, nums))
#[1, 3, 5]


# heapify(x) - Transform list x into a heap, in-place, in linear time.
heapq.heapify(nums)
print(nums)
#[1, 3, 6, 5, 9, 8]


# heappush(heap,item) - Push the value item onto the heap,
#  maintaining the heap invariant.
heapq.heappush(nums, 3)
print(nums)
#[1, 3, 3, 5, 9, 8, 6]


# heappop(heap)
print(heapq.heappop(nums))
# 1

print(nums)
#[3, 3, 6, 5, 9, 8]
