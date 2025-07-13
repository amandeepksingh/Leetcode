# class Solution(object):
#     def dailyTemperatures(self, temperatures):
#         """
#         :type temperatures: List[int]
#         :rtype: List[int]
#         """
#         dayarr = [0]*len(temperatures)
#         st = [0]
#         for i in range(len(temperatures)):
#             while st and temperatures[i] > temperatures[st[-1]]:
#                 idx = st.pop()
#                 dayarr[idx] = i - idx
#             st.append(i)
#         return dayarr
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        dayarr = [0]*len(temperatures) # array to store the final result 
        st = [0] # stack of indexes 
        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]: # while the curr temp > last temp in the stack 
                idx = st.pop() # get the last index 
                dayarr[idx] = i - idx # the diff in the index 
            st.append(i)
        return dayarr
