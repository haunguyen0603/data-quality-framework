# Data Quality Framework

A small Python framework for validating warehouse-ready datasets before downstream consumption.

## Checks

```text
Schema
  |
  +-- Required columns
  +-- Data types

Completeness
  |
  +-- Null checks

Uniqueness
  |
  +-- Business-key duplicates

Validity
  |
  +-- Range / accepted-value checks

Freshness
  |
  +-- Maximum data age
```

## Why it matters

In real data pipelines, a successful job is not necessarily a successful pipeline. Data should also satisfy explicit quality expectations before it reaches dashboards or AI workflows.

## Example usage

```python
from src.quality_checks import check_required_columns, check_no_nulls

errors = []
errors += check_required_columns(records, {"id", "event_date"})
errors += check_no_nulls(records, {"id", "event_date"})
print(errors)
```
