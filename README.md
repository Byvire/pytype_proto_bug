This is a small (minimal?) demonstration of an issue when using pytype and protobuf together.

To use it, clone this repo, `cd` into it (this, the folder with the README), and
do `pip3 install -e .`. Then you'll be able to run the unit test and evaluate
stuff with pytype. (Use virtualenvwrapper or venv if you don't want to install
stuff globally. You probably know this but you're used to using BUILD...)

All scripts use relative paths and are supposed to be run from the root dir of
this repository. Otherwise you'll get file-not-found errors and other nonsense.

I suspect there's an easy resolution to the bug involving... passing the right
flags to pytype so it notices the .pyi files. And then updating the pytype
documentation.

See https://github.com/google/pytype/issues/1590
