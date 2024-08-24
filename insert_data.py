import sqlite3

conn = sqlite3.connect('medications.db')
c = conn.cursor()

medications = [
    ('Aspirin', 'C9H8O4', 'Pain relief, anti-inflammatory', '50-100 mg as needed', 'Avoid in case of bleeding disorders', 'Nausea, vomiting', 'Ibuprofen, Acetaminophen'),
    ('Paracetamol', 'C8H9NO2', 'Pain relief, fever reduction', '500 mg every 4-6 hours', 'Avoid in case of liver disease', 'Liver damage, allergic reactions', 'Aspirin, Ibuprofen'),
    ('Ibuprofen', 'C13H18O2', 'Pain relief, anti-inflammatory', '200-400 mg every 4-6 hours', 'Avoid in case of gastrointestinal problems', 'Stomach upset, headache', 'Aspirin, Naproxen'),
    ('Naproxen', 'C14H14O3', 'Pain relief, anti-inflammatory', '250-500 mg every 12 hours', 'Avoid in case of kidney disease', 'Stomach pain, heartburn', 'Ibuprofen, Aspirin'),
    ('Amoxicillin', 'C16H19N3O5S', 'Antibiotic for bacterial infections', '250-500 mg every 8 hours', 'Avoid in case of penicillin allergy', 'Rash, nausea', 'Penicillin, Cephalexin'),
    ('Cetirizine', 'C21H25ClN2O3', 'Allergy relief', '10 mg once daily', 'Avoid in case of kidney problems', 'Drowsiness, dry mouth', 'Loratadine, Fexofenadine'),
    ('Loratadine', 'C22H23ClN2', 'Allergy relief', '10 mg once daily', 'Avoid in case of liver disease', 'Headache, dry mouth', 'Cetirizine, Fexofenadine'),
    ('Fexofenadine', 'C32H39NO4', 'Allergy relief', '60 mg twice daily or 180 mg once daily', 'Avoid in case of kidney issues', 'Headache, drowsiness', 'Cetirizine, Loratadine'),
    ('Metformin', 'C4H11NO3', 'Diabetes management', '500-1000 mg twice daily', 'Avoid in case of kidney problems', 'Nausea, diarrhea', 'Insulin, Sulfonylureas'),
    ('Insulin', 'Protein hormone', 'Diabetes management', 'Dosage varies by individual', 'Avoid in case of hypoglycemia', 'Hypoglycemia, weight gain', 'Metformin, Sulfonylureas'),
    ('Sulfonylureas', 'Various', 'Diabetes management', 'Dosage varies by specific drug', 'Avoid in case of kidney or liver issues', 'Hypoglycemia, weight gain', 'Metformin, Insulin'),
    ('Simvastatin', 'C25H38O5', 'Cholesterol reduction', '10-40 mg once daily', 'Avoid in case of liver disease', 'Muscle pain, liver damage', 'Atorvastatin, Rosuvastatin'),
    ('Atorvastatin', 'C33H35FN2O5', 'Cholesterol reduction', '10-80 mg once daily', 'Avoid in case of liver disease', 'Muscle pain, digestive problems', 'Simvastatin, Rosuvastatin'),
    ('Rosuvastatin', 'C22H28FN3O6', 'Cholesterol reduction', '5-40 mg once daily', 'Avoid in case of liver problems', 'Headache, muscle pain', 'Atorvastatin, Simvastatin'),
    ('Omeprazole', 'C17H19N3O3S', 'Acid reflux, ulcers', '20-40 mg once daily', 'Avoid in case of liver disease', 'Headache, nausea', 'Lansoprazole, Esomeprazole'),
    ('Lansoprazole', 'C16H14F3N3O2S', 'Acid reflux, ulcers', '15-30 mg once daily', 'Avoid in case of liver disease', 'Diarrhea, headache', 'Omeprazole, Esomeprazole'),
    ('Esomeprazole', 'C17H19N3O3S', 'Acid reflux, ulcers', '20-40 mg once daily', 'Avoid in case of liver problems', 'Headache, nausea', 'Omeprazole, Lansoprazole'),
    ('Prednisone', 'C21H26O5', 'Inflammation, immune disorders', '5-60 mg daily depending on condition', 'Avoid in case of systemic fungal infections', 'Weight gain, mood swings', 'Hydrocortisone, Dexamethasone'),
    ('Hydrocortisone', 'C21H30O5', 'Inflammation, adrenal insufficiency', '20-240 mg daily depending on condition', 'Avoid in case of systemic fungal infections', 'Weight gain, mood swings', 'Prednisone, Dexamethasone'),
    ('Dexamethasone', 'C22H29FO5', 'Inflammation, immune disorders', '0.75-9 mg daily depending on condition', 'Avoid in case of systemic fungal infections', 'Weight gain, mood swings', 'Prednisone, Hydrocortisone'),
    ('Diazepam', 'C16H13ClN2O', 'Anxiety, seizures', '2-10 mg 2-4 times daily', 'Avoid in case of severe liver disease', 'Drowsiness, dizziness', 'Lorazepam, Clonazepam'),
    ('Lorazepam', 'C15H10Cl2N2O2', 'Anxiety, seizures', '2-6 mg daily in divided doses', 'Avoid in case of severe liver disease', 'Drowsiness, dizziness', 'Diazepam, Clonazepam'),
    ('Clonazepam', 'C15H10ClN3O3', 'Anxiety, seizures', '0.5-2 mg 2-3 times daily', 'Avoid in case of severe liver disease', 'Drowsiness, dizziness', 'Diazepam, Lorazepam'),
    ('Alprazolam', 'C17H13ClN4', 'Anxiety, panic disorders', '0.25-4 mg daily in divided doses', 'Avoid in case of severe liver disease', 'Drowsiness, dizziness', 'Diazepam, Lorazepam'),
    ('Buspirone', 'C21H31N5O3', 'Anxiety', '5-10 mg 2-3 times daily', 'Avoid in case of severe liver or kidney disease', 'Dizziness, nausea', 'Diazepam, Alprazolam'),
    ('Warfarin', 'C19H16O4', 'Blood thinning', '2-10 mg daily', 'Avoid in case of active bleeding', 'Bleeding, bruising', 'Heparin, Rivaroxaban'),
    ('Heparin', 'Various', 'Blood thinning', 'Dosage varies by condition', 'Avoid in case of active bleeding', 'Bleeding, bruising', 'Warfarin, Rivaroxaban'),
    ('Rivaroxaban', 'C19H18ClN5O5S', 'Blood thinning', '15-20 mg daily', 'Avoid in case of active bleeding', 'Bleeding, bruising', 'Warfarin, Heparin'),
    ('Digoxin', 'C41H64O14', 'Heart failure, arrhythmias', '0.125-0.5 mg daily', 'Avoid in case of severe kidney disease', 'Nausea, dizziness', 'Beta-blockers, ACE inhibitors'),
    ('Beta-blockers', 'Various', 'Heart conditions', 'Dosage varies by specific drug', 'Avoid in case of severe asthma', 'Fatigue, dizziness', 'Digoxin, ACE inhibitors'),
    ('ACE inhibitors', 'Various', 'Heart conditions', 'Dosage varies by specific drug', 'Avoid in case of severe kidney disease', 'Cough, dizziness', 'Beta-blockers, Digoxin'),
    ('Methotrexate', 'C20H22N8O5', 'Cancer, autoimmune diseases', '7.5-25 mg weekly', 'Avoid in case of liver disease', 'Nausea, liver damage', 'Azathioprine, Cyclosporine'),
    ('Azathioprine', 'C9H7N7O3S', 'Autoimmune diseases', '1-3 mg/kg daily', 'Avoid in case of severe liver disease', 'Nausea, liver damage', 'Methotrexate, Cyclosporine'),
    ('Cyclosporine', 'C62H111N11O12', 'Autoimmune diseases', '2.5-5 mg/kg daily', 'Avoid in case of severe liver disease', 'Gum hyperplasia, kidney damage', 'Methotrexate, Azathioprine'),
    ('Tetracycline', 'C22H24N2O8', 'Antibiotic for bacterial infections', '250-500 mg every 6-12 hours', 'Avoid in case of pregnancy', 'Nausea, sensitivity to sunlight', 'Doxycycline, Minocycline'),
    ('Doxycycline', 'C22H24N2O8', 'Antibiotic for bacterial infections', '100 mg twice daily', 'Avoid in case of pregnancy', 'Nausea, sensitivity to sunlight', 'Tetracycline, Minocycline'),
    ('Minocycline', 'C23H27N7O7', 'Antibiotic for bacterial infections', '100 mg twice daily', 'Avoid in case of pregnancy', 'Nausea, sensitivity to sunlight', 'Tetracycline, Doxycycline'),
    ('Ranitidine', 'C13H22N4O3', 'Acid reflux, ulcers', '150-300 mg twice daily', 'Avoid in case of kidney problems', 'Headache, dizziness', 'Omeprazole, Famotidine'),
    ('Famotidine', 'C8H15N7O2S3', 'Acid reflux, ulcers', '20-40 mg twice daily', 'Avoid in case of kidney problems', 'Headache, dizziness', 'Ranitidine, Cimetidine'),
    ('Cimetidine', 'C10H15N7S', 'Acid reflux, ulcers', '200-400 mg twice daily', 'Avoid in case of kidney problems', 'Headache, dizziness', 'Ranitidine, Famotidine'),
    ('Prednisolone', 'C21H28O5', 'Inflammation, immune disorders', '5-60 mg daily depending on condition', 'Avoid in case of systemic fungal infections', 'Weight gain, mood swings', 'Hydrocortisone, Dexamethasone'),
    ('Methylprednisolone', 'C22H30O5', 'Inflammation, immune disorders', '4-48 mg daily depending on condition', 'Avoid in case of systemic fungal infections', 'Weight gain, mood swings', 'Prednisone, Hydrocortisone'),
    ('Moxifloxacin', 'C21H24FN3O4', 'Antibiotic for bacterial infections', '400 mg once daily', 'Avoid in case of tendon problems', 'Nausea, dizziness', 'Levofloxacin, Ciprofloxacin'),
    ('Levofloxacin', 'C18H20FN3O4', 'Antibiotic for bacterial infections', '250-750 mg once daily', 'Avoid in case of tendon problems', 'Nausea, dizziness', 'Moxifloxacin, Ciprofloxacin'),
    ('Ciprofloxacin', 'C17H18FN3O3', 'Antibiotic for bacterial infections', '250-750 mg twice daily', 'Avoid in case of tendon problems', 'Nausea, dizziness', 'Moxifloxacin, Levofloxacin'),
    ('Fluoxetine', 'C17H18F3NO', 'Depression, anxiety', '20-80 mg daily', 'Avoid in case of bipolar disorder', 'Nausea, insomnia', 'Sertraline, Paroxetine'),
    ('Sertraline', 'C17H17Cl2N', 'Depression, anxiety', '50-200 mg daily', 'Avoid in case of bipolar disorder', 'Nausea, insomnia', 'Fluoxetine, Paroxetine'),
    ('Paroxetine', 'C19H20FNO3', 'Depression, anxiety', '20-50 mg daily', 'Avoid in case of bipolar disorder', 'Nausea, drowsiness', 'Fluoxetine, Sertraline'),
    ('Venlafaxine', 'C17H27NO2', 'Depression, anxiety', '75-375 mg daily', 'Avoid in case of uncontrolled hypertension', 'Nausea, dizziness', 'Duloxetine, Desvenlafaxine'),
    ('Duloxetine', 'C18H19NOS', 'Depression, anxiety', '30-120 mg daily', 'Avoid in case of uncontrolled hypertension', 'Nausea, drowsiness', 'Venlafaxine, Desvenlafaxine'),
    ('Desvenlafaxine', 'C16H25NOS', 'Depression, anxiety', '50-400 mg daily', 'Avoid in case of uncontrolled hypertension', 'Nausea, dizziness', 'Venlafaxine, Duloxetine'),
    ('Lithium', 'Li', 'Bipolar disorder', '300-1200 mg daily in divided doses', 'Avoid in case of severe kidney disease', 'Tremor, nausea', 'Valproate, Lamotrigine'),
    ('Valproate', 'C8H16O2', 'Bipolar disorder, epilepsy', '250-1500 mg daily in divided doses', 'Avoid in case of liver disease', 'Tremor, weight gain', 'Lithium, Lamotrigine'),
    ('Lamotrigine', 'C9H7Cl2N5', 'Epilepsy, bipolar disorder', '25-200 mg daily', 'Avoid in case of severe liver disease', 'Rash, dizziness', 'Lithium, Valproate'),
    ('Quetiapine', 'C21H25ClN6O2', 'Schizophrenia, bipolar disorder', '100-800 mg daily', 'Avoid in case of severe cardiovascular conditions', 'Drowsiness, weight gain', 'Olanzapine, Risperidone'),
    ('Olanzapine', 'C17H20N4S', 'Schizophrenia, bipolar disorder', '5-20 mg daily', 'Avoid in case of severe cardiovascular conditions', 'Weight gain, drowsiness', 'Quetiapine, Risperidone'),
    ('Risperidone', 'C23H27FN4O2', 'Schizophrenia, bipolar disorder', '1-8 mg daily', 'Avoid in case of severe cardiovascular conditions', 'Weight gain, drowsiness', 'Quetiapine, Olanzapine'),
    ('Aripiprazole', 'C23H27Cl2N3O2', 'Schizophrenia, bipolar disorder', '10-30 mg daily', 'Avoid in case of severe cardiovascular conditions', 'Nausea, dizziness', 'Quetiapine, Olanzapine'),
    ('Glyburide', 'C23H28ClN3O5S', 'Diabetes management', '1.25-20 mg daily', 'Avoid in case of severe kidney disease', 'Low blood sugar, weight gain', 'Metformin, Glipizide'),
    ('Glipizide', 'C21H27ClN2O4S', 'Diabetes management', '2.5-40 mg daily', 'Avoid in case of severe kidney disease', 'Low blood sugar, weight gain', 'Metformin, Glyburide'),
    ('Sitagliptin', 'C17H15F6N5O2', 'Diabetes management', '100 mg once daily', 'Avoid in case of severe kidney disease', 'Nausea, headache', 'Metformin, Saxagliptin'),
    ('Saxagliptin', 'C18H25N5O2', 'Diabetes management', '2.5-5 mg daily', 'Avoid in case of severe kidney disease', 'Headache, upper respiratory tract infection', 'Metformin, Sitagliptin'),
    ('Linagliptin', 'C25H28N8O2', 'Diabetes management', '5 mg once daily', 'Avoid in case of severe kidney disease', 'Headache, diarrhea', 'Metformin, Sitagliptin'),
    ('Pioglitazone', 'C19H20N2O3S', 'Diabetes management', '15-45 mg daily', 'Avoid in case of severe liver disease', 'Weight gain, edema', 'Metformin, Rosiglitazone'),
    ('Rosiglitazone', 'C18H22N4O3S', 'Diabetes management', '4-8 mg daily', 'Avoid in case of severe liver disease', 'Weight gain, edema', 'Metformin, Pioglitazone'),
    ('Acarbose', 'C25H43NO18', 'Diabetes management', '25-100 mg with meals', 'Avoid in case of severe kidney disease', 'Flatulence, diarrhea', 'Metformin, Miglitol'),
    ('Miglitol', 'C8H17NO5', 'Diabetes management', '25-100 mg with meals', 'Avoid in case of severe kidney disease', 'Flatulence, diarrhea', 'Metformin, Acarbose'),
    ('Ezetimibe', 'C24H21F2NO3', 'Cholesterol reduction', '10 mg daily', 'Avoid in case of liver disease', 'Abdominal pain, diarrhea', 'Statins, Bile acid sequestrants'),
    ('Bile acid sequestrants', 'Various', 'Cholesterol reduction', 'Dosage varies by specific drug', 'Avoid in case of gastrointestinal disorders', 'Constipation, bloating', 'Ezetimibe, Statins'),
    ('Statins', 'Various', 'Cholesterol reduction', 'Dosage varies by specific drug', 'Avoid in case of liver disease', 'Muscle pain, liver damage', 'Ezetimibe, Bile acid sequestrants'),
    ('Fluticasone', 'C22H27F3O4S', 'Allergic rhinitis, asthma', '50-250 mcg twice daily', 'Avoid in case of active infections', 'Nasal irritation, headache', 'Budesonide, Mometasone'),
    ('Budesonide', 'C25H34O6', 'Allergic rhinitis, asthma', '200-400 mcg twice daily', 'Avoid in case of active infections', 'Nasal irritation, headache', 'Fluticasone, Mometasone'),
    ('Mometasone', 'C22H28Cl2O4', 'Allergic rhinitis, asthma', '200-400 mcg twice daily', 'Avoid in case of active infections', 'Nasal irritation, headache', 'Fluticasone, Budesonide'),
    ('Montelukast', 'C35H36ClNO3S', 'Allergic rhinitis, asthma', '10 mg once daily', 'Avoid in case of liver disease', 'Headache, abdominal pain', 'Loratadine, Cetirizine'),
    ('Theophylline', 'C7H8N4O2', 'Asthma', '200-600 mg daily in divided doses', 'Avoid in case of severe liver disease', 'Nausea, insomnia', 'Montelukast, Beta-agonists'),
    ('Beta-agonists', 'Various', 'Asthma', 'Dosage varies by specific drug', 'Avoid in case of severe cardiovascular conditions', 'Tremor, palpitations', 'Theophylline, Montelukast'),
    ('Niacin', 'C6H5NO2', 'Cholesterol reduction', '500-2000 mg daily', 'Avoid in case of liver disease', 'Flushing, itching', 'Statins, Ezetimibe'),
    ('Omega-3 fatty acids', 'Various', 'Cholesterol reduction', '1-4 g daily', 'Avoid in case of bleeding disorders', 'Nausea, diarrhea', 'Statins, Niacin'),
    ('Sodium chloride', 'NaCl', 'Electrolyte replacement', 'Dosage varies by condition', 'Avoid in case of severe kidney disease', 'Edema, hypertension', 'Potassium chloride, Calcium carbonate'),
    ('Potassium chloride', 'KCl', 'Electrolyte replacement', '10-20 mEq daily', 'Avoid in case of severe kidney disease', 'Hyperkalemia, gastrointestinal irritation', 'Sodium chloride, Calcium carbonate'),
    ('Calcium carbonate', 'CaCO3', 'Calcium supplementation', '500-1000 mg daily', 'Avoid in case of severe kidney disease', 'Constipation, nausea', 'Sodium chloride, Potassium chloride'),
    ('Vitamin D', 'Various', 'Bone health, calcium absorption', '600-800 IU daily', 'Avoid in case of hypercalcemia', 'Nausea, constipation', 'Calcium carbonate, Vitamin K'),
    ('Vitamin K', 'Various', 'Blood clotting', '90-120 mcg daily', 'Avoid in case of anticoagulant therapy', 'Allergic reactions, stomach upset', 'Vitamin D, Calcium'),
    ('Folic acid', 'C19H19N7O6', 'Prevention of neural tube defects', '400-800 mcg daily', 'Avoid in case of vitamin B12 deficiency', 'Nausea, abdominal cramps', 'Vitamin B12, Iron'),
    ('Iron', 'Fe', 'Anemia', '18 mg daily', 'Avoid in case of hemochromatosis', 'Constipation, dark stools', 'Folic acid, Vitamin B12'),
    ('Iodine', 'I', 'Thyroid health', '150 mcg daily', 'Avoid in case of thyroid disorders', 'Skin rash, gastrointestinal upset', 'Thyroxine, Potassium iodide'),
    ('Thyroxine', 'C15H11I4NO4', 'Thyroid hormone replacement', '25-300 mcg daily', 'Avoid in case of untreated hyperthyroidism', 'Palpitations, weight loss', 'Iodine, Liothyronine'),
    ('Liothyronine', 'C15H11I3NO4', 'Thyroid hormone replacement', '5-25 mcg daily', 'Avoid in case of untreated hyperthyroidism', 'Palpitations, weight loss', 'Thyroxine, Iodine'),
    ('Levothyroxine', 'C15H11I4NO4', 'Thyroid hormone replacement', '25-300 mcg daily', 'Avoid in case of untreated hyperthyroidism', 'Palpitations, weight loss', 'Thyroxine, Liothyronine'),
    ('Phenobarbital', 'C12H12N2O3', 'Seizures, sedation', '60-200 mg daily in divided doses', 'Avoid in case of liver disease', 'Drowsiness, dizziness', 'Primidone, Benzodiazepines'),
    ('Primidone', 'C12H14N2O3', 'Seizures', '250-750 mg daily in divided doses', 'Avoid in case of liver disease', 'Drowsiness, dizziness', 'Phenobarbital, Benzodiazepines'),
    ('Benzodiazepines', 'Various', 'Seizures, anxiety', 'Dosage varies by specific drug', 'Avoid in case of severe liver disease', 'Drowsiness, dizziness', 'Phenobarbital, Primidone'),
    ('Acetaminophen', 'C8H9NO2', 'Pain relief, fever reduction', '500-1000 mg every 4-6 hours', 'Avoid in case of liver disease', 'Liver damage, allergic reactions', 'Ibuprofen, Aspirin'),
    ('Codeine', 'C18H21NO3', 'Pain relief, cough suppressant', '15-60 mg every 4-6 hours', 'Avoid in case of respiratory disorders', 'Constipation, drowsiness', 'Hydrocodone, Oxycodone'),
    ('Hydrocodone', 'C18H21NO3', 'Pain relief, cough suppressant', '10-60 mg every 4-6 hours', 'Avoid in case of respiratory disorders', 'Constipation, drowsiness', 'Codeine, Oxycodone'),
    ('Oxycodone', 'C18H21NO4', 'Pain relief', '5-20 mg every 4-6 hours', 'Avoid in case of respiratory disorders', 'Constipation, drowsiness', 'Codeine, Hydrocodone'),
    ('Tramadol', 'C16H25NO2', 'Pain relief', '50-100 mg every 4-6 hours', 'Avoid in case of severe liver or kidney disease', 'Nausea, dizziness', 'Oxycodone, Hydrocodone'),
    ('Methadone', 'C21H27NO', 'Pain relief, opioid dependence', '2.5-10 mg every 8-12 hours', 'Avoid in case of severe respiratory disorders', 'Drowsiness, constipation', 'Oxycodone, Morphine'),
    ('Morphine', 'C17H19NO3', 'Pain relief', '10-30 mg every 4 hours', 'Avoid in case of severe respiratory disorders', 'Constipation, drowsiness', 'Oxycodone, Methadone'),
    ('Buprenorphine', 'C29H41NO4', 'Pain relief, opioid dependence', '0.2-0.8 mg every 6-8 hours', 'Avoid in case of severe respiratory disorders', 'Constipation, nausea', 'Methadone, Morphine'),
    ('Naloxone', 'C19H21NO5', 'Opioid overdose reversal', '0.4-2 mg every 2-3 minutes as needed', 'Avoid in case of non-opioid overdose', 'Withdrawal symptoms', 'Naltrexone, Methadone'),
    ('Naltrexone', 'C20H23NO4', 'Opioid dependence', '50 mg daily', 'Avoid in case of opioid use', 'Nausea, headache', 'Naloxone, Methadone'),
    ('Bupropion', 'C13H18ClNO', 'Depression, smoking cessation', '100-400 mg daily in divided doses', 'Avoid in case of seizure disorders', 'Insomnia, dry mouth', 'Sertraline, Nefazodone'),
    ('Nefazodone', 'C20H22Cl2N4O3', 'Depression', '200-600 mg daily in divided doses', 'Avoid in case of liver disease', 'Drowsiness, dry mouth', 'Sertraline, Bupropion'),
    ('Trazodone', 'C19H22ClN5O', 'Depression, insomnia', '150-600 mg daily in divided doses', 'Avoid in case of recent heart attack', 'Drowsiness, dry mouth', 'Sertraline, Nefazodone'),
    ('Buspirone', 'C21H31N5O3', 'Anxiety', '5-10 mg 2-3 times daily', 'Avoid in case of severe liver or kidney disease', 'Dizziness, nausea', 'Diazepam, Alprazolam'),
    ('Clonidine', 'C9H9Cl2N3', 'Hypertension', '0.1-0.3 mg twice daily', 'Avoid in case of severe bradycardia', 'Drowsiness, dry mouth', 'Labetalol, Methyldopa'),
    ('Methyldopa', 'C10H13NO4', 'Hypertension', '250-1000 mg daily in divided doses', 'Avoid in case of liver disease', 'Drowsiness, dry mouth', 'Clonidine, Labetalol'),
    ('Labetalol', 'C19H24N2O3', 'Hypertension', '100-1200 mg daily in divided doses', 'Avoid in case of severe asthma', 'Dizziness, fatigue', 'Clonidine, Methyldopa'),
    ('Dantrolene', 'C14H9NaO5', 'Muscle spasticity', '25-100 mg 2-4 times daily', 'Avoid in case of liver disease', 'Drowsiness, muscle weakness', 'Baclofen, Tizanidine'),
    ('Baclofen', 'C10H12ClNO2', 'Muscle spasticity', '5-20 mg 3-4 times daily', 'Avoid in case of severe renal impairment', 'Drowsiness, dizziness', 'Dantrolene, Tizanidine'),
    ('Tizanidine', 'C9H8ClN5', 'Muscle spasticity', '2-4 mg 3 times daily', 'Avoid in case of severe liver disease', 'Drowsiness, dizziness', 'Dantrolene, Baclofen')

]

c.executemany('''
    INSERT INTO medications (name, formula, uses, dosage, warnings, effects, alternatives) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', medications)

conn.commit()
conn.close()
