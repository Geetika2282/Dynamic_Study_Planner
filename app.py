import streamlit as st
import pandas as pd
import numpy as np
import random
import time
import requests

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("final_data.csv")
    return df

df = load_data()

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Generate Timetable", "To-Do List", "Pomodoro Timer", "Affirmations"])

# ----------------------- 📅 Generate Timetable Page ------------------------
if page == "Generate Timetable":
    st.title("📚 Personalized Study Plan Generator")

    questions = [
        "How focused are you while studying? (1-10)",
        "Do you prefer studying in long hours or short sessions? (1 for short, 10 for long)",
        "How well do you retain information? (1-10)",
        "How easily do you get distracted? (1-10, lower is better)",
        "Do you prefer morning or night study? (1 for morning, 10 for night)"
    ]

    st.subheader("📝 Answer a few questions about your study habits")
    responses = [st.slider(q, 1, 10, 5) for q in questions]

    study_score = (responses[0] * 2 + responses[1] + responses[2] - responses[3] + responses[4]) / 5

    st.subheader("📌 Personalize Your Study Plan")
    subjects = st.text_input("Enter subjects separated by commas (e.g., Math, Science, English)")
    study_hours_per_week = st.slider("How many hours can you study per week?", 5, 50, 15)
    previous_grade = st.slider("What was your previous grade? (out of 100)", 30, 100, 75)

    if previous_grade < 60:
        study_hours_per_week += 5  # Increase study time if grade is low

    subjects = [sub.strip() for sub in subjects.split(",") if sub.strip()]

    if st.button("📅 Generate Timetable"):

        def fitness_function(study_hours, study_score):
            return -abs(study_score - (3 + 0.4 * study_hours))

        def mutate(child):
            mutation_factor = random.uniform(-1, 1)
            return max(0, child + mutation_factor)

        population = [random.randint(1, 8) for _ in range(10)]
        for _ in range(50):
            population = sorted(population, key=lambda x: -fitness_function(x, study_score))
            best_parents = population[:4]
            children = [mutate(random.choice(best_parents)) for _ in range(6)]
            population = best_parents + children

        optimal_study_hours_per_day = round(np.mean(population))

        st.subheader("📅 Your Personalized Study Timetable")
        time_slots = [f"{hour}:00 - {hour + 1}:00" for hour in range(24)]
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        study_schedule = pd.DataFrame("", index=time_slots, columns=weekdays)
        for _ in range(study_hours_per_week):
            day = random.choice(weekdays)
            hour = random.choice(time_slots)
            subject = random.choice(subjects) if subjects else "Study"
            study_schedule.at[hour, day] = subject

        st.dataframe(study_schedule)

# ----------------------- ✅ To-Do List Page ------------------------
elif page == "To-Do List":
    st.title("📋 To-Do List")

    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    task_input = st.text_input("Add a new task:")
    if st.button("➕ Add Task"):
        if task_input:
            st.session_state.tasks.append({"task": task_input, "completed": False})

    st.subheader("📝 Your Tasks:")
    updated_tasks = []

    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([6, 1])
        col1.write("✅ " + task["task"] if task["completed"] else "❌ " + task["task"])
        if col2.button("✔️", key=f"complete_{i}"):
            task["completed"] = not task["completed"]

        # Append non-completed tasks to keep them
        updated_tasks.append(task)

    # Button to clear completed tasks
    if st.button("🗑️ Clear Completed Tasks"):
        st.session_state.tasks = [task for task in updated_tasks if not task["completed"]]
        st.rerun()  # ✅ Forces Streamlit to refresh and apply changes

# ----------------------- ⏳ Pomodoro Timer Page ------------------------
elif page == "Pomodoro Timer":
    st.title("⏳ Pomodoro Timer")

    if "timer_running" not in st.session_state:
        st.session_state.timer_running = False

    work_time = st.slider("Work Time (minutes)", 10, 60, 25)
    break_time = st.slider("Break Time (minutes)", 5, 30, 5)

    col1, col2 = st.columns(2)

    if col1.button("▶ Start Pomodoro"):
        st.session_state.timer_running = True
        st.success("📖 Focus and study now!")

        work_seconds = work_time * 60

        for i in range(work_seconds):
            if not st.session_state.timer_running:
                st.warning("⏹ Timer Stopped!")
                st.stop()
            time.sleep(1)

        st.success("🚀 Break Time! Relax now.")

        time.sleep(break_time * 60)
        st.balloons()
        st.success("✅ Pomodoro session complete!")

    if col2.button("⏹ Stop Timer"):
        st.session_state.timer_running = False
        st.warning("⏹ Timer Stopped!")

# ----------------------- 🌟 Affirmations Page ------------------------
elif page == "Affirmations":
    st.title("🌟 Daily Affirmation")

    def get_quote():
        try:
            response = requests.get("https://zenquotes.io/api/random")
            if response.status_code == 200:
                quote_data = response.json()
                return quote_data[0]["q"]  # Extracts the quote text
            else:
                return "Failed to fetch quote. Stay positive and keep going!"
        except:
            return "Network issue! Stay positive and keep going!"

    if "quote" not in st.session_state:
        st.session_state.quote = get_quote()

    # Center-align and increase font size
    st.markdown(
        f"<div style='text-align: center; font-size: 24px; font-weight: bold; color: #2E86C1;'>{st.session_state.quote}</div>",
        unsafe_allow_html=True
    )

    if st.button("🔄 New Quote"):
        st.session_state.quote = get_quote()
        st.rerun()  # ✅ Refreshes the page to show the new quote
