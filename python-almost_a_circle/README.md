# python-almost_a_circle

Python classes `Base`, `Rectangle` and `Square` with validated
attributes, plus unit tests for every file.

## Files

- `models/base.py`: `Base`, which manages the `id` attribute
- `models/rectangle.py`: `Rectangle`, with validation, `area`, `display`,
  `__str__` and `update`
- `models/square.py`: `Square`, a `Rectangle` with equal width and height
- `tests/test_models/`: unit tests for each class

## Usage

    python3 -m unittest discover tests
