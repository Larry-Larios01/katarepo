INSERT INTO users (id, ticketit_admin, ticketit_agent) VALUES
(1, TRUE, TRUE),
(2, TRUE, FALSE),
(3, FALSE, TRUE),
(4, FALSE, TRUE),
(5, FALSE, FALSE),
(6, FALSE, TRUE),
(7, TRUE, FALSE),
(8, FALSE, FALSE),
(9, FALSE, TRUE),
(10, TRUE, FALSE),
(11, FALSE, TRUE),
(12, FALSE, TRUE),
(13, TRUE, TRUE),
(14, TRUE, FALSE),
(15, FALSE, FALSE),
(16, TRUE, TRUE),
(17, FALSE, TRUE),
(18, FALSE, FALSE),
(19, TRUE, TRUE),
(20, TRUE, FALSE);





INSERT INTO ticketit_statuses (id, name, color) VALUES
(1, 'Open', 16711680),
(2, 'Pending', 65280),
(3, 'Resolved', 255),
(4, 'Closed', 8421504),
(5, 'Escalated', 16753920),
(6, 'On Hold', 12632256),
(7, 'Awaiting Info', 65535),
(8, 'In Progress', 16776960),
(9, 'Reviewing', 8388736),
(10, 'Cancelled', 32896);


INSERT INTO ticketit_priorities (id, name, color) VALUES
(1, 'Low', 65280),
(2, 'Medium', 16776960),
(3, 'High', 16711680),
(4, 'Critical', 8421504),
(5, 'Urgent', 12632256);

INSERT INTO ticketit_categories (id, name, color) VALUES
(1, 'Technical', 255),
(2, 'Billing', 16711680),
(3, 'Support', 65280),
(4, 'HR', 8421504),
(5, 'IT', 16753920);

INSERT INTO ticketit (id, subject, content, html, status_id, priority_id, user_id, agent_id, category_id, created_at, updatesd_at, completed_at) VALUES
(1, 'Login Issue', 'Cannot login', '<p>Cannot login</p>', 1, 3, 2, 1, 1, NOW(), 1001, NULL),
(2, 'Payment Failure', 'Payment not processed', '<p>Payment not processed</p>', 2, 2, 3, 2, 2, NOW(), 1002, NULL),
(3, 'System Error', 'Error on the dashboard', '<p>Error on the dashboard</p>', 3, 1, 4, 3, 1, NOW(), 1003, NOW()),
(4, 'Update Request', 'Request for data update', '<p>Request for data update</p>', 4, 2, 5, 1, 4, NOW(), 1004, NULL),
(5, 'Password Reset', 'Forgot password', '<p>Forgot password</p>', 5, 1, 6, 2, 3, NOW(), 1005, NULL),
(6, 'VPN Issue', 'Cannot connect to VPN', '<p>Cannot connect to VPN</p>', 6, 4, 7, 4, 1, NOW(), 1006, NULL),
(7, 'App Crash', 'Mobile app crashes', '<p>Mobile app crashes</p>', 7, 3, 8, 5, 5, NOW(), 1007, NOW()),
(8, 'Account Locked', 'Account is locked', '<p>Account is locked</p>', 8, 2, 9, 3, 3, NOW(), 1008, NULL),
(9, 'Feedback', 'Feedback on service', '<p>Feedback on service</p>', 9, 1, 10, 2, 4, NOW(), 1009, NULL),
(10, 'Bug Report', 'Found a bug', '<p>Found a bug</p>', 1, 3, 11, 4, 2, NOW(), 1010, NULL),
(11, 'Network Issue', 'Network is slow', '<p>Network is slow</p>', 2, 4, 12, 5, 1, NOW(), 1011, NULL),
(12, 'Request Access', 'Need access to server', '<p>Need access to server</p>', 3, 2, 13, 1, 5, NOW(), 1012, NULL),
(13, 'Query', 'General query', '<p>General query</p>', 4, 1, 14, 2, 3, NOW(), 1013, NULL),
(14, 'New Feature', 'Request a new feature', '<p>Request a new feature</p>', 5, 1, 15, 3, 4, NOW(), 1014, NOW()),
(15, 'Refund Request', 'Need a refund', '<p>Need a refund</p>', 6, 3, 16, 1, 2, NOW(), 1015, NULL),
(16, 'Training Request', 'Request training', '<p>Request training</p>', 7, 2, 17, 5, 4, NOW(), 1016, NULL),
(17, 'Email Issue', 'Cannot send emails', '<p>Cannot send emails</p>', 8, 3, 18, 3, 1, NOW(), 1017, NULL),
(18, 'Data Loss', 'Data missing', '<p>Data missing</p>', 9, 4, 19, 4, 1, NOW(), 1018, NULL),
(19, 'Upgrade Request', 'Upgrade software', '<p>Upgrade software</p>', 1, 3, 20, 1, 5, NOW(), 1019, NULL),
(20, 'Service Request', 'Need support', '<p>Need support</p>', 2, 1, 1, 2, 3, NOW(), 1020, NULL);


INSERT INTO ticketit_comments (id, content, user_id, ticket_id, created_at, updated_at, html) VALUES
(1, 'We are working on your issue.', 1, 1, NOW(), NOW(), '<p>We are working on your issue.</p>'),
(2, 'Can you provide more details?', 2, 2, NOW(), NOW(), '<p>Can you provide more details?</p>'),
(3, 'Issue has been resolved.', 3, 3, NOW(), NOW(), '<p>Issue has been resolved.</p>'),
(4, 'Waiting for customer response.', 4, 4, NOW(), NOW(), '<p>Waiting for customer response.</p>');
-- Inserta otros 16 comentarios relacionados con tickets.





INSERT INTO ticketit_audits (id, operation, user_id, ticket_id, created_at, updated_at) VALUES
(1, 'Ticket Created', 1, 1, NOW(), NOW()),
(2, 'Ticket Updated', 2, 2, NOW(), NOW()),
(3, 'Status Changed to Resolved', 3, 3, NOW(), NOW()),
(4, 'Priority Updated', 4, 4, NOW(), NOW());
-- Inserta 16 más relacionados con auditorías de tickets.


INSERT INTO ticketit_settings (id, lang, slug, value, default_value, created_at, updated_at) VALUES
(1, 'en', 'default_priority', 1, 1, NOW(), NOW()),
(2, 'es', 'ticket_auto_assign', 0, 1, NOW(), NOW()),
(3, 'en', 'notification_enabled', 1, 1, NOW(), NOW()),
(4, 'fr', 'default_category', 2, 2, NOW(), NOW());
-- Inserta 16 más relacionados con configuraciones del sistema.


INSERT INTO ticketit_categories_users (category_id, user_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);
-- Inserta 15 más asociando categorías y usuarios.


