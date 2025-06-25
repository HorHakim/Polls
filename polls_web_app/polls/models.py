import datetime
from django.db import models

from django.utils import timezone

class Question(models.Model):
    # id = 
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    # choice_set =

    def __str__(self):
        return self.question_text




    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)








    def have_more_than_one_choice(self):
        return self.choice_set.count() >= 1

    @classmethod
    def get_all_questions_with_more_than_one_choice(cls):
    	return [question for question in cls.objects.all() if question.have_more_than_one_choice()] # à revoir !!!!






class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    

    def __str__(self):
        return self.choice_text


"""
Question : 
	id : 0
	question_text : A quelle heure voulez-vous reserver une table ?
	pub_date : 23/06/2025

Choice :
	id : 0
	question_id : 0
	choice_text : olala, j'ai vraiment super faim 19 h
	votes : 0


Choice :
	id : 1
	question_id : 0
	choice_text : Miam on va manger 20 h
	votes : 0

"""