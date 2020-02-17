from django.test import TestCase
from .models import GuessNumbers

class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='monkey', text='1등만세!')
        g.generate()
        print(g.update_date)
        print(g.lottos)
        self.assertTrue(len(g.lottos) > 20) 
        #성공실패 테스트 루틴은 assert 메소드를 사용한다.

