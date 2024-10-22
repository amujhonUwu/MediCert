# main.py
from certificate import MedicalCertificate

if __name__ == "__main__":
    try:
        certificate = MedicalCertificate(
            patient_name="Juan Perez",
            address="Main Street #123, Portoviejo",
            phone_number="0991234567",
            company="XYZ Company",
            job_title="Supervisor",
            id_number="1234567890",
            cie10_name="Dengue Fever",
            cie10_code="A90",
            days_granted=3
        )
        
        certificate.make_certificate()
    except FileNotFoundError as e:
        print(f"File not found: medical_certificate_template.xlsx: {e}")
