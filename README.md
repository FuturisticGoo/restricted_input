# Restricted Input

## Overview

A way of imposing restrictions in `input()`.  

For example, if you want the user to only enter numbers, you could use this. Only want uppercase letters? Works here.  

It uses msvcrt.getch/alternative in *nix to get the keystroke and check it in real time.  

## Installation

Install [restricted_input](https://pypi.org/project/restricted_input/) from [pypi](https://pypi.org/) using:

```bash
pip install restricted_input
```

## How to use it

Import it

```python
from restricted_input import r_input
```

`r_input` is the function which can be used instead of `input()`  

It has three arguments

```python
variable = r_input(prompt, input_type, exclude)
```

* `prompt`: is the prompt to be given for the input dialog. `string`  

* `input_type` : is the type of data to which the input should be restricted to. `string`  

  It can be 

  *  `"normal"`: normal text

  * `"string_all"`: Allows only string, space is not allowed
  *  `"string_upper"`: Allows only uppercase string, space is not allowed
  *  `"string_lower"`: Allows only lowercase string, space is not allowed
  * `"specials"` Allows only special characters - `` ~ ! @ # $ % ^ & * ( ) - _ = + [ { ] } ; : ' " , < . > / ? \ |`. Space not included
  *  `"integer"`: Allows only integers, doesn't allow `-`, `.` or space
  *  `"float"` : Allows only integers, including `.` single time. Space or `-` not included
  * `"version"`: Allows only integers, including `.` multiple times. Space or `-` not included 
  *  `"nothing"` .    Obviously allows nothing. Useful in scenarios where you need only a limited number of characters.

  To get the list of input_types:

  ```python
  from restricted_input import get_input_types
  print(get_input_types)
  ```

* `exclude`: is the argument for allowing certain characters.  `string or list`

   For example, if you want to allow hyphens in `integers`, you can use

  ```python
  r_input("Enter the number: ", "integer", "-")
  ```

  If you want to allow input of the character `v`, `a`,`b` and `g` in version type input, use:

  ```pyth
  r_input("Enter the version: ", "version", "vabg")
  # Or
  r_input("Enter the version: ", "version", ["v", "a", "b", "g"])
  ```

## Example

![Example GIF](https://raw.githubusercontent.com/FuturisticGoo/restricted_input/main/example/example.gif)

## Issues/limitations

* It will not work in some IDLEs like Spyder or PyCharm. This is because some IDLEs emulate a terminal which might not work with this module. Try to run the program in external terminal.

* You tell me!

  

## Contributing

If you need help, don't hesitate to open an issue. Pull requests are welcome, but please state the reason for it.

## License

This project is under [MIT License](https://choosealicense.com/licenses/mit/)