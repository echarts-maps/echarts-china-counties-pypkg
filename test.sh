pip freeze
nosetests --with-coverage --cover-package echarts_china_counties_pypkg --cover-package tests  tests docs/source echarts_china_counties_pypkg && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
