from app import DailyReports


def test_new_daily_reports_instance():
    # First parameter of DailyReports could be any date with format mm/dd/yy
    entry = DailyReports("01/01/21", "Australian Capital Territory", "Australia",
                         "Australian Capital Territory, Australia", 118, 3, 114, 1)

    assert entry.date_recorded == "01/01/21"
    assert entry.ProvinceState == "Australian Capital Territory"
    assert entry.CountryRegion == "Australia"
    assert entry.CombinedKeys == "Australian Capital Territory, Australia"
    assert entry.Confirmed == 118
    assert entry.Deaths == 3
    assert entry.Recovered == 114
    assert entry.Active == 1
