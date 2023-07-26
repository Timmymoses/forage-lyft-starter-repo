from unittest import TestCase

from engine.Engine import Engine
from engine.sternman_engine import SternmanEngine


class SternmnEngineTest(TestCase):

    def test_capulet(self):
        engine: Engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())
