# 🎯 Kraftshala Admissions Lead Qualifier

An AI-powered lead scoring tool built for edtech admissions teams.

## The Problem
Admissions teams at edtech companies manually evaluate hundreds of inbound student enquiries every day. This is slow, inconsistent, and pulls counsellors away from high-intent leads that actually convert.

## The Solution
This tool uses an LLM to instantly score each inbound lead as High / Medium / Low, explain the reasoning, and suggest a specific follow-up action — so the admissions team focuses their energy where it matters most.

## What It Does
- Takes student details as input — course interest, budget, timeline, background
- Scores the lead using AI
- Provides a clear reason for the score
- Suggests one specific follow-up action for the admissions team

## Impact It Would Drive
- Reduce time spent per lead by admissions team
- Improve conversion rate by prioritising high-intent leads
- Standardise qualification criteria across the team

## Built With
- Python
- Streamlit
- Groq API (LLaMA 3.3 70B)

## Live Demo
[Click here to try the app](https://kraftshala-lead-qualifier-jrrmuqcj94zfe5crurt3pj.streamlit.app/)

## How to Run Locally
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Groq API key to a `.env` file as `GROQ_API_KEY=your-key`
4. Run: `streamlit run app.py`