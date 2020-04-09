from simulation import Simulation
from generator.perceptions import PerceptionGenerator

import click

generate_help_str = "Generate perceptions. Require 2 args: total number of perceptions and percentage of invalid perceptions, in this order. Exemple: --generate 500 80"
reload_help_str = "Reload or not current agent file. If true, will overwrite agent.txt with base-agent.txt file, removing plans created by the autoplanner."
reasoning_time_help_str = (
    "Define agent's avarege reasoning time. Default is 1, as proposed in the paper."
)
planning_time_help_str = (
    "Define agent's autoplanner avarege time. Default is 32, but any value can be used."
)


@click.command()
@click.option("--generate", "-G", default=0, nargs=2, help=generate_help_str)
@click.option("--reload-agent/--not-reload", "-R/", default=True, help=reload_help_str)
@click.option("--reasoning-time", default=1, help=reasoning_time_help_str)
@click.option("--planning-time", default=32, help=planning_time_help_str)
def run(generate, reload_agent, reasoning_time, planning_time):

    if generate:
        g = PerceptionGenerator(*generate)
        g.generate()

    s = Simulation(reasoning_time, planning_time, reload_agent=reload_agent)
    s.start()


if __name__ == "__main__":
    run()
