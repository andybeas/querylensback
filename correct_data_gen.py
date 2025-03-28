import pandas as pd

# Load the ACS data
acs_data = pd.read_csv('./llm_finetuning/acs_data.csv')

# Prepare a list of questions and corresponding answers based on the dataset
question_answer_data = []

# Generate a list of questions from the dataset
for index, row in acs_data.iterrows():
    state = row['State']
    county = row['County']
    total_pop = row['TotalPop']
    men_pop = row['Men']
    women_pop = row['Women']
    hispanic = row['Hispanic']
    white = row['White']
    black = row['Black']
    employed = row['Employed']
    mean_commute = row['MeanCommute']
    
    question_answer_data.append({
        "Question": f"What is the total population of {county}, {state}?",
        "Correct Answer": str(total_pop)
    })
    
    question_answer_data.append({
        "Question": f"What is the percentage of Hispanic people in {county}, {state}?",
        "Correct Answer": str(hispanic) + "%"
    })
    
    question_answer_data.append({
        "Question": f"What is the percentage of White people in {county}, {state}?",
        "Correct Answer": str(white) + "%"
    })
    
    question_answer_data.append({
        "Question": f"What is the percentage of Black people in {county}, {state}?",
        "Correct Answer": str(black) + "%"
    })
    
    question_answer_data.append({
        "Question": f"How many people are employed in {county}, {state}?",
        "Correct Answer": str(employed)
    })
    
    question_answer_data.append({
        "Question": f"What is the mean commute time in {county}, {state}?",
        "Correct Answer": str(mean_commute) + " minutes"
    })

# Convert the question-answer data into a DataFrame
df_question_answers = pd.DataFrame(question_answer_data)

# Save the generated question-answer dataset to a CSV file
df_question_answers.to_csv('./llm_finetuning/generated_correct_answers.csv', index=False)

print("The predefined question-answer dataset has been generated and saved as 'generated_correct_answers.csv'.")
