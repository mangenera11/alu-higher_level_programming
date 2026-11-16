# Python - Input/Output

This project covers reading and writing files in Python.

## Files

- `0-read_file.py`: function `read_file(filename="")` that reads a UTF8 text file and prints it to stdout.
- `1-write_file.py`: function `write_file(filename="", text="")` that writes a string to a UTF8 text file and returns the number of characters written.
- `2-append_write.py`: function `append_write(filename="", text="")` that appends a string to a UTF8 text file and returns the number of characters added.
- `3-to_json_string.py`: function `to_json_string(my_obj)` that returns the JSON representation of an object.
- `4-from_json_string.py`: function `from_json_string(my_str)` that returns the object represented by a JSON string.
- `5-save_to_json_file.py`: function `save_to_json_file(my_obj, filename)` that writes an object to a text file using its JSON representation.
- `6-load_from_json_file.py`: function `load_from_json_file(filename)` that creates an object from a JSON file.
- `7-add_item.py`: script that adds all arguments to a Python list and saves them to `add_item.json`.
- `8-class_to_json.py`: function `class_to_json(obj)` that returns the dictionary description of an object for JSON serialization.
- `9-student.py`: class `Student` with `first_name`, `last_name`, `age` and a `to_json()` method that returns its dictionary description.
- `10-student.py`: class `Student` whose `to_json(attrs=None)` returns its dictionary description, filtered to the attribute names in `attrs` when given a list of strings.
- `11-student.py`: class `Student` with `to_json(attrs=None)` and `reload_from_json(json)` to serialize and rebuild its attributes.
- `12-pascal_triangle.py`: function `pascal_triangle(n)` that returns a list of lists of integers representing Pascal's triangle of `n`.
