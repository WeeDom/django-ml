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


class ABTest(models.Model):
    '''
        The ABTest will keep information about A/B tests.
        Attributes:
            title: The title of test.
            created_by: The name of creator.
            created_at: The date of test creation.
            ended_at: The date of test stop.
            summary: The description with test summary,
                created at test stop.
            parent_mlalgorithm_1: The reference to the
                first corresponding MLAlgorithm.
            parent_mlalgorithm_2: The reference to the
                second corresponding MLAlgorithm.
    '''
    title = models.CharField(max_length=10000)
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    summary = models.CharField(max_length=10000, blank=True, null=True)

    parent_mlalgorithm_1 = models.ForeignKey(
        MLAlgorithm,
        on_delete=models.CASCADE,
        related_name="parent_mlalgorithm_1"
     )
    parent_mlalgorithm_2 = models.ForeignKey(
        MLAlgorithm,
        on_delete=models.CASCADE,
        related_name="parent_mlalgorithm_2"
    )


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
