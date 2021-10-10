def calculate(self, s: str) -> int:
    arr = []
    for ch in s:
        arr.append(ch)
    return self._calculate_util(arr)
    
    def _calculate_util(self, nums):
        stack, sign, num = [], '+', 0
        while len(nums) > 0:
            ch = nums.pop(0)
            
            if ch.isdigit():
                num = num*10 + int(ch)
            if ch == '(':
                num = self._calculate_util(nums)
            if ch == '+' or ch == '-' or ch == ')' or len(nums) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                sign = ch
                num = 0
                if ch == ')':
                    break
        return sum(stack)
