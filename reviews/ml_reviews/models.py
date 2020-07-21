from django.db import models


class Review(models.Model):
    text = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    sampled_date = models.DateTimeField('date sampled', auto_now_add=True)

    def __str__(self):
        return f'text: {self.text} sampled_date: {self.sampled_date}'


class Opinion(models.Model):
    opinions = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        db_column='review_id')
    text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    sampled_date = models.DateTimeField('date sampled')

    def __str__(self):
        return f'opinion: {self.text} - score: {self.score}'


class Endpoint(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class MLAlgorithm(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class MLAlgorithmStatus(models.Model):
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(
        MLAlgorithm,
        on_delete=models.CASCADE,
        related_name="status")


class MLRequest(models.Model):
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(
        MLAlgorithm,
        on_delete=models.CASCADE)
