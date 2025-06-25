from django.test import TestCase
from .models import Question, Choice

import datetime
from django.utils import timezone


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_past_question(self):

        time = timezone.now() - datetime.timedelta(days=2)
        future_question = Question(question_text="Comment ça va ?", pub_date=time)
        
        self.assertIs(future_question.was_published_recently(), False)



    def test_have_more_than_one_choice_with_question_having_no_choice(self):
    	question_object = Question(id=50, question_text="what's up ?", pub_date=timezone.now())

    	self.assertIs(question_object.have_more_than_one_choice(), False)