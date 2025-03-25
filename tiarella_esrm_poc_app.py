
import streamlit as st

# Title
st.title("Tiarella ESRM Risk Rating Tool (POC)")
st.subheader("Environmental & Social Risk Categorization Engine (IFC PS 2 - PS 8)")

st.markdown("Answer the following questions to assess the ESG risk category of a client or project.")

# Define a few ESG sample trigger questions
questions = {
    "Labour & Working Conditions": [
        ("Does the obligor have vulnerable or exploited workers?", "C", 0.0),
        ("Has the obligor recently retrenched workers without proper process?", "B", 0.5),
        ("Is there a complete lack of employment policies or direction?", "B", 0.5),
    ],
    "Pollution & Resource Efficiency": [
        ("Does the customer's operations use harmful chemicals?", "C", 0.0),
        ("Are there visible signs of environmental degradation?", "A", 4.0),
    ],
    "Community Health & Safety": [
        ("Are public protests common around the project area?", "A", 4.0),
        ("Does the project increase noise, dust, or emissions for local communities?", "A", 4.0),
    ]
}

total_score = 0.0
ratings = []

# Display questions
for category, items in questions.items():
    st.markdown(f"### {category}")
    for q_text, rating, score in items:
        response = st.checkbox(q_text)
        if response:
            total_score += score
            ratings.append(rating)

# Determine final risk rating
if total_score >= 10:
    final_rating = "A (High Risk)"
elif total_score >= 3:
    final_rating = "B (Medium Risk)"
else:
    final_rating = "C (Low Risk)"

# Display Results
st.markdown("---")
st.subheader("Results")
st.write(f"**Total ESG Risk Score:** {total_score}")
st.write(f"**Final Risk Category:** {final_rating}")
