Steps to run the Automation Suite:
    1. Install all the dependencies using 'pip install -r /path/to/requirements.txt'
    2. Run the automation tests using :
        python3 -m pytest tests/maxPointsTests/ --log-cli-level=INFO  --html=report.html --self-contained-html
    3. Once the tests have completed execution, the results will be available in the below location:
        python-pytest-api-tests-master/report.html

Points to Note:
    The automation suite has 3 tests.
        1. test_points_randomness - Makes 4 call sequentially at a time interval of 1 min each and retieves the id and max points. Incase points or id's are repeated more than 2 times over the 4 calls, the test fails because the random numbers are not distributed evenly assuming that the random number generator is not properly configured.
        2. test_timestamp_update - Cheks if the timestamp key has correct value of the last time the query was made
        3. test_response_and_status_code  - Check for the staus code and if the points is within the range of 1-100 and if the user id is not repeated
