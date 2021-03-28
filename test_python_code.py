import python_code

import unittest

class TestPythonCode(unittest.TestCase):
    def test_func1(self):
        val = python_code.func1()
        self.assertEqual("Hello", val)

if __name__ == "__main__":
    unittest.main()
