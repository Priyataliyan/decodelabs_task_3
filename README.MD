# AI Recommendation System

## Project Title
AI Recommendation System Using Preference Matching

## Project Description
This project is a simple Artificial Intelligence based recommendation
system that recommends movies based on the user's interests.

The system takes user preferences such as action, comedy, sci-fi, romance,
or thriller and matches them with the genres of available movies.

## Objective
The main objective of this project is to build a basic recommendation
system using user preferences and simple similarity logic.

## Dataset
The dataset contains the following columns:

- name
- genres

The `name` column contains the movie name.

The `genres` column contains the genres associated with each movie.

## Technology Used
- Python
- CSV
- VS Code

## Recommendation Logic
The system uses a simple similarity matching technique.

For every genre that matches the user's preference, the movie receives
one similarity score.

For example:

User Preferences:
- sci-fi
- action

Movie Genres:
- sci-fi
- action
- thriller

Similarity Score:
- 2

Movies with matching preferences are displayed as recommendations.

## Project Workflow

1. Load the movie data
2. Take user interests as input
3. Process the user's preferences
4. Compare user preferences with movie genres
5. Calculate the similarity score
6. Sort the matching movies
7. Display recommended movies

## Project Structure

AI_Recommendation_System/
│
├── dataset.csv
├── main.py
├── requirements.txt
└── README.md

## Installation

No external Python libraries are required for the current project.

Make sure Python is installed on your computer.

Check Python using:

python --version

## How to Run

Run the following command in the VS Code terminal:

python main.py

## Example Input

sci-fi, action

## Expected Output

The program will display:

- Matching movies
- Similarity scores
- Recommended movies

Example:

Inception - Similarity Score: 2
Avengers: Endgame - Similarity Score: 2
Interstellar - Similarity Score: 1

## Conclusion

This project demonstrates the basic concepts of recommendation systems,
user preference matching, pattern matching, similarity scoring, and
personalized recommendations using Python.
