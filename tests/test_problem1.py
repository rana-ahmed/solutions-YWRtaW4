import pytest
from problems.problem1 import measure_depth


class TestMeasureDepth(object):
    @pytest.mark.parametrize(
        "data,expected", [
            (None, []),
            ({}, []),
            ({"key1": 1}, ['key1 1']),
            (
                    {"key1": 1, "key2": {"key3": 1, "key4": {"key5": 4}}},
                    ['key1 1', 'key2 1', 'key3 2', 'key4 2', 'key5 3']
            )
        ]
    )
    def test_depth_data(self, data, expected):
        depth_data = measure_depth(data, [])
        assert depth_data == expected
