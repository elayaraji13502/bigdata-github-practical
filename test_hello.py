import unittest
from hello import get_message

class TestHello(unittest.TestCase):

    def test_get_message(self):
        self.assertEqual(
            get_message(),
            "Hello from Big Data CI/CD Pipeline!"
        )

if __name__ == "__main__":
    unittest.main()
