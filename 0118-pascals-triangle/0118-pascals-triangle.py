# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         rows = [[1]]
#         for i in range(1, numRows):
#             if i == 1:
#                 rows.append([1, 1])
#             else:
#                 tosum = 2**i # this is what it should sum up to
#                 toapp = [0]*(i+1) # placeholder array 
#                 toapp[0], toapp[-1] = 1, 1
#                 tosum = tosum - 2 
#                 while tosum > 0:
#                     for j in range(1, 1 + len(toapp)//2):
#                         toapp[j] = rows[i-1][j] + rows[i-1][j-1]
#                         toapp[-j - 1] = toapp[j]
#                         tosum = tosum - 2*toapp[j]
#                     rows.append(toapp)
#         # print(toapp)
#         return rows 
                    
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            if i == 1:
                rows.append([1, 1])
            else:
                toapp = [0]*(i+1) # placeholder array 
                toapp[0], toapp[-1] = 1, 1
                for j in range(1, 1 + len(toapp)//2):
                    toapp[j] = rows[i-1][j] + rows[i-1][j-1]
                    toapp[-j - 1] = toapp[j]
                rows.append(toapp)
        return rows 
                    