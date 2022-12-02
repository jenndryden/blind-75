class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0 
        for i in range(1,len(colors)):
                print(i)
                #if len(colors)>i+1:
                if colors[i] == colors[i-1]:
                    time += min(neededTime[i], neededTime[i-1])
                    neededTime[i] = max(neededTime[i],neededTime[i-1])
        return time
#         ans = 0
#         for i in range(1,len(colors)):
#             print(i)
#             if colors[i] == colors[i-1]:
#                 ans += min(neededTime[i],neededTime[i-1])
#                 neededTime[i] = max(neededTime[i],neededTime[i-1])
#         return ans
        