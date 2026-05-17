class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(m_list):
            if len(m_list) <= 1:
                return m_list

            n = len(m_list) // 2

            l1 = mergeSort(m_list[:n])
            l2 = mergeSort(m_list[n:])

            return self.ascend_sort(l1, l2)

        return mergeSort(nums)

    
    def ascend_sort(self, l1, l2):
        p1, p2 = 0, 0
        result = []

        while p1 < len(l1) and p2 < len(l2):
            if l1[p1] < l2[p2]:
                result.append(l1[p1])
                p1 += 1
            else:
                result.append(l2[p2])
                p2 += 1

        if p1 != len(l1):
            result.extend(l1[p1:])
        elif p2 != len(l2):
            result.extend(l2[p2:])

        return result
