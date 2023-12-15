# Two sum Problem 
class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None

solution = Solution()
numbers = [2,7,11,15]
goal = 9
result = solution.twoSum(numbers,goal)
print(result) 

# Reverse Linklist

class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def ReverseList(self,head):
        prev = None
        current = head
        while(current):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return(prev)
 
# Valid Parenthesis

class Solution:
    def isValid(self,s):
        stack = []
        open_brackets = '{(['
    
        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
    
        return len(stack) == 0

