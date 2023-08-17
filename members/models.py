from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #100 level courses
    taken_EECS110 = models.BooleanField(blank=True, default=False)
    taken_EECS183 = models.BooleanField(blank=True, default=False)
    #200 level courses
    taken_EECS200 = models.BooleanField(blank=True, default=False)
    taken_EECS201 = models.BooleanField(blank=True, default=False)
    taken_EECS203 = models.BooleanField(blank=True, default=False)
    taken_EECS215 = models.BooleanField(blank=True, default=False)
    taken_EECS216 = models.BooleanField(blank=True, default=False)
    taken_EECS230 = models.BooleanField(blank=True, default=False)
    taken_EECS270 = models.BooleanField(blank=True, default=False)
    taken_EECS280 = models.BooleanField(blank=True, default=False)
    taken_EECS281 = models.BooleanField(blank=True, default=False)
    taken_EECS298 = models.BooleanField(blank=True, default=False)
    #300 level courses
    taken_EECS300 = models.BooleanField(blank=True, default=False)
    taken_EECS301 = models.BooleanField(blank=True, default=False)
    taken_EECS311 = models.BooleanField(blank=True, default=False)
    taken_EECS312 = models.BooleanField(blank=True, default=False)
    taken_EECS314 = models.BooleanField(blank=True, default=False)
    taken_EECS320 = models.BooleanField(blank=True, default=False)
    taken_EECS330 = models.BooleanField(blank=True, default=False)
    taken_EECS334 = models.BooleanField(blank=True, default=False)
    taken_EECS351 = models.BooleanField(blank=True, default=False)
    taken_EECS370 = models.BooleanField(blank=True, default=False)
    taken_EECS373 = models.BooleanField(blank=True, default=False)
    taken_EECS376 = models.BooleanField(blank=True, default=False)
    taken_EECS388 = models.BooleanField(blank=True, default=False)
    taken_EECS399 = models.BooleanField(blank=True, default=False)
    #400 level courses
    taken_EECS402 = models.BooleanField(blank=True, default=False)
    taken_EECS409 = models.BooleanField(blank=True, default=False)

    taken_EECS411 = models.BooleanField(blank=True, default=False)
    taken_EECS413 = models.BooleanField(blank=True, default=False)
    taken_EECS414 = models.BooleanField(blank=True, default=False)

    taken_EECS421 = models.BooleanField(blank=True, default=False)
    taken_EECS423 = models.BooleanField(blank=True, default=False)
    taken_EECS427 = models.BooleanField(blank=True, default=False)
    taken_EECS428 = models.BooleanField(blank=True, default=False)

    taken_EECS434 = models.BooleanField(blank=True, default=False)
    taken_EECS435 = models.BooleanField(blank=True, default=False)

    taken_EECS441 = models.BooleanField(blank=True, default=False)
    taken_EECS442 = models.BooleanField(blank=True, default=False)
    taken_EECS443 = models.BooleanField(blank=True, default=False)
    taken_EECS445 = models.BooleanField(blank=True, default=False)

    taken_EECS452 = models.BooleanField(blank=True, default=False)
    taken_EECS453 = models.BooleanField(blank=True, default=False)
    taken_EECS455 = models.BooleanField(blank=True, default=False)
    taken_EECS458 = models.BooleanField(blank=True, default=False)

    taken_EECS460 = models.BooleanField(blank=True, default=False)
    taken_EECS461 = models.BooleanField(blank=True, default=False)
    taken_EECS463 = models.BooleanField(blank=True, default=False)
    taken_EECS464 = models.BooleanField(blank=True, default=False)
    taken_EECS465 = models.BooleanField(blank=True, default=False)
    taken_EECS467 = models.BooleanField(blank=True, default=False)

    taken_EECS470 = models.BooleanField(blank=True, default=False)
    taken_EECS471 = models.BooleanField(blank=True, default=False)
    taken_EECS473 = models.BooleanField(blank=True, default=False)
    taken_EECS475 = models.BooleanField(blank=True, default=False)
    taken_EECS477 = models.BooleanField(blank=True, default=False)

    taken_EECS481 = models.BooleanField(blank=True, default=False)
    taken_EECS482 = models.BooleanField(blank=True, default=False)
    taken_EECS483 = models.BooleanField(blank=True, default=False)
    taken_EECS484 = models.BooleanField(blank=True, default=False)
    taken_EECS485 = models.BooleanField(blank=True, default=False)
    taken_EECS487 = models.BooleanField(blank=True, default=False)
    taken_EECS489 = models.BooleanField(blank=True, default=False)

    taken_EECS490 = models.BooleanField(blank=True, default=False)
    taken_EECS491 = models.BooleanField(blank=True, default=False)
    taken_EECS492 = models.BooleanField(blank=True, default=False)
    taken_EECS494 = models.BooleanField(blank=True, default=False)
    taken_EECS495 = models.BooleanField(blank=True, default=False)
    taken_EECS496 = models.BooleanField(blank=True, default=False)
    taken_EECS497 = models.BooleanField(blank=True, default=False)
    taken_EECS498 = models.BooleanField(blank=True, default=False)
    taken_EECS499 = models.BooleanField(blank=True, default=False)

    #500 level courses
    taken_EECS501 = models.BooleanField(blank=True, default=False)
    taken_EECS507 = models.BooleanField(blank=True, default=False)

    taken_EECS517 = models.BooleanField(blank=True, default=False)
    taken_EECS520 = models.BooleanField(blank=True, default=False)
    taken_EECS523 = models.BooleanField(blank=True, default=False)

    taken_EECS530 = models.BooleanField(blank=True, default=False)

    taken_EECS540 = models.BooleanField(blank=True, default=False)
    taken_EECS542 = models.BooleanField(blank=True, default=False)
    taken_EECS544 = models.BooleanField(blank=True, default=False)

    taken_EECS551 = models.BooleanField(blank=True, default=False)
    taken_EECS553 = models.BooleanField(blank=True, default=False)
    taken_EECS554 = models.BooleanField(blank=True, default=False)
    taken_EECS558 = models.BooleanField(blank=True, default=False)

    taken_EECS560 = models.BooleanField(blank=True, default=False)
    taken_EECS561 = models.BooleanField(blank=True, default=False)
    taken_EECS563 = models.BooleanField(blank=True, default=False)
    taken_EECS564 = models.BooleanField(blank=True, default=False)

    taken_EECS574 = models.BooleanField(blank=True, default=False)
    taken_EECS575 = models.BooleanField(blank=True, default=False)

    taken_EECS582 = models.BooleanField(blank=True, default=False)
    taken_EECS583 = models.BooleanField(blank=True, default=False)
    taken_EECS584 = models.BooleanField(blank=True, default=False)
    taken_EECS587 = models.BooleanField(blank=True, default=False)

    taken_EECS595 = models.BooleanField(blank=True, default=False)
    taken_EECS598 = models.BooleanField(blank=True, default=False)
    taken_EECS599 = models.BooleanField(blank=True, default=False)

    taken_EECS628 = models.BooleanField(blank=True, default=False)

class SearchRequest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="NONE")
    user_request = models.TextField(blank=False, null=True, default='NONE')
