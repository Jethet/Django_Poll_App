# This code creates a django.test.TestCase subclass with a method that creates
# a Question instance with a pub_date in the future. Then the output is checked
# of was_published_recently(). This should be False.

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose
        pub_date is in the future:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
