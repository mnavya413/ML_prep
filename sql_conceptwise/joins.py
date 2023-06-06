1.SELECT s.name as "Salesman",
c.cust_name, c.city
FROM customer c
JOIN salesman s
ON c.salesman_id = s.salesman_id

2.SELECT o.ord_no, o.purch_amt,
c.cust_name, c.city
FROM orders o, customer c
WHERE o.customer_id = c.customer_id
AND o.purch_amt BETWEEN 500 and 2000

3.SELECT s.name AS "Salesman", s.commission,
c.cust_name AS "Customer Name", c.city
FROM customer c, salesman s
WHERE c.salesman_id = s.salesman_id

4.SELECT s.name AS "Salesman", s.commission,
c.cust_name AS "Customer Name", c.city
FROM customer c, salesman s
WHERE c.salesman_id = s.salesman_id
AND s.commission > 0.12

5.SELECT s.name AS "Salesman", s.city, s.commission,
c.cust_name AS "Customer Name", c.city
FROM customer c
JOIN salesman s
ON c.salesman_id = s.salesman_id
WHERE c.city != s.city
AND s.commission > 0.12

6.SELECT o.ord_no, o.ord_date, o.purch_amt,
c.cust_name AS "Customer Name", c.grade, s.name AS "Salesman", s.commission
FROM orders o
INNER JOIN customer c
ON o.salesman_id = c.salesman_id
INNER JOIN salesman s
ON s.salesman_id = c.salesman_id

7.SELECT *
FROM orders
NATURAL JOIN customer
NATURAL JOIN salesman

8.SELECT c.cust_name AS "Customer Name", c.grade, c.city AS "Customer city",
s.name AS "Salesman", s.city AS "Salesman city"
FROM customer c
JOIN salesman s
ON c.salesman_id = s.salesman_id
Order by c.customer_id

9.SELECT c.cust_name AS "Customer Name", c.grade, c.city AS "Customer city",
s.name AS "Salesman", s.city AS "Salesman city"
FROM customer c
JOIN salesman s
ON c.salesman_id = s.salesman_id
WHERE c.grade < 300
Order by c.customer_id

10.SELECT c.cust_name AS "Customer Name", c.city AS "Customer city",
o.ord_no AS "order number", o.ord_date, o.purch_amt AS "order amount"
FROM customer c
JOIN orders o
ON c.customer_id = o.customer_id
Order by o.ord_date

11.SELECT c.cust_name, c.city,
o.ord_no, o.ord_date, o.purch_amt AS "order amount"
s.name, s.commission
FROM customer c
LEFT OUTER JOIN orders o
ON c.customer_id = o.customer_id
LEFT OUTER JOIN salesman s
ON s.salesman_id = o.salesman_id

12.SELECT a.cust_name, a.city, a.grade,
b.name AS "Salesman", b.city
FROM customer a
RIGHT OUTER JOIN salesman b
ON b.salesman_id = a.salesman_id
ORDER BY b.salesman_id

13.SELECT a.cust_name, a.city, a.grade,
b.name AS "Salesman",
c.ord_no, c.ord_date, c.purch_amt
FROM customer a
RIGHT OUTER JOIN salesman b
ON b.salesman_id = a.salesman_id
RIGHT OUTER JOIN orders c
ON c.customer_id = a.customer_id

14.SELECT a.cust_name, a.city, a.grade,
b.name AS "Salesman",
c.ord_no, c.ord_date, c.purch_amt
FROM customer a
RIGHT OUTER JOIN salesman b
ON b.salesman_id = a.salesman_id
LEFT OUTER JOIN orders c
ON c.customer_id = a.customer_id
WHERE c.purch_amt >= 2000
AND a.grade IS NOT NULL

15.SELECT a.cust_name, a.city, b.ord_no,
b.ord_date, b.purch_amt AS "Order Amount"
FROM customer a
LEFT OUTER JOIN orders b
ON a.customer_id = b.customer_id
