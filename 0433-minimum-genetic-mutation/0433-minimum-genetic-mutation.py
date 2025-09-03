# class Solution:
#     def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
#         if startGene == endGene:
#             return 0 
            

#         mut = 0
#         gene_choices = ['A', 'C', 'G', 'T']
#         bank_set = set(bank) 

#         # bfs
#         queue = deque()
#         queue.append(startGene)
#         visited_set = set()

#         while queue:
#             for i in range(len(queue)):
#                 gene = queue.popleft()
#                 if gene == endGene: # stop condition
#                     return mut
#                 # if not found then for 8 characters we try switches 
#                 for j in range(8):
#                     for g in gene_choices: 
#                         if gene[:j] + g + gene[j+1:] not in visited_set and gene[:j] + g + gene[j+1:] in bank_set:
#                             visited_set.add(gene[:j] + g + gene[j+1:])
#                             queue.append(gene[:j] + g + gene[j+1:])
#             mut = mut + 1


#         return -1 # no valid mutations to get from startGene to endGene

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        mut = 0 
        choices = ['A', 'T', 'C', 'G']
        bank_set = set(bank)

        queue = deque()
        queue.append(startGene)
        visited = set()

        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return mut 
                for i in range(8):
                    for c in choices:
                        if gene[:i] + c + gene[i+1:] not in visited and gene[:i] + c + gene[i+1:] in bank_set:
                            queue.append(gene[:i] + c + gene[i+1:])
                            visited.add(gene[:i] + c + gene[i+1:])
            mut = mut + 1 
        return -1
