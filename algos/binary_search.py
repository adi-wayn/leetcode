class Solution(object):
    def binary_search(self, arr, target):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

if __name__ == "__main__":
    solution = Solution()
    arr = [1, 2, 3, 4, 5]
    target = 3
    result = solution.binary_search(arr, target)
    print(f"Index of {target} in array: {result}")