from simulation import Simulation
from analyzer import get_mean
from generator.perceptions import PerceptionGenerator
import strings
from time import time

import click
from proggy import BarInfo
from proggy.tty import TTYProgressBar


@click.command()
@click.option("--generate", "-G", default=0, nargs=2, help=strings.generate_help)
@click.option(
    "--reload-agent/--not-reload", "-R/", default=True, help=strings.reload_help
)
@click.option("--reasoning-time", default=1, help=strings.reasoning_time_help)
@click.option("--planning-time", default=32, help=strings.planning_time_help)
@click.option(
    "--perceptions-per-cycle", "-C", default=1, help=strings.perceptions_per_cycle_help
)
@click.option("--iterations", "-I", default=1, help=strings.iterations_help)
def run(
    generate,
    reload_agent,
    reasoning_time,
    planning_time,
    perceptions_per_cycle,
    iterations,
):

    open("results.txt", "w").close()
    start_time = time()

    with TTYProgressBar(BarInfo(size=30, total=iterations)) as p:

        for i in range(iterations):
            # print(f"-------------\nSIMULATION {i}\n-------------")

            if generate:
                g = PerceptionGenerator(*generate, perceptions_per_cycle)
                g.generate()

            s = Simulation(
                reasoning_time,
                planning_time,
                perceptions_per_cycle,
                reload_agent=reload_agent,
            )
            vtime, perceptions_processed, plans_created = s.start()
            perceptions_processed = perceptions_processed / perceptions_per_cycle
            
            results = open("results.txt", "a")
            results.write(f"{vtime},{perceptions_processed},{plans_created};")
            results.close()
            p.progress += 1


    final_time = time()
    total_time = final_time - start_time
    total_time = "{:.2f}".format(total_time)
    print(
        f"------------\nFinished Simulation\nTime elapsed: {total_time}s\n------------"
    )
    print("Results:")
    get_mean()


if __name__ == "__main__":
    run()
