import wx
from datetime import datetime
from certificate import MedicalCertificate

class CertificateApp(wx.Frame):
    def __init__(self, *args, **kw):
        super(CertificateApp, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#DCE3E8')

        vbox = wx.BoxSizer(wx.VERTICAL)

        # Date Input
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Fecha (dd/mm/aaaa):')
        st1.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.date = wx.TextCtrl(panel, style=wx.BORDER_SUNKEN)
        self.date.SetMinSize((300, -1))
        self.date.SetValue(datetime.now().strftime("%d/%m/%Y"))
        hbox1.Add(self.date, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.ALL, border=15)

        # Patient Name Input
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Nombre del Paciente:')
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        self.patient_name = wx.TextCtrl(panel, style=wx.BORDER_SUNKEN|wx.TE_LEFT)
        hbox2.Add(self.patient_name, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Address Input
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(panel, label='Dirección:')
        hbox3.Add(st3, flag=wx.RIGHT, border=8)
        self.address = wx.TextCtrl(panel)
        hbox3.Add(self.address, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Phone Number Input
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st4 = wx.StaticText(panel, label='Teléfono:')
        hbox4.Add(st4, flag=wx.RIGHT, border=8)
        self.phone_number = wx.TextCtrl(panel)
        hbox4.Add(self.phone_number, proportion=1)
        vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Company Input
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        st5 = wx.StaticText(panel, label='Empresa:')
        hbox5.Add(st5, flag=wx.RIGHT, border=8)
        self.company = wx.TextCtrl(panel)
        hbox5.Add(self.company, proportion=1)
        vbox.Add(hbox5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Job Title Input
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        st6 = wx.StaticText(panel, label='Puesto de Trabajo:')
        hbox6.Add(st6, flag=wx.RIGHT, border=8)
        self.job_title = wx.TextCtrl(panel)
        hbox6.Add(self.job_title, proportion=1)
        vbox.Add(hbox6, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # ID Number Input
        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        st7 = wx.StaticText(panel, label='Número de Cédula:')
        hbox7.Add(st7, flag=wx.RIGHT, border=8)
        self.id_number = wx.TextCtrl(panel)
        hbox7.Add(self.id_number, proportion=1)
        vbox.Add(hbox7, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Diagnosis Input
        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        st8 = wx.StaticText(panel, label='Diagnóstico (CIE10):')
        hbox8.Add(st8, flag=wx.RIGHT, border=8)
        self.cie10_name = wx.TextCtrl(panel)
        hbox8.Add(self.cie10_name, proportion=1)
        vbox.Add(hbox8, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # CIE10 Code Input
        hbox9 = wx.BoxSizer(wx.HORIZONTAL)
        st9 = wx.StaticText(panel, label='Código CIE10:')
        hbox9.Add(st9, flag=wx.RIGHT, border=8)
        self.cie10_code = wx.TextCtrl(panel)
        hbox9.Add(self.cie10_code, proportion=1)
        vbox.Add(hbox9, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Days Granted Input
        hbox10 = wx.BoxSizer(wx.HORIZONTAL)
        st10 = wx.StaticText(panel, label='Días Otorgados:')
        hbox10.Add(st10, flag=wx.RIGHT, border=8)
        self.days_granted = wx.TextCtrl(panel)
        hbox10.Add(self.days_granted, proportion=1)
        vbox.Add(hbox10, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Checkboxes
        self.checkbox_illness = wx.CheckBox(panel, label='Enfermedad')
        self.checkbox_illness.SetBackgroundColour('#DCE3E8')
        vbox.Add(self.checkbox_illness, flag=wx.LEFT|wx.TOP, border=10)
        self.checkbox_symptoms = wx.CheckBox(panel, label='Presenta síntomas')
        vbox.Add(self.checkbox_symptoms, flag=wx.LEFT|wx.TOP, border=10)
        self.checkbox_isolation = wx.CheckBox(panel, label='Aislamiento/Teletrabajo')
        vbox.Add(self.checkbox_isolation, flag=wx.LEFT|wx.TOP, border=10)

        # Generate Certificate Button
        btn_generate = wx.Button(panel, label='Generar Certificado')
        btn_generate.SetBackgroundColour('#4CAF50')
        btn_generate.SetForegroundColour('white')
        btn_generate.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        vbox.Add(btn_generate, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=20)
        btn_generate.Bind(wx.EVT_BUTTON, self.OnGenerateCertificate)

        panel.SetSizer(vbox)

    def OnGenerateCertificate(self, event):
        try:
            # Obtener los datos de los campos
            today = self.date.GetValue()
            patient_name = self.patient_name.GetValue()
            address = self.address.GetValue()
            phone_number = self.phone_number.GetValue()
            company = self.company.GetValue()
            job_title = self.job_title.GetValue()
            id_number = self.id_number.GetValue()
            cie10_name = self.cie10_name.GetValue()
            cie10_code = self.cie10_code.GetValue()
            days_granted = int(self.days_granted.GetValue())

            # Obtener valores de los checkboxes
            illness = self.checkbox_illness.GetValue()
            symptoms = self.checkbox_symptoms.GetValue()
            isolation = self.checkbox_isolation.GetValue()

            # Crear y generar el certificado
            certificate = MedicalCertificate(
                patient_name=patient_name,
                address=address,
                phone_number=phone_number,
                company=company,
                job_title=job_title,
                id_number=id_number,
                cie10_name=cie10_name,
                cie10_code=cie10_code,
                days_granted=days_granted
            )

            # Aquí puedes agregar lógica adicional para rellenar el certificado con la información de los checkboxes si lo necesitas.

            certificate.make_certificate()

            # Mostrar mensaje de éxito
            wx.MessageBox('¡El certificado se ha generado correctamente!', 'Éxito', wx.OK | wx.ICON_INFORMATION)
        except Exception as e:
            wx.MessageBox(f'Ocurrió un error al generar el certificado: {e}', 'Error', wx.OK | wx.ICON_ERROR)
            print(e)

if __name__ == '__main__':
    app = wx.App()
    frm = CertificateApp(None, title='Generador de Certificados Médicos', size=(500, 700))
    frm.Show()
    app.MainLoop()
