class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0 
            
        mut = 0
        gene_choices = ['A', 'C', 'G', 'T']
        bank_set = set(bank)

        # bfs
        queue = deque()
        queue.append(startGene)
        visited_set = set()

        while queue:
            for i in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return mut
                for j in range(8):
                    for g in gene_choices: 
                        if gene[:j] + g + gene[j+1:] not in visited_set and gene[:j] + g + gene[j+1:] in bank_set:
                            visited_set.add(gene[:j] + g + gene[j+1:])
                            queue.append(gene[:j] + g + gene[j+1:])
            mut = mut + 1


        return -1