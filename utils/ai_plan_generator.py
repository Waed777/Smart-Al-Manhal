import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_plan(teacher_name, subject, book_text):
    prompt = f"""
    أنت مساعد ذكي للتعليم. أنشئ خطة علاجية مفصلة وملخصة من الكتاب التالي للمعلمة {teacher_name} لمادة {subject}. 
    قم بتوليد:
    - خطة أسبوعية
    - اختبارات قصيرة لكل فصل
    - اقتراح روابط فيديو تعليمية
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    content = response.choices[0].message.content
    # لفصل المحتوى لقسم الخطة والاختبارات والفيديوهات
    plan = content
    tests = "اختبارات قصيرة مستخرجة"
    video_links = ["https://youtube.com/example1", "https://youtube.com/example2"]
    return plan, tests, video_links
