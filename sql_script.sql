USE liquorSales;

/*Query for a quick overview of the table*/
SELECT *
FROM finance_liquor_sales;

/*Query to get all the columns of the table between the years 2016-2019*/
SELECT *
FROM finance_liquor_sales
WHERE date >= '2016-01-01' and date <='2019-12-31'
ORDER BY date ASC;
