from simulation import Simulation
from analyzer import get_mean
from generator.perceptions import PerceptionGenerator
import strings
from time import time

import click


@click.command()
@click.option("--generate", "-G", default=0, nargs=2, help=strings.generate_help)
@click.option("--reload-agent/--not-reload", "-R/", default=True, help=strings.reload_help)
@click.option("--reasoning-time", default=1, help=strings.reasoning_time_help)
@click.option("--planning-time", default=32, help=strings.planning_time_help)
@click.option("--perceptions-per-cycle", "-C", default=1)
@click.option("--iterations", "-I", default=1)
def run(generate, reload_agent, reasoning_time, planning_time, perceptions_per_cycle, iterations):

    open('results.txt', 'w').close()
    start_time = time()

    for i in range(iterations):
        print(f'-------------\nSIMULATION {i}\n-------------')

        if generate:
            g = PerceptionGenerator(*generate)
            g.generate()

        s = Simulation(reasoning_time, planning_time, perceptions_per_cycle, reload_agent=reload_agent)
        vtime, perceptions_processed, plans_created = s.start()

        results = open('results.txt', 'a')
        results.write(f'{vtime},{perceptions_processed},{plans_created};')
        results.close()

    final_time = time()
    total_time = final_time - start_time
    print(f'------------\nFinished Simulations\nTime elapsed: {total_time}\n------------')
    print('Results:')
    get_mean()

if __name__ == "__main__":
    run()
