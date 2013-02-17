all:
	rm -rf build pyltsv.egg-info pyltsv/pyltsv.so pyltsv.so && python setup.py build && python setup.py test
build:
	python setup.py build
test:
	python setup.py test
clean:
	rm -rf build pyltsv.egg-info pyltsv/pyltsv.so pyltsv.so
benchmark:
	python benchmark/benchmark.py

.PHONY: all, build, clean, test, benchmark
