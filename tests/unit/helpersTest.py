import json
TestModule = projectRelativeImport('helpers', 'app/util', 'TestModule')
TestCase = projectRelativeImport('testCase', 'tests', 'TestCase')
TestCases = projectRelativeImport('testCases', 'tests', 'TestCases')
TestChecker = projectRelativeImport('testCasesChecker', 'tests', 'TestChecker')

class Main(TestChecker.Checker):#extends TestChecker.Checker which has the run method
    def __init__(self):
        self.TestModule = TestModule #the module we're testing functions for
        self.cases = TestCases.CaseHolder #holds the method and cases we test on it for the module given above
        method = 'url_validate' #we're testing the url_validate method
        cases = [#these are our inputs and expected outputs
            TestCase.Case('/noDomainNoFile', False),
            TestCase.Case('/noDomain/file.html', False),
            TestCase.Case('google.com', False),
            TestCase.Case('http://google.com', True),
            TestCase.Case('https://google.com', True),
            TestCase.Case('ftp://domain.com/path', True),
            TestCase.Case('http://domain.com/path/file.html', True)
        ]
        for case in cases:#go through our array of cases and add them all to our cases object
            self.TestCases.addCaseToMethod(method, case)
