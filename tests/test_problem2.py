import pytest
from problems.problem2 import measure_depth, Person


person_a = Person("A", "B", "C")
person_b = Person("E", "F", {"mega": 5})


class TestMeasureDepth(object):
    @pytest.mark.parametrize(
        "data,expected", [
            (None, []),
            ({}, []),
            ({"key1": 1}, ['key1 1']),
            (
                {"key1": 1, "key2": {"key3": 1, "key4": {"key5": person_a, "key6": person_b}}},
                ['key1 1', 'key2 1', 'key3 2', 'key4 2', 'key5 3', 'first_name 4', 'last_name 4',
                 'father 4', 'key6 3', 'first_name 4', 'last_name 4', 'father 4', 'mega 5']
            )
        ]
    )
    def test_depth_data(self, data, expected):
        depth_data = measure_depth(data, [])
        assert depth_data == expected
