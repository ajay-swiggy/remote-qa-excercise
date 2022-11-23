
# Exercise 1


## 1. What kind of tests would you conduct to make sure it was well built? 

The following tests should be considered: 

#### In Dev environment
    Unit tests

#### In QA envronment
    1. Automated Functional End to End tests- to check the correctness of data by verifying from DB
    2. Security testing to make sure DB values are secured, eg. Making sure the database is not using the default acccount, SQL Injection attacks
    3. Performance test to make sure the service can handle large number of users and send a response within milli seconds

#### In Prod Environment:
    A sanity check in Prod to make sure the app is connected to right data base and configs are correct and the feature is working   
    correctly

## 2. In your opinion what would be the 3 more important things to test here?
    
    1. Functional End to End Test - A thorough end to end functional test should be done to Verify the correctness of data and if the response is as per the specification.
    2. Security Test - Preventing DOS Attack, SQL Injection as the service relies heavily on Database.
    3. Performance - Making sure the app can handle a large number of users and can send a reponse within milli seconds

## 3. What would you improve in this spec?
    
	1. Make the timestamp human readable by mentioning the time zone - (eg:  Sat, 19 Nov 2022, 07:48:31.317513 GMT )
	2. Have a query Param to be able to fetch any range of the leaderboard, not just the top two results  (eg: ?user_count=15)
	3. Update the URL format - The URL should have a Base URL and meaningful Endpoint name ( eg: http://44.204.29.211:4000/getMaxPoints)
	4. Display the number of seconds until the next DB refresh, so that users can know when the points will be refreshed
	5. Have a POST endpoint for allowing users to Add users and points
	6. Have a endpoints that will Get points of any given user using the user id. (eg: http://44.204.29.211:4000/gerPoints?id=4)
	7. Specify the performance requirements. (Eg: With 100 parallel requests, expected response time is 100ms)
	8. For the First call ever made, we need to specify what the time stamp should be sent

## Additional Test cases to be tested

	1. Verify if the points is updated every 60 seconds and if it is in the range of 1 to 100 
	2. Verify that the random points are spread evenly throughout the range and are not repeated too frequently
	3. Compare with the Database if the top 2 points returned 
	4. Check that only 2 users are returned.
	5. For the first ever call made to this API, what will be the Time Stamp
	6. Verify that the database can handle multiple parallel calls
	7. Verify the response code, payload, header for successful and Error cases
	8. Verify that users cannot modify the Database and  will not be able to add or remove entries using put/post/delete endpoints.
	9. Verify that SQL injection is not possible
	10. Verify that DB information is not shared in logs or error message and the database does not use the default account
	11. Run load tests and verify the app performance under normal and heavy load
	12. Clear the database and re-start the app, make sure that the DB entries are created
	13. Make sure entries persist even after DB restart
	14. Test the service when the DB is down