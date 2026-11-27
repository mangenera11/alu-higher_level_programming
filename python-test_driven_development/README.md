# python-test_driven_development

Python functions with documentation and tests: interactive doctests in
`tests/*.txt` and unit tests with `unittest`.

## Files

- `0-add_integer.py`: adds two integers
- `2-matrix_divided.py`: divides all elements of a matrix
- `3-say_my_name.py`: prints a name
- `4-print_square.py`: prints a square with `#`
- `5-text_indentation.py`: prints text with line breaks after `.`, `?` and `:`
- `6-max_integer.py`: finds the max integer in a list
- `tests/6-max_integer_test.py`: unit tests for `max_integer`

## Usage

    python3 -m doctest -v ./tests/0-add_integer.txt
    python3 -m unittest tests.6-max_integer_test
