import unittest
from hello import get_message

class TestHello(unittest.TestCase):

    def test_get_message(self):
        self.assertEqual(
            get_message(),
            "Jenkins automatically detected my GitHub commit!"
        )

if __name__ == "__main__":
    unittest.main()
