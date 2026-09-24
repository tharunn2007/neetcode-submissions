class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #we compared prices accordingly for the minimum rather than global minimum cuz sometimes we cant determine the global minimum is always the max profit giving 
        min_prices = prices[0]

        # setting max profit to 0 and then later if greater we can change...for the same question but repeated buying and selling (the II version) I guess we want to successivly add and minimize the array after 1 search through some sort of recursion but idk how to find the base case for that tho
        max_profit = 0


        for i in prices:
            
            #checking if the prices[0] can be changed or not
            if i<min_prices:
                min_prices = i
            
            # since it cant be we can go to the next step if the profit is maximizing comapred to prev set value


            elif i-min_prices>max_profit:
                max_profit = i-min_prices
        return max_profit