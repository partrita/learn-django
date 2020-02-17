from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model): #슈퍼클래스 models의 하위클래스 Model을 상속받는다.
    # 필요한 데이터 정의
    name = models.CharField(max_length = 24)
    lottos = models.CharField(max_length = 255, default = '[1, 2, 3, 4, 5, 6]')
    text = models.CharField(max_length = 255)
    num_lotto = models.IntegerField(default = 5)
    update_date = models.DateTimeField()

    # 메소드 정의
    def generate(self):
        self.lottos = ""
        origin = list(range(1,46)) #[1, 2, 3.....44, 45]
        for _ in range(0, self.num_lotto): # self.num_lotto 수만큼 반복해서 아래를 수행한다.
            guess = random.choices(origin, k=6)
            guess.sort()
            self.lottos += str(guess) + '\n'
        self.update_date = timezone.now()
        self.save() # 오브젝트를 db에 저장

    def __str__(self):
        return self.name