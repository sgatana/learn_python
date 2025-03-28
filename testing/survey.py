class AnonymousSurvey:
    """Collect anonymous question to a survey question"""

    def __init__(self, question):
        """Store questions and prepare responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show question"""
        print(self.question)

    def store_responses(self, new_response):
        """Store a single response"""
        self.responses.append(new_response)

    def display_results(self):
        """Display responses"""
        print("Survey results")
        for response in self.responses:
            print(f"- {response}")


