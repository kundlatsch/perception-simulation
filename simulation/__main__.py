from simulation import Simulation
from generator.perceptions import PerceptionGenerator
import strings

import click


@click.command()
@click.option("--generate", "-G", default=0, nargs=2, help=strings.generate_help)
@click.option("--reload-agent/--not-reload", "-R/", default=True, help=strings.reload_help)
@click.option("--reasoning-time", default=1, help=strings.reasoning_time_help)
@click.option("--planning-time", default=32, help=strings.planning_time_help)
@click.option("--iterations", "-I", default=1)
def run(generate, reload_agent, reasoning_time, planning_time, iterations):

    for i in range(iterations):
        print(f'------------\nSIMULATION {i}\n------------')
        if generate:
            g = PerceptionGenerator(*generate)
            g.generate()

        s = Simulation(reasoning_time, planning_time, reload_agent=reload_agent)
        vtime, perceptions_processed, plans_created = s.start()

        results = open('results.txt', 'a')
        results.write(f'{vtime},{perceptions_processed},{plans_created};')
        results.close()



if __name__ == "__main__":
    run()
