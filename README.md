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

**Total: 60 programs.** Files follow the original assignment and question order. Document line breaks and indentation have been repaired to make separate Python files executable.

## Notes about incomplete or corrected source

- **Assignment 1, Q4:** The manual gives `sqrt(b*b) - (4*c*a)` as the expression passed to `math.sqrt`. It has been preserved as written; it is not the standard quadratic discriminant and may fail for some inputs.
- **Assignment 5, Q6:** The supplied manual omits the first-set input statement, but the remaining code refers to `s1`. The file marks this missing section rather than guessing it.
- **Assignment 6, Q5:** The manual defines `Fibonacci` but calls `fibonacci`; the name is made consistent.
- **Assignment 7, Q5:** The manual maps over `l2` for the tuple conversion; this is changed to `t1` to match the question.
- **Assignment 8, Q3:** The two-column page layout interleaves separate examples. They have been separated, and the clipped sorting statement is reconstructed as `np.sort(arr4)`.

## Run a program

```bash
python Assignment-01/Q01_Arithmetic_Operations.py
```

## Install dependencies

```bash
pip install -r requirements.txt
```

Python 3.x is required. Third-party packages are listed in `requirements.txt`.
