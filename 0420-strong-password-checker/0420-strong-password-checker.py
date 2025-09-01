class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        missing = 0
        if not any(c.islower() for c in password):  missing += 1
        if not any(c.isupper() for c in password):  missing += 1
        if not any(c.isdigit() for c in password):  missing += 1
        # substeps2 = missing

        # length steps
        addsteps = max(0, 6 - n)
        delsteps = max(0, n - 20)
        
        substeps = 0
        groups = [len(list(grp)) for _, grp in itertools.groupby(password)]
        print(groups)

        # with strategic delete, the number of substitions can be reduced 
        # def apply_best_delete():
        #     argmin, _ = min(
        #         enumerate(groups),
        #         # Ignore groups of length < 3 as long as others are available.
        #         key=lambda it: it[1] % 3 if it[1] >= 3 else 10 - it[1],
        #     )
        #     groups[argmin] -= 1
        
        for _ in range(delsteps):
            argmin, _ = min(
                enumerate(groups), # index @ 0 and val @ 1 
                # Ignore groups of length < 3 as long as others are available.
                key=lambda it: it[1] % 3 if it[1] >= 3 else 10 - it[1],
            )
            print(groups)
            groups[argmin] -= 1
            print(groups[argmin])
            print("ok")
        
        # On the finished groups, we need one repace per 3 consecutive letters
        substeps = sum(group // 3 for group in groups)

        print("add/del", addsteps, delsteps)
        print("rep", substeps)
        print("up, low, num", missing)
        return delsteps + max(substeps, missing, addsteps)
        