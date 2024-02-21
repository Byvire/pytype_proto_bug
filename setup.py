from distutils.core import setup

setup(
    name='pytype_proto_demo',
    version='1.0',
    author='Oliver Kisielius',
    packages=['pytype_proto_demo'],
    install_requires=[
        'protobuf',
        'pytype',
    ],
)
