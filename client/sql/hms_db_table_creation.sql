-- create database hms_db;
use hms_db;

-- Patients table 
create table patients(
patient_id int not null,
mrn varchar(20),
full_name varchar(100),
date_of_birth date,
gender varchar(10),
city varchar(100),
blood_type varchar(5),
phone varchar(30),
created_at datetime,
updated_at datetime,
primary key(patient_id));

-- Doctors table
create table doctors (
doctor_id int not null,
employee_code varchar(20),
full_name varchar(255),
speciality varchar(100),
department varchar(100),
experience_years int,
is_active tinyint(1),
created_at datetime,
primary key(doctor_id));

-- visits
create table visits (
visit_id int not null,
patient_id int,
doctor_id int,
visit_date date,
department varchar(100),
cheif_complaint varchar(200),
discharge_date date,
created_at datetime,
primary key(visit_id),
foreign key (patient_id) references patients(patient_id),
foreign key (doctor_id) references doctors(doctor_id));

-- treatments
create table treatments (
treatment_id int,
visit_id int,
treatment_name varchar(100),
cost decimal(10,2),
administrated_by varchar(255),
treatment_date date,
created_at datetime,
primary key(treatment_id),
foreign key(visit_id) references visits(visit_id));

-- claims
create table claims (
claim_id int,
patient_id int,
visit_id int,
claim_amount decimal(12,2),
insurer_name varchar(120),
policy_number varchar(30),
status varchar(20),
claim_date date,
settled_date date,
created_at datetime,
primary key (claim_id),
foreign key(patient_id) references patients(patient_id),
foreign key(visit_id) references visits(visit_id));
