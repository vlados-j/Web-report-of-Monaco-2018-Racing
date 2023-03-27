# Web report of Monaco 2018 Racing

Web application was written using Flask and the report package from my project - https://github.com/vlados-j/Report-of-Monaco-2018-Racing.

The application has a few routes:

http://localhost:5000/report shows common statistics of F1 racers

http://localhost:5000/report/drivers/ shows a list of driver's names and abbreviations. You can click on the driver and you'll be redirected to the info about the driver

http://localhost:5000/report/drivers/?driver_id=SVF shows info about a driver

Also, each route can get the order parameter:

http://localhost:5000/report/drivers/?order=desc

For html has been used the jinja2 package.
Also, the application has tests using pytest.
