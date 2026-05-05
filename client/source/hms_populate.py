import csv
import os
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker('en_IN')
random.seed(42)
Faker.seed(42)

output_folder = "C:\\DataEngineer_project\\client\\hms_csv_output"
os.makedirs(output_folder, exist_ok=True)

specialties = [
    "Cardiology", "Oncology", "Neurology", "Orthopedics",
    "Pediatrics", "Dermatology", "Gastroenterology",
    "Pulmonology", "Endocrinology", "Nephrology","Other"
]

departments = ["ICU", "OPD", "Emergency", "Surgery", "Radiology", "Pathology","Other"]

blood_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

genders = ["M", "F", "Other"]

insurers = [
    "Star Health Insurance", "HDFC ERGO Health",
    "Bajaj Allianz Health", "New India Assurance",
    "United India Insurance", "ICICI Lombard Health",
    "Niva Bupa Health", "Aditya Birla Health",
    "Care Health Insurance", "Tata AIG Health","Other"
]

claim_statuses = ["Submitted", "Approved", "Rejected", "Pending", "Under Review"]

treatments_list = [
    "Blood Test", "MRI Scan", "CT Scan", "ECG",
    "X-Ray", "Ultrasound", "Chemotherapy", "Dialysis",
    "Physiotherapy", "Endoscopy", "Biopsy", "Colonoscopy",
    "Echocardiogram", "Spirometry", "Allergy Test",
    "Insulin Therapy", "Blood Transfusion", "Wound Dressing",
    "IV Drip", "Oxygen Therapy","Other"
]

complaints = [
    "Chest pain", "Shortness of breath", "Severe headache",
    "Abdominal pain", "Fever and chills", "Joint pain",
    "Back pain", "Dizziness", "Nausea and vomiting",
    "Skin rash", "Persistent cough", "Fatigue",
    "Swollen legs", "High blood sugar", "Blurred vision","Other"
]


def write_csv(filename, headers, rows):
    filepath = os.path.join(output_folder, filename)
    f = open(filepath, "w", newline="", encoding="utf-8")
    writer = csv.writer(f)
    writer.writerow(headers)
    for row in rows:
        writer.writerow(row)
    f.close()
    print("saved", filename, "with", len(rows), "rows")


# imperfection 1 - some patient names have extra spaces
def add_name_whitespace(name):
    i = random.random()
    if i < 0.025:
        return " " + name
    elif i < 0.05:
        return name + " "
    return name


# imperfection 3 - some doctor names have messed up capitalisation
def mess_doctor_name(name):
    if random.random() >= 0.06:
        return name
    words = name.split()
    new_words = []
    for word in words:
        r = random.random()
        if r < 0.33:
            new_words.append(word.upper())
        elif r < 0.66:
            new_words.append(word.lower())
        else:
            new_words.append(word)
    result = " ".join(new_words)
    if random.random() < 0.4:
        result = "dr. " + result
    return result


# imperfection 4 - some treatment names have spacing or casing issues
def mess_treatment_name(name):
    j = random.random()
    if j < 0.02:
        return " " + name
    elif j < 0.04:
        return name + " "
    elif j < 0.05:
        return name.upper()
    elif j < 0.06:
        return name.lower()
    return name


# imperfection 5 - some insurer names have spacing or casing issues
def mess_insurer_name(name):
    i = random.random()
    if i < 0.015:
        return " " + name
    elif i < 0.025:
        return name + " "
    elif i < 0.035:
        return name.upper()
    elif i < 0.04:
        return name.lower()
    return name


# --- generate patients ---
print("generating patients...")
patient_rows = []

for i in range(1, 501):
    patient_id = i
    mrn = "MRN-" + str(i).zfill(5)
    name = add_name_whitespace(fake.name())
    dob = fake.date_of_birth(minimum_age=1, maximum_age=90)
    gender = random.choice(genders)
    city = fake.city()

    if random.random() > 0.10:
        blood = random.choice(blood_types)
    else:
        blood = ""

    if random.random() > 0.15:
        phone = fake.phone_number()[:20]
    else:
        phone = ""

    created = datetime.now()
    updated = created

    patient_rows.append([patient_id, mrn, name, dob, gender, city, blood, phone, created, updated])

# imperfection 2 - duplicate MRNs from a bad data migration
targets = random.sample(range(250, 500), 15)
sources = random.sample(range(0, 250), 15)
for t, s in zip(targets, sources):
    patient_rows[t][1] = patient_rows[s][1]

write_csv("patients.csv",
          ["patient_id", "mrn", "full_name", "date_of_birth", "gender",
           "city", "blood_type", "phone", "created_at", "updated_at"],
          patient_rows)

