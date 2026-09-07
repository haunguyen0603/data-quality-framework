from src.quality_checks import check_no_nulls, check_required_columns, check_unique


def test_required_columns():
    assert check_required_columns([{"id": 1}], {"id"}) == []
    assert check_required_columns([{"id": 1}], {"id", "date"}) == ["missing_column:date"]


def test_null_check():
    assert check_no_nulls([{"id": 1}], {"id"}) == []
    assert check_no_nulls([{"id": None}], {"id"}) == ["null_value:row=0:column=id"]


def test_unique():
    rows = [{"id": 1}, {"id": 1}]
    assert check_unique(rows, ("id",)) == ["duplicate_key:row=1:key=(1,)"]
