Weather Graph Generator

A simple Python program that prompts the user to enter temperatures for a chosen number of days and generates a clean line graph using Matplotlib.
The graph automatically highlights the highest and lowest temperatures.

Features

Input number of days

Temperature input for each day

Automatically generated line graph

Highlights:

🔴 Highest temperature

🟢 Lowest temperature

Fixed Y-axis scale (0°C to 60°C) for neat comparisons

Easy to run, beginner-friendly Python project

🖥️ Technologies Used

Python 3

Matplotlib

📦 Installation

Clone the repository:

git clone https://github.com/<your-username>/<your-repo-name>.git


Install required dependencies:

pip install matplotlib


Run the program:

python weather_graph.py

📘 Usage

Once you run the script, you will be prompted to:

Enter the number of days

Enter the temperature for each day

The program will then display a graph similar to this:

A blue line showing temperatures across days

A red dashed line marking the highest temperature

A green dashed line marking the lowest temperature



🔍 How It Works

The script:

Collects user input

Stores all temperatures in a list

Finds the highest and lowest values

Uses Matplotlib to:

Plot the temperature line

Add horizontal guide lines for min & max

Customize graph appearance (labels, title, axes)



This project is available for personal and educational use.

