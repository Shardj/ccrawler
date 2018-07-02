# python3 -m unittest tests/test_helpers.py
import unittest

class TestHelperMethods(unittest.TestCase):
    def setUp(self):
        if not callable(projectRelativeImport):
            self.fail('You need to bootstrap this test')

        self.Helper = projectRelativeImport('helpers', 'app/util', 'Helper')

    def test_url_validate(self):
        self.assertEqual(self.Helper.url_validate('/noDomainNoFile'), False)
        self.assertEqual(self.Helper.url_validate('/noDomain/file.html'), False)
        self.assertEqual(self.Helper.url_validate('google.com'), False)
        self.assertEqual(self.Helper.url_validate('http://google.com'), True)
        self.assertEqual(self.Helper.url_validate('https://google.com'), True)
        self.assertEqual(self.Helper.url_validate('ftp://domain.com/path'), True)
        self.assertEqual(self.Helper.url_validate('http://domain.com/path/file.html'), True)

if __name__=='__main__':
    unittest.main()
