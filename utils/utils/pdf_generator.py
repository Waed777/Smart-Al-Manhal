from fpdf import FPDF

def generate_pdf(teacher_name, subject, plan, tests, video_links):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"خطة علاجية – {teacher_name} – {subject}", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, plan)
    pdf.multi_cell(0, 8, tests)
    pdf.multi_cell(0, 8, "\n".join(video_links))
    path = f"reports/{teacher_name}_{subject}.pdf"
    pdf.output(path)
    return path
