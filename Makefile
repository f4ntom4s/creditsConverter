run:
	python creditsConverter/creditsConverter.py $(FILE)

test:
	python tests/parse_tests.py
