import unittest

from pytype_proto_demo.proto import bugdemo_pb2
from pytype_proto_demo import example


class ExampleTestCase(unittest.TestCase):

    def test_ice_cream_is_delicious(self):
        self.assertEqual(example.evaluate(bugdemo_pb2.Dessert.DESSERT_SUNDAE),
                         "yum!")


if __name__ == "__main__":
    unittest.main()
