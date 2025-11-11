void rotate(int* nums, int numsSize, int k) {
    if (numsSize == 0) return;

    k = k % numsSize;
    if (k == 0) return;

    int count = 0;

    for (int start = 0; count < numsSize; start++) {
        int current = start;
        int prev = nums[start];

        do {
            int next = (current + k) % numsSize;
            int temp = nums[next];
            nums[next] = prev;
            prev = temp;
            current = next;
            count++;
        } while (start != current);
    }
}