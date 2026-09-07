from __future__ import annotations

from collections.abc import Iterable


def check_required_columns(records: list[dict], required: set[str]) -> list[str]:
    if not records:
        return ["dataset_empty"]
    present = set(records[0].keys())
    return [f"missing_column:{column}" for column in sorted(required - present)]


def check_no_nulls(records: Iterable[dict], columns: set[str]) -> list[str]:
    errors: list[str] = []
    for index, record in enumerate(records):
        for column in columns:
            if record.get(column) is None:
                errors.append(f"null_value:row={index}:column={column}")
    return errors


def check_unique(records: Iterable[dict], key_columns: tuple[str, ...]) -> list[str]:
    seen: set[tuple[object, ...]] = set()
    errors: list[str] = []
    for index, record in enumerate(records):
        key = tuple(record.get(column) for column in key_columns)
        if key in seen:
            errors.append(f"duplicate_key:row={index}:key={key}")
        seen.add(key)
    return errors
