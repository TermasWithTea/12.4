import unittest
import logging
from rt_with_exceptions import Runner






class RunnerTest(unittest.TestCase):

    is_frozen = False


    def test_walk(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            runner = Runner('test-walk')
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
        except IndexError as err:
            logging.warning('неверная скорость для Runner')



    def test_run(self):
        try:
            logging.info('"test+_run" выполнен успешно')
            runner = Runner('test_walk')
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except NameError as err:
            logging.warning("Неверный тип данных для объекта Runner")



    def test_challenge(self):
        challenger = Runner('test1')
        challenge2 = Runner('test2')

        for _ in range(10):
            challenger.run()
            challenge2.walk()
        self.assertNotEqual(challenger.distance, challenge2.distance)


if __name__ == '__main__':
    unittest.main()
    logging.basicConfig(level = logging.INFO, filemode = 'w', filename = 'runner_test.log',
                        encoding='utf-8',
                        format='%(asktime)s | %(levelname)s |%(massage)s')