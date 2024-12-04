# UTF-8 Validation

## Description
This project involves writing a method that determines if a given data set represents a valid UTF-8 encoding.

## Requirements
- Python 3.x

## Files
- `0-validate_utf8.py`: Contains the `validUTF8` function.
- `README.md`: Project documentation.

## Usage
To use the `validUTF8` function, import it into your Python script and pass a list of integers representing the data set to be validated.

```python
from 0-validate_utf8 import validUTF8

data = [197, 130, 1]
print(validUTF8(data))  # Output: True
```

## Testing
To run the tests, execute the following command:

```bash
python3 -m unittest discover tests
```

## Author
Muktr