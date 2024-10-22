# certificate.py
from openpyxl import load_workbook
from datetime import datetime, timedelta
import win32com.client as win32
import os

from utils import translate_day, translate_month

class MedicalCertificate:

    def __init__(self, 
                 patient_name: str, 
                 address: str, 
                 phone_number: str, 
                 company: str, 
                 job_title: str, 
                 id_number: str, 
                 cie10_name: str, 
                 cie10_code: str, 
                 days_granted: int):
        self.patient_name = patient_name
        self.address = address
        self.phone_number = phone_number
        self.company = company
        self.job_title = job_title
        self.id_number = id_number
        self.cie10_name = cie10_name
        self.cie10_code = cie10_code
        self.days_granted = days_granted
        self.today = datetime.now()
        self.workbook = load_workbook('../templates/medical_certificate_template.xlsx')
        self.sheet = self.workbook.active

    def __fill_patient_info(self) -> None:
        """Fill in patient information in the Excel sheet."""
        self.sheet['K20'] = self.patient_name
        self.sheet['K22'] = self.address
        self.sheet['K24'] = self.phone_number
        self.sheet['K26'] = self.company
        self.sheet['K28'] = self.job_title
        self.sheet['K30'] = self.id_number
        self.sheet['K32'] = f"HC-{self.id_number}"
        self.sheet['H35'] = self.cie10_name
        self.sheet['H37'] = self.cie10_code

    def __fill_dates_and_rest_period(self) -> None:
        """Fill in the dates for the rest period in the Excel sheet."""
        day_written = translate_day(self.today.strftime('%A'))
        formatted_date = self.today.strftime('%d/%m/%Y')
        self.sheet['K17'] = f'PORTOVIEJO {day_written} {formatted_date}'

        # Rest period - From (G49) and To (G51)
        start_date = self.today
        end_date = start_date + timedelta(days=self.days_granted)

        day_start_written = translate_day(start_date.strftime('%A'))
        month_start_written = translate_month(start_date.strftime('%B'))
        formatted_start_date = start_date.strftime('%d/%m/%Y')
        self.sheet['G49'] = f"{day_start_written} {start_date.day} de {month_start_written} del {start_date.year} ({formatted_start_date})"

        day_end_written = translate_day(end_date.strftime('%A'))
        month_end_written = translate_month(end_date.strftime('%B'))
        formatted_end_date = end_date.strftime('%d/%m/%Y')
        self.sheet['G51'] = f"{day_end_written} {end_date.day} de {month_end_written} del {end_date.year} ({formatted_end_date})"

    def __fill_symptoms_and_description(self) -> None:
        """Fill in the symptoms and general description in the Excel sheet."""
        self.sheet['J39'] = "X"  # Mark "Yes" for symptoms
        self.sheet['S39'] = ""   # Leave "No" empty
        self.sheet['J41'] = "X"  # Mark "Illness"
        self.sheet['S41'] = ""   # Leave "Isolation/Telework" empty
        self.sheet['I42'] = "General Contingency"
        self.sheet['J44'] = "FEVER - DYSPHAGIA - GENERAL DISCOMFORT"

    def __fill_days_granted(self) -> None:
        """Fill in the number of days granted in the Excel sheet."""
        total_hours = self.days_granted * 24
        days_written = "THREE"  # You could automate this as needed
        self.sheet['J47'] = f"{self.days_granted} ({days_written}) ({total_hours} HOURS)"


    def __save_certificate(self) -> None:
        """Save the generated certificate in both Excel and PDF formats."""
        folder_name: str = f'medical_certificates/{self.id_number}_{self.patient_name.replace(" ", "_")}'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        excel_filename: str = f'{folder_name}/medical_certificate_{self.id_number}_{self.today.strftime("%Y%m%d_%H%M%S")}.xlsx'
        self.workbook.save(excel_filename)
        print(f"Certificate generated successfully! Saved as: {excel_filename}")


        try:
            excel_app = win32.Dispatch('Excel.Application')
            excel_app.Visible = False
            workbook = excel_app.Workbooks.Open(os.path.abspath(excel_filename))

            pdf_filename = os.path.abspath(f'../{folder_name}/medical_certificate_{self.id_number}_{self.today.strftime("%Y%m%d_%H%M%S")}.pdf')
            workbook.ExportAsFixedFormat(0, pdf_filename)  # 0 = PDF format

            print(f"Certificate generated successfully! Saved as: {excel_filename} and {pdf_filename}")
        except Exception as e:
            print(f"Error generating PDF: {e}")

        finally:
            print(excel_filename)
            workbook.Close(False)
            excel_app.Quit()

    def make_certificate(self) -> None:
        self.__fill_patient_info()
        self.__fill_dates_and_rest_period()
        self.__fill_symptoms_and_description()
        self.__fill_symptoms_and_description()
        self.__fill_days_granted()
        self.__save_certificate()

