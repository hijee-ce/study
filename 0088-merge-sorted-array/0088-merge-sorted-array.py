class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, write_index = m-1, n-1, m+n-1
        
        # nums1과 nums2의 배열에서 비교할 원소가 남아 있는 동안 확인
        while j >= 0 and i >= 0:
            if nums1[i] > nums2[j]:
                nums1[write_index] = nums1[i]
                i -= 1
            else:
                nums1[write_index] = nums2[j]
                j -= 1
            write_index -= 1
        
        # nums2에 남은 원소가 있으면, nums1에 남은 자리에 이동
        while j >= 0:
            nums1[write_index] = nums2[j]
            j -= 1
            write_index -= 1
        # nums1의 원소들은 이미 올바른 위치에 있으므로 이동할 필요 없음