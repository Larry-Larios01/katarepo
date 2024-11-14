create  table ticketit 
(
 id int primary key,
 subject varchar(30),
 content text, 
 html text,
 status_id int,
 priority_id int, 
 user_id int,
 agent_id int,
 category_id int,
 created_at timestamp, 
 updatesd_at bigint,
 completed_at timestamp


);


create  table ticketit_comments
(
 id int primary key,
 content text, 
 user_id int,
 ticket_id int,
 created_at timestamp, 
 updated_at timestamp,
 html text


);

create  table ticketit_settings
(
 id int primary key,
 lang varchar(30), 
 slug varchar(30),
 value int,
 default_value int,
 created_at timestamp, 
 updated_at timestamp
 


);


create  table ticketit_audits
(
 id int primary key,
 operation text, 
 user_id int,
 ticket_id int,
 created_at timestamp, 
 updated_at timestamp


);

create  table users
(
 id int primary key,
 ticketit_admin boolean,
 ticketit_agent boolean


);

create  table ticketit_categories_users
(
 category_id int primary key,
 user_id int


);


create  table ticketit_categories
(
 id int primary key,
 name varchar(30), 
 color bigint

);

create  table ticketit_statuses
(
 id int primary key,
 name varchar(30), 
 color bigint 


);

create  table ticketit_priorities
(
 id int primary key,
 name varchar(30), 
 color bigint 


);


ALTER TABLE ticketit 
ADD CONSTRAINT fk_status
FOREIGN KEY (status_id)
REFERENCES ticketit_statuses(id);


ALTER TABLE ticketit 
ADD CONSTRAINT fk_priorities
FOREIGN KEY (priority_id)
REFERENCES ticketit_priorities(id);

ALTER TABLE ticketit 
ADD CONSTRAINT fk_status
FOREIGN KEY (status_id)
REFERENCES ticketit_statuses(id);


ALTER TABLE ticketit 
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id)
REFERENCES users(id);

ALTER TABLE ticketit 
ADD CONSTRAINT fk_agent
FOREIGN KEY (agent_id)
REFERENCES users(id);

ALTER TABLE ticketit 
ADD CONSTRAINT fk_categories
FOREIGN KEY (category_id)
REFERENCES ticketit_categories(id);

ALTER TABLE ticketit_comments
ADD CONSTRAINT fk_users_comments
FOREIGN KEY (user_id)
REFERENCES users(id);

ALTER TABLE ticketit_comments
ADD CONSTRAINT fk_ticketit
FOREIGN KEY (ticket_id)
REFERENCES ticketit(id);

ALTER TABLE ticketit_audits
ADD CONSTRAINT fk_ticket
FOREIGN KEY (ticket_id)
REFERENCES ticketit(id);

ALTER TABLE ticketit_audits
ADD CONSTRAINT fk_users
FOREIGN KEY (user_id)
REFERENCES users(id);

ALTER TABLE ticketit_categories_users
ADD CONSTRAINT fk_users
FOREIGN KEY (user_id)
REFERENCES users(id);

ALTER TABLE ticketit_categories_users
ADD CONSTRAINT fk_categories
FOREIGN KEY (category_id)
REFERENCES ticketit_categories(id);















