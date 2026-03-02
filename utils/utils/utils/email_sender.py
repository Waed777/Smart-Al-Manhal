import yagmail
import pandas as pd

def send_email(teacher_name, pdf_path):
    teachers_df = pd.read_csv("data/teachers.csv")
    email = teachers_df.loc[teachers_df['اسم المعلمة'] == teacher_name, 'البريد الإلكتروني'].values[0]

    yag = yagmail.SMTP("waedamari1@gmail.com", "YOUR_EMAIL_APP_PASSWORD")

    subject = "تنبيه آلي – خطة علاجية جديدة"
    body = f"""
    <h3>مرحباً {teacher_name}</h3>
    <p>تم توليد خطتك العلاجية للمادة. يرجى مراجعة التقرير المرفق.</p>
    <p>Smart Score و الحالة مرفقة داخل PDF.</p>
    <p>CC: الإدارة والمديرة</p>
    """
    yag.send(to=email, subject=subject, contents=body, attachments=pdf_path)
