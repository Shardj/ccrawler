class Case:
    def __init__(self, inputs, expectedOutput):
        if type(inputs) is not list:
            inputs = [inputs]

        self.inputs = inputs
        self.expectedOutput = expectedOutput
        self.trueOutput = None

    def check():
        return self.expectedOutput == self.trueOutput
