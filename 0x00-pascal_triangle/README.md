# alx-interview
## 0x00. Pascal's Triangle

This project involves creating a function that generates Pascal's Triangle up to a given number of rows.

### Requirements

- Python 3.x
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Usage

To use the function, import it into your script and call it with the desired number of rows:

```python
from pascal_triangle import pascal_triangle

print(pascal_triangle(5))
```

### Example

For `n = 5`, the function should return:

```
[
    [1],
    [1, 1],
   [1, 2, 1],
  [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
```

### Author

Muktr