# Python Programming Lab

A collection of Python lab programs organised assignment-wise, following the college Python Programming Lab manual.

## Assignments

| Folder | Topics | Programs |
|---|---|---:|
| Assignment-01 | Basic Python, arithmetic operations and number conversions | 8 |
| Assignment-02 | Conditions, loops, numbers and strings | 6 |
| Assignment-03 | Prime numbers, factorial, leap year and strings | 6 |
| Assignment-04 | Lists, functions, Fibonacci and recursion | 6 |
| Assignment-05 | Dictionaries and sets | 6 |
| Assignment-06 | Matrices and lambda functions | 6 |
| Assignment-07 | map(), lambda and lists | 6 |
| Assignment-08 | NumPy | 5 |
| Assignment-09 | Pandas | 4 |
| Assignment-10 | Matplotlib and data visualisation | 5 |

**Total: 58 programs.** The `Assignment-01` to `Assignment-10` folders retain the manual-based source versions. Improved versions of programs with identified issues are provided in matching folders under `Corrected/`.

## Corrected versions

The `Corrected/` directory contains versions with input validation, boundary-case handling, and fixes for identified logic errors. Original files are retained in the assignment folders for comparison.

Notable corrections include quadratic roots, invalid triangle sides, division by zero, grade validation, perfect-number zero handling, consonant counting, prime-factor integer division, whitespace-safe word processing, list-size validation, Fibonacci boundary cases, safe dictionary input, missing set input, rectangular matrix transpose, and empty-list ratio handling.

**Manual ambiguities:** Assignment 5, Q6's missing first-set input is supplied as an inferred line and is commented in the corrected file. Assignment 8, Q3's clipped sorting example is reconstructed as `np.sort(arr4)`.

## Run a program

Original:
```bash
python Assignment-01/Q01_Arithmetic_Operations.py
```

Corrected:
```bash
python Corrected/Assignment-01/Q04_Quadratic_Equation_Roots.py
```

## Install dependencies

```bash
pip install -r requirements.txt
```

Python 3.x is required. NumPy, Pandas, and Matplotlib are used in Assignments 8–10.
