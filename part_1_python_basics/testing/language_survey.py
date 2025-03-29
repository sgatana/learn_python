from survey import AnonymousSurvey

question = "How many programming languages do you know/use?"

language_survey = AnonymousSurvey(question)

# show the question and store responses to the question
language_survey.show_question()

while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_responses(response)

# show survey results
print("\nThank you to everyone who participated in the survey!")
language_survey.display_results()
