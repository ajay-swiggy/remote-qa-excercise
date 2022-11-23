# QA Code Excercie

### Problem:
https://www.notion.so/QA-code-exercise-Briefing-91c1dc0fc84048c2848c9d56f4e2677b


### Excercie 1:
Solution to all questions under Excercise 1 are explained in the file [__Excercise-1.md__](Excercise-1.md)

### Excercise 2

__Steps to run the Automation Suite:__

1. Install all the dependencies using 

	```
	pip install -r requirements.txt
	```

2. Run the automation tests using :

	``` 
	cd automation-tests/
	python3 -m pytest  tests/maxPointsTests/ --log-cli-level=INFO  --html=report.html --self-contained-html `
	```
3. Once the tests have completed execution, the results will be available in the below location:
	[automation-tests/report.html](automation-tests/report.html)

__Automated Tests:__

The automation suite has 3 tests.

1. __test_points_randomness__ - Makes 4 call sequentially at a time interval of 1 min each and retieves the id and max points. Incase points or id's are repeated more than 2 times over the 4 calls, the test fails because the random numbers are not distributed evenly assuming that the random number generator is not properly configured.
2. __test_timestamp_update__ - Checks if the timestamp key has correct value of the last time the query was made
3. __test_response_and_status_code__  - Checks for the status code and if the points is within the range of 1-100 and if the user id is not repeated

 
__ __
 __Points to Note__:

The report will have one failure for the test case __test_points_randomness__. This is because the id's and points are repeated too frequenly. The number of accepteble repetitions for both id and points is 2. Incase the number of repetitions exceeds two, the test is considered a failure.