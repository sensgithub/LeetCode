/* Write your PL/SQL query statement below */

Select Person.firstname, Person.lastname, Address.city, Address.state
from Person left join Address
using(personId)