-- SQLite
SELECT *
FROM users;


update users
set Admin = "yes"
where id = "12";

Delete from users where id = 3;

CREATE TABLE User_Settings
(
    user_id varchar(50),
    emailAddress varchar(250)
)

select *
from User_Settings;