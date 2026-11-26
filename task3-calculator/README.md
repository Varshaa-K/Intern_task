# Task 3 - Office Commute Calculator

## Overview

A Python command-line calculator that estimates commute and meal spending for a
planned office stint, checks the available card and wallet balances, and
calculates the final date.

## Requirements

- Python 3, with the standard library's `datetime` and `decimal` modules.
- No additional packages are required.

## How to Run

From this directory, run:

```bash
python calculator.py
```

Enter the name, balances, per-day meal and one-way travel costs, number of
working days, and first office date when prompted. Monetary amounts must be
positive and may have up to two decimal places. The date must be a valid date
in `dd/mm/yyyy` format, and the number of days must be a positive integer.

See [sample_run.txt](sample_run.txt) for a complete example.

## Design Decisions

- Input collection, calculation, and presentation are separated into
  `collect_inputs`, `calculate_commute`, and `display_summary`.
- `Decimal` is used instead of floating-point arithmetic for money.
- Travel is charged once per office day, as specified. To model a return
  commute, the travel cost can be doubled in the calculation.
- The end date adds `Days - 1` calendar days. Weekends and holidays are not
  skipped.
- Invalid input produces a concise error message instead of a traceback.
- Each balance is checked separately, and any shortfall is shown as an amount.

## Effort

Time spent was not tracked. The task brief estimates a few hours of focused
work for implementation, documentation, and verification.
