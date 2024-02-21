from __future__ import annotations

from pytype_proto_demo.proto import bugdemo_pb2

def evaluate(dessert: bugdemo_pb2.Dessert) -> str:
    if dessert == bugdemo_pb2.Dessert.DESSERT_SUNDAE:
        return "yum!"
    if dessert == bugdemo_pb2.Dessert.DESSERT_SHRIMP_SMOOTHIE:
        return "gross!"
    return "dessert unidentified, presumed yucky"
