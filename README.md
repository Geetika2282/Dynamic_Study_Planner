# Dynamic_Study_Planner, is a web-based platform designed to help users organize their schedules and routines effectively while boosting productivity. It combines Artificial Intelligence (AI) and Genetic Algorithms (GA) to generate personalized study or work timetables based on user preferences, their existing schedules, and workload requirements.

The platform has a clean UI featuring a sidebar with tools like:

Questionnaire: Captures user inputs about their preferred study or work hours and productivity patterns.
Add Timetable: Lets users upload their current schedule (PDFs of school, work, etc.) to integrate it with a customized plan.
To-Do List: Users can add, delete, and manage their daily tasks easily.
Pomodoro Timer: Facilitates focused work using the Pomodoro technique for time management.
Affirmations: Displays random motivational quotes to enhance a positive mindset.
Calendar: Simplifies navigating dates and planning long-term schedules.
Core functionality revolves around personalized timetable recommendations:

Using Genetic Algorithms, we merge the user’s existing timetable with the additional hours they wish to dedicate to tasks like studies or personal work. The GA optimizes hours by adjusting task distribution while respecting constraints like total weekly hours, daily availability, and user preferences (e.g., morning or evening productivity).
The platform includes a Machine Learning-driven clustering mechanism to group similar user preferences and improve timetable suggestions over time. Additionally, the fitness function ensures task allocations are feasible and efficient.

Key technical aspects:

Genetic Algorithm for optimizing timetables.
Integration with ML-based recommendation systems using clustering and imputation methods.
A modular approach where the timetable logic accounts for user-defined parameters such as time of day and specific days for tasks.
For user engagement, we added practical tools like a to-do list manager, a calendar for date navigation, and a Pomodoro timer to encourage productive work sessions.

This project stands out for its innovative use of Genetic Algorithms in real-world time management and its blend of automation with user personalization.

The motivation stemmed from a common problem: efficiently managing time while balancing personal, academic, or professional responsibilities. Existing tools focus on static schedules or generic planners. I wanted to create a system that dynamically adapts to individual preferences and routines. By using Genetic Algorithms, I could bring an element of optimization to task scheduling, making the solution both personalized and efficient.

Additionally, integrating AI-based clustering added the ability to make smart recommendations tailored to user behavior. The positive response I received during testing motivated me further, as users found the platform extremely helpful in reducing scheduling stress and improving their daily routines.

