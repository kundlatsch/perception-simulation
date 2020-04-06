"""Perception Revision System implementation.

This module implements all the formal model described in the
illusion and hallucination paper. It can be attached to any
cognitive architecture to reason about the perceptions coming
from the environment.
"""

from utils import (
    parse_agent_plans,
    get_perceptions_actions,
    get_agent_context,
    parse_perception,
)

from structures import AvaliationBlock, Autoplanner

from random import choice


class PerceptionRevision:
    def __init__(self, agent, reasoning_at, autoplanning_at):
        self.plans = parse_agent_plans(agent)
        self.actions = get_perceptions_actions(self.plans)
        # print(self.plans)
        # print(self.actions)
        

        self.context_bodies, self.context_args = get_agent_context(self.plans)
        self.context = self.context_bodies.union(self.context_args)
        # print(self.context_bodies)
        # print(self.context_args)
        # print(self.context)


        self.illusion1_AB = AvaliationBlock(reasoning_at, autoplanning_at)
        self.illusion2_AB = AvaliationBlock(reasoning_at, autoplanning_at)
        self.hallucination_AB = AvaliationBlock(reasoning_at, autoplanning_at)

        self.avaliation_blocks = (self.illusion1_AB, self.illusion2_AB, self.hallucination_AB)

        self.MAP_PERCEPTION_TO_AB = {
            'illusion1': self.illusion1_AB,
            'illusion2': self.illusion2_AB,
            'hallucination': self.hallucination_AB,
        }

        self.autoplanner = Autoplanner(self.actions)

    def __classify_perception(self, perception: str) -> str:
        """Classify if a perception is an illusion or hallucination.

        Args:
            perception: The perception string in the format p(x).
        Returns:
            An int, 1 for illusion class 1, 2 for illusion class 2 and 3 for hallucination.
        """
        body, arg = parse_perception(perception)

        if body in self.context and arg in self.context:
            return "valid"

        if body in self.context:
            return "illusion1"

        if arg in self.context:
            return "illusion2"

        return "hallucination"


    def process_perceptions(self, perceptions):
        
        have_anomaly = False
        # Add each perception to it's respective avaliation block
        for perception in perceptions:
            perception_type = self.__classify_perception(perception)

            if perception_type in self.MAP_PERCEPTION_TO_AB:
                self.MAP_PERCEPTION_TO_AB[perception_type].list.push(perception)
                have_anomaly = True
        
        if not have_anomaly:
            return False

        vtime = 0
        keep_planning = True
        
        while keep_planning:
            avaliation_block = choice(self.avaliation_blocks)
            print(avaliation_block)
            keep_planning = False
        



