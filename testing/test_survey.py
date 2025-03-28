from survey import AnonymousSurvey
import pytest


@pytest.fixture
def language_survey():
    """A survey that will be available to all tests"""
    question = "What is your favorite programming language(s)"
    lang_survey = AnonymousSurvey(question)
    return lang_survey


def test_store_single_response(language_survey):
    """Test a single response is stored correctly"""
    language_survey.store_responses("Python")
    assert "Python" in language_survey.responses


def test_store_multiple_responses(language_survey):
    """Test multiple responses"""
    responses = ["Python", "Java", "C++", 'Javascript']
    for response in responses:
        language_survey.store_responses(response)
    for response in responses:
        assert response in language_survey.responses
