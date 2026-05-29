from data_pipeline import transform_data

def test_transform_data():
    # If we pass "test", we expect "TEST" back
    assert transform_data(["test"]) == ["TEST"]