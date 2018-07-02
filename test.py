# python3 -m test
import unittest, bootstrap
print('checking __name__ == "__main__"')
if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('tests')
    print('Attempting to run tests')
    unittest.TextTestRunner().run(all_tests)
    print('Tests completed')
