/*
Problem: 175. Combine Two Tables
Category: Database

Description: Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

Algorithm:
- Use a LEFT JOIN from Person to Address matching on personId
- This ensures all people are included, with NULL for missing address information

Complexity:
- Time: O(n + m)
- Space: O(n)
*/

SELECT 
    p.firstName, 
    p.lastName, 
    a.city, 
    a.state
FROM Person AS p
LEFT JOIN Address AS a
    ON p.personId = a.personId;
