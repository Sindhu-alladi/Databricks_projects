-- view creations 

-- patients view
create or replace view vw_patients as
select 
patient_id,
mrn,
full_name,
date_of_birth,
gender,
city,
blood_type,
phone from patients;

select * from vw_patients;

-- doctore view
create or replace view vw_doctors as 
select 
doctor_id,
employee_code,
full_name,
specialty,
department,
experience_years,
is_active from doctors;

desc vw_doctors;
select * from vw_doctors;

-- visits view
create or replace view vw_visits as 
select
visit_id,
patient_id,
doctor_id,
visit_date,
department,
chief_complaint,
discharge_date from visits;

-- treatments view
create or replace view vw_treatments as 
select
treatment_id,
visit_id,
treatment_name,
cost,
administered_by,
treatment_date from treatments;

select * from vw_treatments;

-- claims
create or replace view vw_claims as 
select 
claim_id,
patient_id,
visit_id,
claim_amount,
insurer_name,
policy_number,
status,
claim_date,
settled_date from claims;


select * from vw_treatments;






