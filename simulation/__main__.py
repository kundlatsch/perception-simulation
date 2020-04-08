REASONING_CYCLE_TIME = 1
AUTO_PLANNING_TIME = 4

from pr_system import PerceptionRevision
from structures import OrderedList
from random import choice
from generator.perceptions import PerceptionGenerator


def main():
    # a = PerceptionRevision("agent.txt", 10, 1)
    # a.process_perceptions(["ball(red)", "uai"])
    b = PerceptionGenerator(100, 90)
    b.generate()


if __name__ == "__main__":
    main()
