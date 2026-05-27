CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20)
);

insert into contacts (name, phone) values ('Alice', '97976855654'),
('Bob', '97976855655'),
('Charlie', '97976855656');