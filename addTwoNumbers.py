# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #first we will create the 3 variables we need to solve this problem
        carry = 0
        output = ListNode(0)
        pointer = output
        
        #now we iterate over our lists as long as they are not empty and we still have a carry-over
        #value
        while (l1 or l2 or carry):
            
            #handling case where there is no l1 or l2 value
            firstVal = l1.val if l1 else 0
            secondVal = l2.val if l2 else 0
            
            #now we sum our first and second vals and the carry
            #then we calculate the remainder with the modulus which is the value to be stored in our 
            #new linked list
            #lastly, we calculate the carry value by doing floor division by 10
            summ = firstVal + secondVal + carry
            rem = summ % 10
            carry = summ // 10
            
            #now we store the rem in the pointer which will also update our output list
            pointer.next = ListNode(rem)
            #shifting our pointer up one place to point to the next spot in the list
            pointer = pointer.next
            
            #now we shift up in list1 and list2 as long as there is a value there
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        #we return output.next because the initial value stored in output was a 0 which we don't 
        #actually want
        return output.next