## E1 - Implement external API

UPDATE: 2018-03-28: We found out that the fixer.io API is no more free for the needed full use:
1. You can try to do an alternative version of that task (implement an API, download data into a well-designed database schema, show your SQL skills)
2. There is a way to solve the task with the limited capabilities of the free fixer.io API. But it takes more time and you can not load years of data, so prepare the example for some months or weeks…
3. Use exchangeratesapi.io.

- at http://fixer.io/ you find an exchange API for currency rates on a daily bases
- load all exchanges for the current year into a database
- ensure that you can easily convert multiple source (target) prices into at least 2 base currencies: USD or EUR, example target data:
```
SELECT CAST('2018-01-01' AS DATE) AS date_date, CAST('EUR' AS CHAR(3)) AS target_currency, CAST('11.11' AS NUMERIC(14,4)) AS a_price UNION
SELECT CAST('2018-02-01' AS DATE) AS date_date, CAST('GBP' AS CHAR(3)) AS target_currency, CAST('12.12' AS NUMERIC(14,4)) AS a_price UNION
SELECT CAST('2018-03-01' AS DATE) AS date_date, CAST('RUB' AS CHAR(3)) AS target_currency, CAST('333.33' AS NUMERIC(14,4)) AS a_price;
```
Goal:
- please show how you downloaded the data (any observations, pitfalls?)
- show and explain the data model you created
- show that you can convert multiple source (target) prices from a query result (eg. SQL “data example” above), into one base price within one query
Background - Use case:
- you have a dashboard with currency-related numbers.
- you have different users for that dashboard: All local dealers (eg. Russia, Europe, US), but also the boss of that dealers
- All use the same dashboards, but want to see their own numbers (the numbers are in the original values and currency stored) in RUB, EUR and $, etc.
- But the Boss wants to see over ALL locations the numbers in  EUR (or $)
- ToDo: sketch out a (data) solution, that would solve this problem (do NOT build the dashboard, pls. build the load into a (data) storage to get all the raw data for calculation, sketch out the problem and show solution (eg. with SQL) how you calculate on the fly into the two base currencies EUR from some dummy data (eg. data example SELECT above) from RUB, GBP, whatever)
