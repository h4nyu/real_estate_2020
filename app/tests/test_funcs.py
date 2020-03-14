import pytest
import pandas as pd
from app.encoders import (
    parse_age,
    parse_floor,
    parse_quater,
    parse_erea,
    parse_duration,
    kfold,
)

test_df = pd.read_csv("/store/data/test_data.csv")


@pytest.mark.parametrize(
    "test_input,expected",
    [("昭和30年", 1955), ("平成3年", 1991), ("平成10年", 1998), (None, None)],
)
def test_parse_age(test_input, expected):
    assert expected == parse_age(test_input)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("１K", {"dinning": 0, "kitchen": 1, "room": 1, "living": 0, "storage": 0}),
        ("２LDK", {"dinning": 1, "kitchen": 1, "room": 2, "living": 1, "storage": 0}),
        ("１K＋S", {"dinning": 0, "kitchen": 1, "room": 1, "living": 0, "storage": 1}),
        ("１R", {"dinning": 0, "kitchen": 0, "room": 1, "living": 0, "storage": 0}),
        ("スタジオ", {"dinning": 0, "kitchen": 0, "room": 1, "living": 0, "storage": 0}),
        (
            None,
            {
                "dinning": None,
                "kitchen": None,
                "room": None,
                "living": None,
                "storage": None,
            },
        ),
    ],
)
def test_parse_floor(test_input, expected):
    assert expected == parse_floor(test_input)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("2018年第３四半期", {"year": 2018, "quarter": 3}),
        ("2019年第１四半期", {"year": 2019, "quarter": 1}),
    ],
)
def test_parse_query(test_input, expected):
    assert expected == parse_quater(test_input)


@pytest.mark.parametrize(
    "test_input,expected", [("5000㎡以上", 5000), ("24", 24), ("10m^2未満", 10),],
)
def test_parse_erea(test_input, expected):
    assert expected == parse_erea(test_input)


@pytest.mark.parametrize(
    "test_input,expected", [("11", 11), ("1H?1H30", 60), ("1H30?2H", 120),],
)
def test_parse_duration(test_input, expected):
    assert expected == parse_duration(test_input)


def test_kfold():
    df = pd.read_csv("/store/preprocess-train_data.csv")
    #  df = pd.DataFrame([
    #      {"year":2018, "quarter": 2},
    #      {"year":2018, "quarter": 2},
    #      {"year":2018, "quarter": 2},
    #      {"year":2018, "quarter": 2},
    #      {"year":2018, "quarter": 2},
    #  ])
    kfold(df)
    #  print(df)