patient_ids = [row[0] for row in patient_rows]


# --- generate doctors ---
print("generating doctors...")
doctor_rows = []

for i in range(1, 51):
    doctor_id = i
    emp_code = "EMP-" + str(i).zfill(3)
    name = mess_doctor_name(fake.name())
    specialty = random.choice(specialties)
    dept = random.choice(departments)
    exp = random.randint(1, 40)
    created = datetime.now()

    doctor_rows.append([doctor_id, emp_code, name, specialty, dept, exp, 1, created])

write_csv("doctors.csv",
          ["doctor_id", "employee_code", "full_name", "specialty",
           "department", "experience_years", "is_active", "created_at"],
          doctor_rows)

doctor_ids = [row[0] for row in doctor_rows]


# --- generate visits ---
print("generating visits...")
visit_rows = []

for i in range(1, 2001):
    visit_id = i
    patient_id = random.choice(patient_ids)
    doctor_id = random.choice(doctor_ids)
    visit_date = fake.date_between(start_date="-2y", end_date="today")
    dept = random.choice(departments)

    if random.random() > 0.05:
        complaint = random.choice(complaints)
    else:
        complaint = ""

    if random.random() < 0.15:
        discharge = visit_date + timedelta(days=random.randint(1, 14))
        if discharge > datetime.now().date():
            discharge = datetime.now().date()
    else:
        discharge = ""

    created = datetime.combine(visit_date, datetime.min.time()) + timedelta(hours=random.randint(6, 22))

    visit_rows.append([visit_id, patient_id, doctor_id, visit_date, dept, complaint, discharge, created])

write_csv("visits.csv",
          ["visit_id", "patient_id", "doctor_id", "visit_date",
           "department", "chief_complaint", "discharge_date", "created_at"],
          visit_rows)

visit_ids = [row[0] for row in visit_rows]


# --- generate treatments ---
print("generating treatments...")
treatment_rows = []
visit_picks = random.choices(visit_ids, k=3000)

for i in range(len(visit_picks)):
    treatment_id = i + 1
    visit_id = visit_picks[i]
    treatment = mess_treatment_name(random.choice(treatments_list))
    cost = round(random.uniform(200, 50000), 2)

    if random.random() > 0.2:
        done_by = fake.name()
    else:
        done_by = ""

    t_date = fake.date_between(start_date="-2y", end_date="today")
    created = datetime.combine(t_date, datetime.min.time()) + timedelta(hours=random.randint(6, 22))

    treatment_rows.append([treatment_id, visit_id, treatment, cost, done_by, t_date, created])

write_csv("treatments.csv",
          ["treatment_id", "visit_id", "treatment_name", "cost",
           "administered_by", "treatment_date", "created_at"],
          treatment_rows)


# --- generate claims ---
print("generating claims...")
claim_rows = []

for i in range(1, 981):
    claim_id = i
    patient_id = random.choice(patient_ids)

    if random.random() < 0.85:
        visit_id = random.choice(visit_ids)
    else:
        visit_id = ""

    amount = round(random.uniform(500, 200000), 2)
    insurer = mess_insurer_name(random.choice(insurers))

    if random.random() > 0.1:
        policy = "POL-" + fake.bothify("??####??").upper()
    else:
        policy = ""

    status = random.choice(claim_statuses)
    claim_date = fake.date_between(start_date="-2y", end_date="today")

    if status in ("Approved", "Rejected") and random.random() < 0.30:
        settled = claim_date + timedelta(days=random.randint(3, 90))
        if settled > datetime.now().date():
            settled = datetime.now().date()
    else:
        settled = ""

    created = datetime.combine(claim_date, datetime.min.time()) + timedelta(hours=random.randint(6, 22))

    claim_rows.append([claim_id, patient_id, visit_id, amount, insurer, policy, status, claim_date, settled, created])

# imperfection 6 - 20 duplicate rows from the insurance portal retry bug
duplicates = random.sample(claim_rows, 20)
next_id = 981
for dup in duplicates:
    new_row = list(dup)
    new_row[0] = next_id
    claim_rows.append(new_row)
    next_id += 1

random.shuffle(claim_rows)
for k in range(len(claim_rows)):
    claim_rows[k][0] = k + 1

write_csv("claims.csv",
          ["claim_id", "patient_id", "visit_id", "claim_amount",
           "insurer_name", "policy_number", "status",
           "claim_date", "settled_date", "created_at"],
          claim_rows)

print("\ndone! check the", output_folder, "folder")