# 05 — Third-Party Packages & `pip`

## What is PyPI?

[PyPI](https://pypi.org) (Python Package Index) is the official repository of third-party Python packages — over 500,000 packages available for free.

## `pip` — Python's package manager

```bash
pip install cowsay          # install
pip install cowsay requests # install multiple
pip list                    # see what's installed
pip show cowsay             # info about a package
pip uninstall cowsay        # remove
pip install --upgrade cowsay # update to latest
```

## `cowsay` example

```bash
pip install cowsay
python3 cowsay_demo.py David
```

```python
import cowsay
cowsay.cow("hello, David")    # ASCII cow speaks
cowsay.trex("RAWR!")          # T-Rex speaks
```

## Try it

```bash
pip install cowsay
python3 cowsay_demo.py YourName
```

## Notable packages from PyPI

| Package | What it does |
|---------|-------------|
| `requests` | HTTP requests / web APIs |
| `flask` | Web framework |
| `pandas` | Data analysis |
| `numpy` | Numerical computing |
| `pillow` | Image processing |
| `rich` | Beautiful terminal output |
| `cowsay` | ASCII animals that talk 🐄 |
