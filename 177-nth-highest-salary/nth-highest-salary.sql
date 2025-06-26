CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
IF N < 1 THEN
    RETURN  QUERY(SELECT NULL:: INT AS SALARY);
ELSE
    RETURN QUERY (
    -- Write your PostgreSQL query statement below.
        select distinct 
        Employee.Salary from
        Employee order by salary DESC
        limit 1     
        offset N-1
    );
    END IF;
END;
$$ LANGUAGE plpgsql;