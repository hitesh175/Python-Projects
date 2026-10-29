# Python Practice Projects

Two Jupyter notebooks exploring object-oriented programming and PDF document generation.

## Projects

| Notebook | What it demonstrates |
| --- | --- |
| [Hotel Management](Hotel_Management.ipynb) | Hotel/user classes, sample records, filtering, and sorting exercises |
| [Payment Receipt](Payment_Receipt.ipynb) | Styled PDF tables using ReportLab |

## Run locally

```bash
python -m venv .venv
python -m pip install jupyter reportlab
jupyter notebook
```

Activate the virtual environment before installing dependencies. Open either notebook and run its cells in order.

The receipt notebook writes `receipt92.pdf` in the working directory. Its prices and totals are hard-coded sample values; they are not calculated invoice amounts.

## Current limitations

The hotel notebook uses three sample records and has no persistent booking database. Its `Hotel.__lt__` method currently lacks a return statement, so its sorting examples need correction before their results can be relied on.

These are learning exercises rather than complete hotel-management or billing systems.
