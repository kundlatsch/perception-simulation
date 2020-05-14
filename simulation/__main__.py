from simulation import Simulation
from analyzer import get_mean
from generator.perceptions import PerceptionGenerator
import strings
from time import time
from pathlib import Path
import pandas as pd

import click
from proggy import BarInfo
from proggy.tty import TTYProgressBar


@click.command()
@click.option("--generate", "-G", default=0, nargs=2, help=strings.generate_help)
@click.option(
    "--reload-agent/--not-reload", "-R/", default=True, help=strings.reload_help
)
@click.option("--reasoning-time", default=1.0, help=strings.reasoning_time_help)
@click.option("--planning-time", default=32.0, help=strings.planning_time_help)
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

    start_time = time()
    vtimes = []
    pps = []
    pcs = []

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
            print(plans_created)
            vtimes.append(vtime)
            pps.append(perceptions_processed)
            pcs.append(plans_created)

            p.progress += 1

    final_time = time()
    total_time = final_time - start_time
    total_time = "{:.2f}".format(total_time)
    print(
        f"------------\nFinished Simulation\nTime elapsed: {total_time}s\n------------"
    )

    d = {"vtime": vtimes, "perceptions_processed": pps, "plans_created": pcs}

    print(d)
    df = pd.DataFrame(data=d)
    print(df)
    p = Path('/results')
    factors = f"valid{generate[1]}reasoning{reasoning_time}planning{planning_time}perceptions{perceptions_per_cycle}"
    df.to_csv(f'./results/{factors}.csv', index=False)
    print(Path(p))


if __name__ == "__main__":
    run()
