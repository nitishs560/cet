from django.db import models

# Create your models here.


class physics(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=400)
    image = models.CharField(max_length=400, default='')
    option1 = models.CharField(max_length=400)
    option2 = models.CharField(max_length=400)
    option3 = models.CharField(max_length=400)
    option4 = models.CharField(max_length=400)
    answer = models.CharField(max_length=10)
    rand = models.FloatField(default=0)

    def __str__(self):
        return self.question_id


class chemistry(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=400)
    image = models.CharField(max_length=400, default='')
    option1 = models.CharField(max_length=400)
    option2 = models.CharField(max_length=400)
    option3 = models.CharField(max_length=400)
    option4 = models.CharField(max_length=400)
    answer = models.CharField(max_length=10)
    rand = models.FloatField(default=0)

    def __str__(self):
        return self.question_id


class math(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=400)
    image = models.CharField(max_length=400, default='')
    option1 = models.CharField(max_length=400)
    option2 = models.CharField(max_length=400)
    option3 = models.CharField(max_length=400)
    option4 = models.CharField(max_length=400)
    answer = models.CharField(max_length=10)
    rand = models.FloatField(default=0)

    def __str__(self):
        return self.question_id


class student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=10)
    random_no = models.IntegerField()


defaultValues = []
for i in range(150):
    defaultValues.append(str(0))
defaultValues = ",".join(defaultValues)


class question_answers(models.Model):
    username = models.CharField(max_length=40)
    physics_questions = models.CharField(max_length=250)
    physics_answers = models.CharField(max_length=250)
    chemistry_questions = models.CharField(max_length=250)
    chemistry_answers = models.CharField(max_length=250)
    math_questions = models.CharField(max_length=250)
    math_answers = models.CharField(max_length=250)
    marked_answers = models.CharField(max_length=300, default=defaultValues)
    bookmark = models.CharField(max_length=300, default=defaultValues)
    invalid = models.CharField(max_length=300, default=defaultValues)
    attempted = models.CharField(max_length=300, default=defaultValues)
    time_left = models.IntegerField(default=10800000)

    def __str__(self):
        return self.username


class results(models.Model):
    username = models.CharField(max_length=40)
    physics_marks = models.IntegerField(default=0)
    chemistry_marks = models.IntegerField(default=0)
    math_marks = models.IntegerField(default=0)
    total_marks = models.IntegerField(default=0)

    def __str__(self):
        return self.username


