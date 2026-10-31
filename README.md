# Python Learning Lab

A collection of beginner-friendly Python exercises and data-preparation examples. The repository is organized into Python fundamentals and data preprocessing and cleaning; it is a learning workspace, not a packaged application.

## What's inside

### `Basic-fundamental/`

Standalone scripts covering variables and input, arithmetic, conditionals, loops, functions, lambda expressions, lists, tuples, sets, dictionaries, strings, and file handling. It also includes small exercises such as a shopping cart, palindrome check, and password check, plus text files used by examples.

### `DataPreprocessingAndCleaning/`

Python scripts and Jupyter notebooks demonstrating dataset inspection and cleaning, including missing values, duplicates, column names, data types, and loading CSV, TSV, JSON, and SQLite data. The folder includes sample datasets and a smartwatch health dataset.

The `data-gathering/` subfolder contains another set of CSV, JSON, SQLite, and TMDB API loading examples with its own copies of the sample data files.

## Requirements

- Python 3
- `pandas` for the data processing and loading scripts
- `requests` for the TMDB API example
- Jupyter Notebook or JupyterLab to run the `.ipynb` notebooks

The fundamental exercises mainly use Python's standard library. There is no dependency manifest in this repository, so install the packages needed for the examples you plan to run:

```bash
python3 -m pip install pandas requests
```

## Running examples

Run the fundamental scripts from their directory:

```bash
cd Basic-fundamental
python3 data_structure.py
```

Run data-processing scripts from `DataPreprocessingAndCleaning`, so their relative `data/` paths resolve:

```bash
cd DataPreprocessingAndCleaning
python3 load-data-from-csv.py
python3 load-data-from-json.py
python3 load-data-from-sql.py
```

The examples in `data-gathering/` use that directory's own `data/` folder; run them from there:

```bash
cd DataPreprocessingAndCleaning/data-gathering
python3 load-data-from-csv.py
```

The SQLite examples recreate the `employees` table in the bundled `data/sample.db` file. Use a copy if you need to preserve its existing contents.

## TMDB API example

The TMDB scripts require a TMDB API key in the `TMDB_API_KEY` environment variable. From `DataPreprocessingAndCleaning`, set the variable and run:

```bash
export TMDB_API_KEY="your-tmdb-api-key"
python3 load-data-from-tmdb-api.py
```

For examples in `data-gathering/`, run the corresponding script from that directory instead. The scripts fetch popular movie data from TMDB; the CSV export line is currently commented out.

---

Auther: Navneet Tyagi (Software Engineer)
