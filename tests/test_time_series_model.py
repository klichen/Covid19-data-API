from app import TimeSeries


def test_new_time_series_instance():
    #Last parameter of TimeSeries could be Confirmed, Deaths, or Recovered
    entry = TimeSeries("", "Albania", "05/25/21", 25000, "Confirmed")

    assert entry.ProvinceState == ""
    assert entry.CountryRegion == "Albania"
    assert entry.date_recorded == "05/25/21"
    assert entry.quantity == 25000
    assert entry.case_type == "Confirmed"
