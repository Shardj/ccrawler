class Checker:
    def run(self):
        for function, functionCases in enumerate(self.cases):
            for case in functionCases:
                method_to_call = getattr(self.TestModule, function)
                case.trueOutput = method_to_call(*case.inputs)
                if case.check() is False:
                    print('Failed test case with inputs:\n' + json.dumps(case.inputs)
                    + '\n\nExpected output:\n' + json.dumps(case.expectedOutput))
                    + '\n\nTrue output:\n' + json.dumps(case.trueOutput))
