public class Merge_Sorted_Array {

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] nums1_copy = new int[m];

        for (int i = 0; i < m; i++) {
            nums1_copy[i] = nums1[i];
        }

        int i = 0, j = 0, k = 0;
        while (i < m && j < n) {
            if (nums1_copy[i] <= nums2[j]) {
                nums1[k] = nums1_copy[i];
                i++;
            } else {
                nums1[k] = nums2[j];
                j++;
            }

            k++;
        }

        while (i < m) {
            nums1[k] = nums1_copy[i];
            k++;
            i++;
        }

        while (j < n) {
            nums1[k] = nums2[j];
            k++;
            j++;
        }
    }
}