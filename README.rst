Pyltsv
======

Dead simple LTSV parser written in Python C Extension.

- `Repository <https://github.com/heavenshell/py-pyltsv`_


This is a experimental library.

If you want more stable ltsv library, recommend to use `ltsv <http://pypi.python.org/pypi/ltsv>`_.

Installation
------------

::

  $ virtualenv --distribute pyltsv_sample
  $ source pyltsv_sample/bin/activate
  $ git clone https://github.com/heavenshell/py-pyltsv.git
  $ python setup.py build
  $ python setup.py install

Usage
-----

::
  >>> from pyltsv import parse_file, parse_line
  >>> parse_file("ip:127.0.0.1\thost:localhost")
  {'ip': '127.0.0.1', 'host': 'localhost'}


Benchmark
---------
Pyltsv is written in C extension.
So it's faster than pure Python imprementation.

Benchmark script is in `benchmark/benchmark.py`.

============== =============
Imprementation Score
============== =============
Pure Python    111.830234528
C Extension    80.0704956055
============== =============

If you want to run benchmark script, copy `pyltsv.so` from `build` directory.

::
  $ python setup.py build
  $ cp build/lib.macosx-10.8-x86_64-2.7/pyltsv/pyltsv.so benchmark/.
  $ cd benchmark
  $ python benchmark.py


Contributing
------------
1. Fork it
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

