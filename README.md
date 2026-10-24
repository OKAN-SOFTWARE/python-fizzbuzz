# FizzBuzz in Python

A beginner-friendly Python program with comments explaining functions, loops,
conditions, and the remainder operator (`%`).

## What it does

For each number from 1 through `n`, the program prints:

- `FizzBuzz` if the number is divisible by both 3 and 5.
- `Fizz` if the number is divisible by 3 only.
- `Buzz` if the number is divisible by 5 only.
- The number itself otherwise.

The combined condition comes first so that numbers such as 15 print `FizzBuzz`.

## Requirements

- Python 3
- No third-party packages are needed.

## Run the program

Download the project, then open a terminal in the folder containing `fizzBuzz.py`:

```powershell
python fizzBuzz.py
```

On Windows, if Python is installed but `python` is not available, try:

```powershell
py fizzBuzz.py
```

The script currently calls `fizz_buzz(12)`, producing:

```text
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
```

## Change the limit

Edit the call at the bottom of `fizzBuzz.py`. For example, to print through 15:

```python
if __name__ == "__main__":
    fizz_buzz(15)
```

Save the file and run it again. The final line will be `FizzBuzz`.

## Use the function from another file

```python
from fizzBuzz import fizz_buzz

fizz_buzz(15)
```

The `if __name__ == "__main__":` guard keeps the example call from running when
the module is imported. The function prints results directly and returns `None`.

Pass a positive integer for `n`. If `n` is zero or negative, the loop prints
nothing. The `int` type hint documents the expected input; it does not validate it.

## Files to upload

- `fizzBuzz.py`: the program and explanatory comments.
- `README.md`: this documentation.
- `.gitignore`: excludes Python caches, virtual environments, and local settings
  when using Git.
