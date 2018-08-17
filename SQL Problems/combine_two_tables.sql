SELECT FirstName, LastName, City, State
FROM Person P
LEFT OUTER JOIN Address a
ON p.PersonID = a.PersonID;