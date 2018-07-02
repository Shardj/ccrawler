class CaseHolder:
    def addMethodToTest(methodName):
        setattr(self, methodName, []]) #equivalent to: self.methodName = []

    def addCaseToMethod(methodName, case):
        if not hasattr(self, methodName):
            addMethodToTest(methodName)

        getattr(self, methodName).append(case)
