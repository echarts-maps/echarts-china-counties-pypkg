from echarts_china_counties_pypkg import Pypkg


def test_pypkg():
    __pkg__ = Pypkg()
    assert __pkg__.js_extension_path.endswith("resources")
