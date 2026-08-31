class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # Use variables to track the previous two steps (Iterative Approach)
        one_step_behind = 2
        two_steps_behind = 1
        current_step = 0
        
        for i in range(3, n + 1):
            current_step = one_step_behind + two_steps_behind
            two_steps_behind = one_step_behind
            one_step_behind = current_step
            
        return current_step