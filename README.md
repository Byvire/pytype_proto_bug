This is a small (minimal?) demonstration of an issue when using pytype and protobuf together.

All scripts use relative paths and are supposed to be run from the root dir of
this repository. Otherwise you'll get file-not-found errors and other nonsense.

I suspect there's an easy resolution involving... passing the right flags to
pytype so it notices the .pyi files. And then updating the pytype
documentation.

See TODO issue report.
