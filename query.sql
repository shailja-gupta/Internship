SELECT * FROM capston_project.table1;
-- Query 1
select Rental_Price from table1 order by Rental_Price ASC;
-- Query 2
SELECT city, state_code, AVG(Rental_Price)
FROM table1
WHERE city in (select DISTINCT city from table1) group by city, State_Code;
-- Query 3
SELECT * FROM capston_project.table1;
SELECT Address, City, Deposit
FROM table1
ORDER BY Deposit DESC limit 5;
-- Query 4
SELECT * FROM capston_project.table1;
SELECT count(Country) from table1;

-- Query 5
SELECT * FROM capston_project.table1;
select * from table1
Where Rental_Price > (select AVG(Rental_Price) from table1);

-- Table 2 Query

SELECT * FROM capston_project.table2;
Select No_of_Bed, AVG(Area) from table2
group by No_of_Bed;

-- Q2
SELECT * FROM capston_project.table2;
Select * from table2
Where Bathroom > 1 and Pet_allowed="yes";

-- Q3
SELECT * from table2
ORDER BY Area DESC limit 3;

-- Q4
select No_of_Bed, Bathroom, Count(*) from table2
group by No_of_Bed, Bathroom;

-- Q5

select * from table2
Where Pet_allowed="yes"
order by Area desc limit 1;

--- Table 3
-- Q1
SELECT * FROM capston_project.table3;
select * from table3
where Washer and AC="yes"
order by Sno;

SET SQL_SAFE_UPDATES=0;
update table3 SET Storage='No' where Sno = '4' and Storage = 'yes';
SET SQL_SAFE_UPDATES=1;
commit;
SELECT * FROM capston_project.table3;

-- Q2
Select * from table3
where Hardwood_floors="yes" and Roofdeck='No' and Storage='No'
Order By Sno Desc;

-- Q3
select * from table3
where AC='yes' and Parking='yes' and Fireplace='yes' and Dishwasher= 'yes'
Order by Sno;

-- Q4
select Roofdeck, Storage, Count(*) from table3
where Roofdeck='No' and Storage='No';

-- Q5
select Parking, Fireplace, Dishwasher Count(*) from table3
where Parking='yes' and Fireplace='yes' or Dishwasher='yes';

-- Join Query
-- Q1
SELECT * from table1, table2
WHERE Area >= (SELECT AVG(Area) from table2);

-- Q2
SELECT table2.Pet_allowed, table2.No_of_Bed
FROM table2
WHERE table2.Pet_allowed = 'yes'
AND table2.No_of_Bed > 3;

-- Q3
select table2.Bathroom, table3.AC
from table2, table3
where table2.Bathroom > 2 and table3.AC = 'yes';

