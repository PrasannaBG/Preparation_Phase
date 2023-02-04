def finalValueAfterOperations(self, operations):
        # 2011. Final Value of Variable After Performing Operations
        # operations = ["--X","X++","X++"]
        X = 0
        Dict = {"--X":-1,"++X":1,"X++":1,"X--":-1}
        for i in range(0,len(operations)):
            X += Dict[operations[i]]
        return X