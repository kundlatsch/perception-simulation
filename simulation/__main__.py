REASONING_CYCLE_TIME = 1
AUTO_PLANNING_TIME = 4

from pr_system import PerceptionRevision
from structures import OrderedList
from simulation import Simulation
from random import choice
from generator.perceptions import PerceptionGenerator


def main():
    # a = PerceptionRevision("agent.txt", 10, 1)
    # a.process_perceptions(["ball(red)", "uai(so)"])

    # b = PerceptionGenerator(100, 95)
    # b.generate()

    c = Simulation(1, 32, reload_agent=False)
    c.start()

if __name__ == "__main__":
    main()
