# IDAI102-2505525-AashrutiAhuja-MedTimer_App
MedTimer is a Streamlit-based medicine management app featuring multi-dose scheduling, progress tracking, badges, and turtle animations, with a modern mint-teal design, motivational quotes, and weekly adherence reports for elderly users.

# Overview
MedTimer is an up-to-date Python- and Streamlit-built medicine management program that is intended to make elderly patients and chronically ill individuals maintain compliance with medication routines. The application enables the user to enter medicines with complete information like name, dose, time, frequency, and specific days. A well-defined, color-coded dashboard illustrates each dose's status—taken, due, or missed—allowing easy tracking and hassle-free monitoring.

MedTimer features sophisticated features such as progress tracking with Turtle graphics, motivational quotes, and achievement badges to promote good habits. People can see their complete medication history and print downloadable adherence reports for any month or week, not only the last one. With a mint–teal gradient scheme, white shadowed cards, and clear layout, MedTimer makes medication management a fun, rewarding, and visually soothing daily experience

# Problem & Purpose
Most older adults and chronic patients have difficulty coping with more than one medication, forgetting to take doses or losing count of where they are. Skipping doses can cause medical problems and anxiety for both patients and caregivers. Conventional reminder strategies tend to be stiff, formal, or hard for seniors to operate.

MedTimer was created to address these challenges by offering a easy, visual, and interactive way that is more like having a supportive friend rather than an unrelenting reminder. It makes it easy for users to see their complete medicine regimen all at once, monitor progress real-time, and commemorate adherence milestones through badges and turtle graphics.

The mission of MedTimer is to marry functionality with compassion—providing elderly users with clarity, motivation, and autonomy through accessible technology. By featuring historical tracking and report download options, the application allows caregivers and patients to view medication patterns and compliance trends over any period of time, which benefits long-term health awareness.

# App Features

 # Medicine Management Features
1.Add medicines with details: name, dose, time, frequency, and specific days (Mon–Sun).
2.Support for multiple doses per day and recurring options — Daily, Specific Days, or Monthly.
3.Color-coded status indicators:
     - 🟢 Taken – Dose completed
     - 🟡 Upcoming – Dose scheduled soon
     - 🔴 Missed – Dose not taken on time
4.Option to edit, delete, or update medicines anytime.
5.Clear confirmation table displaying all added medicines with dose, time, quantity, and frequency before saving.

 # Main Tracking & Interaction Features
1.Today’s Medicines List — displays all doses for the current day.
2.“Take” Button for each medicine to mark as completed instantly.
3.Progress Circle with live adherence percentage and animated Turtle graphic when score ≥ 80%.
4.Motivational Quotes that change dynamically to keep users encouraged.
5.Streak Counter (🔥 X Days) — tracks consecutive adherence days.
6.Achievement Badges awarded for consistency, like “Weekly Winner” or “Perfect Adherence”.
7.Settings Sidebar with customizable options:
     - Theme switch (Light / Dark)
     - Turtle graphic toggle
    - Custom reminder time (⏰)
8.Report Sidebar with:
    - Weekly statistics (total, taken, missed)
    - Option to view and download reports for any week or month, not just the recent one.
    - History view that shows all past medication data and adherence progress.
9.Reset and Update Buttons for clearing or modifying schedules quickly.

 # Design Features
1.Mint–Teal Gradient Background matching the HTML design version.
2.White Rounded Cards with soft shadows for a clean and calming look.
3.Color-coded medicine cards (green, yellow, red) to highlight status clearly.
4.Professional table design on the confirmation page for clarity and readability.
5.Large, accessible fonts and intuitive layout suitable for elderly users.

# App Flow
1. Welcome Screen
-Displays app logo and mascot with a friendly welcome message.
-Shows short description: “Track your medicines easily and never miss a dose.”
-Highlights key features (tracking, reminders, motivational tips, reports).
-Includes “Start” button → leads to Login Screen.

2. Login Screen
-User enters Name and Email to begin.
-Simulated login using Streamlit session state (no real authentication).
-After successful login → redirects to Add Medicine Page.

3. Add Medicine Page
-User inputs detailed medicine information:
    Medicine Name
    Dose / Quantity (e.g., 1 tablet)
    Time / Times per day (e.g., 9:00 AM, 9:00 PM)
    Days to take (Mon–Sun checkboxes)
-Add Medicine button → adds entry to a live confirmation table.
-Confirmation table allows:
    Review of added entries
    Edit incorrect data
    Delete entries
-Continue button → proceeds to Main Dashboard after confirming medicines.

4. Main Dashboard
-Displays Today’s Medicine List with:
     🟢 Taken 🟡 Upcoming 🔴 Missed statuses
     “Take” buttons to mark medicines as completed
-Shows a Progress Circle with live adherence percentage.
-Turtle 🐢 appears when adherence ≥ 80%.
-Includes Streak Counter (🔥 X days) for consistent days.
-Displays Motivational Quotes and Achievement Badges.
-Has a Top-Right History & Reports Panel for easy access.
-Reset button available at bottom → takes user back to confirmation table.

5. History & Reports Panel (Top-Right Corner)
-View complete medication history and past adherence trends.
-Select any week or month to view detailed performance.
-Download reports as PDF or CSV for doctors or caregivers.
-Displays:
      Weekly comparison
      Total adherence trends
      Summary of taken vs missed doses
-Always accessible from dashboard for quick review.

6. Reset Function
-Located on main dashboard.
-Returns user to the confirmation table from Add Medicine Page.
-Allows user to edit, delete, or re-enter medicines.
-Useful for starting a new schedule or correcting errors.

# Design Planning

Q.Who are your users?
-Primary Users: Elderly individuals who need reminders to take their medicines on time.
-Secondary Users: Caregivers or family members who help manage and monitor the medication schedule.

Q.What emotions should the app create?
-Comfort: The design should feel calm and reassuring, reducing anxiety around medication management.
-Motivation: Encourage users to stay consistent with their medicines using friendly visuals and progress indicators.
-Clarity: Information should be simple, clearly visible, and well-organized to avoid confusion.

Q.Color Palette
-Soft Green : Symbolizes health, freshness, and balance.
-White : Represents cleanliness and simplicity.
-Reason: Green and white together create a natural, fresh, and peaceful appearance that’s easy on the eyes and suitable for elderly users.

Q.Font
-Type: Sans-serif (e.g., Open Sans, Roboto, or Arial)
-Size: Large and readable
-Reason: Larger, clean fonts improve readability and accessibility for older users.

Q.Wireframe / Sketch Description
1. Welcome Screen
-App Name and Logo (green and white theme)
-“Login” or “Continue” button

2. Add Medicine Screen
-Text fields for:
  Medicine Name
  Dose
  Time
  Days of the week
-Buttons:
  “Save” 
  “Cancel” 

3. Dashboard (Main Screen)
-Header: “Today’s Medicines”
-List showing:
   Medicine Name
   Time
   Status (Take / Taken)
-Progress Circle: Shows how much of today’s medicine

# Streamlit Link
https://idai102-2505525-aashrutiahuja-medtimerapp-engudnyishgpvqypkrrz.streamlit.app/

