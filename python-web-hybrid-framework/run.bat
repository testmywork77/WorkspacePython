pytest -s -v -m "sanity" --html=./Reports/report.html testCases/test_sample.py --browser chrome
rem pytest -s -v -m "smoke" --html=./Reports/report.html testCases/test_sample.py --browser chrome
rem pytest -s -v -m "regression" --html=./Reports/report.html testCases/test_sample.py --browser chrome
rem pytest -s -v -m "smoke and regression" --html=./Reports/report.html testCases/test_sample.py --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases/test_sample.py --browser chrome