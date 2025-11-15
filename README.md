# KAUN-BANEGA-CROREPATI
A fun quiz-based Python game inspired by the famous Indian TV show
This is my second project.

---------------------------- OVERVIEW ----------------------------

This project is a command-line game based on Kaun Banega Crorepati (KBC).
The player answers multiple-choice questions, climbs the money ladder, and uses lifelines just like in the real show.

The game includes:

1. 16 random questions
2. Money ladder from ₹5,000 to ₹7 Crore
3. 4 lifelines (50-50, Audience Poll, Flip Question, Phone-a-Friend)
4. Safe levels
5. Quit option
6. Smooth input validation
7. Randomized question order

---------------------------- FEATURES ----------------------------

1. Multiple Choice Questions (MCQs)
   Each question comes with 4 options: A, B, C, D.

2. Money Ladder
   You earn a fixed amount after each correct answer:
   ₹5,000 → ₹10,000 → ₹15,000 → ₹20,000 → ₹25,000 → ₹50,000 → ₹1,00,000  → ₹2,00,000 → ₹3,00,000 → ₹5,00,000 → ₹7,50,000 → ₹12,50,000  → ₹25,00,000 → ₹50,00,000 → ₹1 Crore → ₹7 Crore

3. Safe Levels
   These amounts are guaranteed even after a wrong answer:
   ₹25,000; ₹5,00,000; ₹7 Crore

4. Lifelines
   All lifelines can be used once:
   Lifeline	Description:
   50-50 ->	Removes 2 wrong options
   Audience Poll ->	Random percentage distribution
   Phone-a-Friend -> Gives a hint (not always correct!)
   Flip the Question -> Replaces the current question
   
5. Quit Anytime
   Type quit to walk away with your current amount.

---------------------------- HOW TO RUN THE GAME ----------------------------

Requirements:
- Python 3.14.0
- No external libraries required

- Steps
  1. Clone or download the project
  2. Open terminal in project folder
  3. Run the game using:
     python KBC.py

---------------------------- PROJECT STRUCTURE ----------------------------

📁 KBC-Game:
│–– KBC.py        # Main game file
|–– README.md     # Project documentation

---------------------------- ACKNOWLEDGEMENT ----------------------------

This is my second Python project, and it helped me practice:
1. functions
2. loops
3. conditionals
4. lists
5. input validation
6. random operations
