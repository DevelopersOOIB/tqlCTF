CREATE DATABASE hrboard;

USE hrboard;

CREATE TABLE workers (
    id INT, name VARCHAR(60), 
    aboutme VARCHAR(550), 
    avatar VARCHAR(10), 
    salary INT
);


INSERT INTO workers (id, name, aboutme, avatar, salary) VALUES (
    1, 
    'Alice Johnson', 
    'Job Description: Software Engineer - Responsible for building and maintaining software applications, collaborating with cross-functional teams, and ensuring high-quality code.', 
    '1.png', 
    350
);


INSERT INTO workers (id, name, aboutme, avatar, salary) VALUES (
    2, 
    'Michael Smith', 
    'Job Description: Data Analyst - Analyze complex datasets to help drive business decisions and improve processes, using statistical tools and methods.', 
    '2.png', 
    300
);


INSERT INTO workers (id, name, aboutme, avatar, salary) VALUES (
    3, 
    'Emily Davis', 
    'Job Description: UX/UI Designer - Create user-friendly interfaces for websites and applications, focusing on enhancing user experience and accessibility.', 
    '3.png', 
    8989
);


INSERT INTO workers (id, name, aboutme, avatar, salary) VALUES (
    4, 
    'David Brown', 
    'Job Description: DevOps Engineer - Collaborate with development and operations teams to implement CI/CD pipelines, automate processes, and improve system reliability.', 
    '4.png', 
    787
);


INSERT INTO workers (id, name, aboutme, avatar, salary) VALUES (
    5, 
    'Sophie Wilson', 
    'Job Description: Front-End Developer - Build responsive and interactive web applications using HTML, CSS, and JavaScript frameworks.', 
    '5.png', 
    111
);


INSERT INTO workers (id, name, aboutme, avatar, salary) VALUES (
    6, 
    'James Taylor', 
    'Job Description: Back-End Developer - Develop server-side logic and APIs, manage database interactions, and ensure application performance and scalability.', 
    '6.png', 
    453
);


INSERT INTO workers (id, name, aboutme, avatar, salary) VALUES (
    7, 
    'Isabella Martinez', 
    'Job Description: Project Manager - Oversee IT projects from inception to completion, ensuring timelines, budgets, and quality standards are met.', 
    '7.png', 
    556
);


INSERT INTO workers (id, name, aboutme, avatar, salary) VALUES (
    8, 
    'Jacob Anderson', 
    'Job Description: Quality Assurance Tester - Design test plans and conduct manual and automated testing to ensure software reliability and performance.', 
    '8.png', 
    334
);


INSERT INTO workers (id, name, aboutme, avatar, salary) VALUES (
    9, 
    'Olivia Thomas', 
    'Job Description: Cybersecurity Analyst - Monitor systems for security breaches, respond to incidents, and implement security measures to protect sensitive information.', 
    '9.png', 
    480
);


INSERT INTO workers (id, name, aboutme, avatar, salary) VALUES (
    10, 
    'Daniel White', 
    'Job Description: Cloud Solutions Architect - Design and implement cloud infrastructure and services, ensuring optimal performance and security for cloud-based applications.', 
    '10.png', 
    960
);