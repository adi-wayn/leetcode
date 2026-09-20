class Solution(object):
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        sorted_arr = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        while i < len(left):
            sorted_arr.append(left[i])
            i += 1

        while j < len(right):
            sorted_arr.append(right[j])
            j += 1

        return sorted_arr


if __name__ == "__main__":
    solution = Solution()
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = solution.merge_sort(arr)
    print(f"Sorted array: {sorted_arr}")