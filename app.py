from groq import Groq
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def qualify_lead(name, course_interest, budget, timeline, background):
    prompt = f"""
You are an expert admissions counselor at Kraftshala, India's largest marketing-focused edtech platform with a 94% placement rate.

A student has enquired about joining Kraftshala. Your job is to qualify this lead for the admissions team.

Student Details:
- Name: {name}
- Course Interest: {course_interest}
- Budget: {budget}
- Timeline to Join: {timeline}
- Current Background: {background}

Provide:
1. LEAD SCORE: High / Medium / Low
2. REASON: 2-3 sentences explaining the score
3. FOLLOW-UP ACTION: One specific, personalized action for the admissions team
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message.content

st.set_page_config(page_title="Kraftshala Lead Qualifier", page_icon="🎯")
st.title("🎯 Kraftshala Admissions Lead Qualifier")
st.markdown("AI-powered lead scoring for the admissions team")

with st.form("lead_form"):
    name = st.text_input("Student Name")
    course_interest = st.selectbox("Course Interest", [
        "Marketing & Sales (PGP)",
        "Digital Marketing",
        "Content & Brand Management",
        "Media Planning"
    ])
    budget = st.selectbox("Budget Range", [
        "Under ₹50,000",
        "₹50,000 - ₹1,00,000",
        "₹1,00,000 - ₹2,00,000",
        "Above ₹2,00,000"
    ])
    timeline = st.selectbox("Timeline to Join", [
        "Immediately",
        "Within 1 month",
        "1-3 months",
        "3-6 months",
        "Just exploring"
    ])
    background = st.text_area("Student Background", placeholder="e.g. Final year B.Com student, interested in digital marketing...")
    submitted = st.form_submit_button("Qualify Lead")

if submitted:
    if name and background:
        with st.spinner("Analysing lead..."):
            result = qualify_lead(name, course_interest, budget, timeline, background)
        st.markdown("### 📊 Qualification Result")
        st.markdown(result)
    else:
        st.warning("Please fill in at least the name and background.")