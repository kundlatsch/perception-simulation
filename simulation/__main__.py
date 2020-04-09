from simulation import Simulation
from generator.perceptions import PerceptionGenerator
import strings

import click


@click.command()
@click.option("--generate", "-G", default=0, nargs=2, help=strings.generate_help)
@click.option("--reload/--not-reload", "-R/", default=True, help=strings.reload_help)
@click.option("--reasoning-time", default=1, help=strings.reasoning_time_help)
@click.option("--planning-time", default=32, help=strings.planning_time_help)
def run(generate, reload_agent, reasoning_time, planning_time):

    if generate:
        g = PerceptionGenerator(*generate)
        g.generate()

    s = Simulation(reasoning_time, planning_time, reload_agent=reload_agent)
    s.start()


if __name__ == "__main__":
    run()
