from django.db import models

# History Model
class History(models.Model):
    client_name = models.CharField(max_length=20)
    health_pro_name = models.CharField(max_length=20)
    chief_complaint = models.CharField(max_length=255, default="empty")
    gravida = models.CharField(max_length=20, default="empty")
    para = models.CharField(max_length=20, default="empty")
    abortion = models.CharField(max_length=20, default="empty")
    stillbirth = models.CharField(max_length=20, default="empty")
    early_neonatal_death = models.CharField(max_length=20, default="empty")
    present_history = models.TextField(default="empty")
    past_obs_history = models.TextField(default="empty")
    menstrual_history = models.TextField(default="empty")
    sexual_history = models.TextField(default="empty")
    family_planning = models.TextField(default="empty")
    gynecological_history = models.TextField(default="empty")
    medical_history = models.TextField(default="empty")
    family_history = models.TextField(default="empty")
    medication_history = models.TextField(default="empty")
    surgical_history = models.TextField(default="empty")
    nutritional_history = models.TextField(default="empty")
    diagnosis = models.CharField(max_length=255, default="empty")
    created_at = models.DateTimeField(auto_now_add=True)
    general_appearance = models.TextField(default="empty")
    skin = models.TextField(default="empty")
    head = models.TextField(default="empty")
    eye = models.TextField(default="empty")
    ear = models.TextField(default="empty")
    nose = models.TextField(default="empty")
    throat = models.TextField(default="empty")
    cardiovascular = models.TextField(default="empty")
    respiratory = models.TextField(default="empty")
    gastrointestinal = models.TextField(default="empty")
    genitourinary = models.TextField(default="empty")
    musculoskeletal = models.TextField(default="empty")
    neurological = models.TextField(default="empty")
    psychiatric = models.TextField(default="empty")
    endocrine = models.TextField(default="empty")
    immune = models.TextField(default="empty")
    breast = models.TextField(default="empty")
    blood_pressure = models.CharField(max_length=10, default="empty")
    respiratory_rate = models.CharField(max_length=10, default="empty")
    temperature = models.CharField(max_length=10, default="empty")
    pulse_rate = models.CharField(max_length=10, default="empty")
    spo2 = models.CharField(max_length=10, default="empty")
    weight = models.CharField(max_length=10, default="empty")

# Free History Model
class FreeHistory(models.Model):
    client_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    history = models.TextField()
    health_pro_name = models.CharField(max_length=20)

# Chart Model
class Chart(models.Model):
    client_name = models.CharField(max_length=20)
    health_pro_name = models.CharField(max_length=20)
    purpose = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    blood_pressure = models.CharField(max_length=10, default="empty")
    respiratory_rate = models.CharField(max_length=10, default="empty")
    temperature = models.CharField(max_length=10, default="empty")
    pulse_rate = models.CharField(max_length=10, default="empty")
    spo2 = models.CharField(max_length=10, default="empty")
    fetal_heart_rate = models.CharField(max_length=10, default="empty")
    abdominal_pain = models.CharField(max_length=255, default="empty")
    vaginal_bleeding = models.CharField(max_length=255, default="empty")
    rash = models.CharField(max_length=255, default="empty")
    itching = models.CharField(max_length=255, default="empty")
    vomiting = models.CharField(max_length=255, default="empty")
    headache = models.CharField(max_length=255, default="empty")
    blurred_vision = models.CharField(max_length=255, default="empty")
    convulsion = models.CharField(max_length=255, default="empty")
    gcs = models.CharField(max_length=10, default="empty")
    drt = models.CharField(max_length=10, default="empty")
    uop = models.CharField(max_length=10, default="empty")
    oxytocin_drop = models.CharField(max_length=10, default="empty")
    oxytocin_dose = models.CharField(max_length=10, default="empty")
    contractions = models.CharField(max_length=255, default="empty")
    membranes = models.CharField(max_length=255, default="empty")
    cervical_dilation = models.CharField(max_length=255, default="empty")
    effacement = models.CharField(max_length=255, default="empty")
    station = models.CharField(max_length=255, default="empty")

# Medication Model
class Medication(models.Model):
    client_name = models.CharField(max_length=20)
    given_by = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    dose = models.CharField(max_length=20)
    route = models.CharField(max_length=20)
    frequency = models.CharField(max_length=20)

# Order Model
class Order(models.Model):
    client_name = models.CharField(max_length=20)
    ordered_by = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    order_to = models.CharField(max_length=20)
    order_detail = models.TextField()
    result = models.TextField()
    done_by = models.CharField(max_length=20)

# Consent Model
class Consent(models.Model):
    client_name = models.CharField(max_length=20)
    health_pro_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    consent_detail = models.TextField()
    patient_response = models.TextField()

# Intervention Model
class Intervention(models.Model):
    client_name = models.CharField(max_length=20)
    health_pro_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    intervention_detail = models.TextField()
    
    
    
    
    
    
	







