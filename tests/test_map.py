# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Map


def test_city_map():
    map = Map("海淀示例", width=1200, height=600)
    map.add("", [], [], maptype='海淀区',
            visual_text_color='#000')
    # To avoid potential pinyin crash, all cities have a province prefix
    html = map._repr_html_()
    assert "zhi2xia2_bei3jing1_hai3dian4" in html
    print(html)
    assert "nbextensions/echarts-china-counties-js" in html
