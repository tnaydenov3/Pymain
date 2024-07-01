from solutions.interface.console import ConsoleLogger
from solutions.testing.counter import TestsCounter
from solutions.testing.testcase import TestCase


class TestPack:

    __slots__ = ("_testcases", "_passed", "_failed", "_error")

    def __init__(self) -> None:
        self._testcases: list[TestCase] = []
        self._counter = TestsCounter()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} (total_tests: {len(self._testcases)})>"

    def __str__(self) -> str:
        title = f"{self.__class__.__name__} (total_tests: {len(self._testcases)})"
        tests_list = "\n".join([str(object=testcase) for testcase in self._testcases])
        tail = f"Total ran: {self._counter.total}"

        return f"{title}\n{tests_list}\n{tail}"

    @property
    def testcases(self) -> list[TestCase]:
        return self._testcases

    def add_testcase(self, testcase: TestCase) -> None:
        self._testcases.append(testcase)

    def run(self) -> None:
        for testcase in self._testcases:
            testcase.run()
            self._counter.increment_counter(result=testcase.result)
            ConsoleLogger.log_test_result(testcase=testcase)

        ConsoleLogger.log_testpack_result(counter=self._counter)
