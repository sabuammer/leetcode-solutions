# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr_place = 1
        first_num = second_num = 0
        while l1:
            first_num += l1.val * curr_place
            curr_place *= 10
            l1 = l1.next
        curr_place = 1
        while l2:
            second_num += l2.val * curr_place
            curr_place *= 10
            l2 = l2.next
        total = first_num + second_num
        str_total = str(total)
        total_lst = ListNode(str_total[-1])
        return_lst = total_lst
        for i in range(len(str_total) - 2, -1, -1):
            total_lst.next = ListNode(int(str_total[i]))
            total_lst = total_lst.next
        return return_lst