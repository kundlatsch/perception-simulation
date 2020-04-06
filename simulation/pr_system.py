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

from structures import AvaliationBlock


class PerceptionRevision:
    def __init__(self, agent):
        self.plans = parse_agent_plans(agent)
        self.actions = get_perceptions_actions(self.plans)

        self.context_bodies, self.context_args = get_agent_context(self.plans)
        self.context = self.context_bodies.union(self.context_args)

        self.illusion1_AB = AvaliationBlock()
        self.illusion2_AB = AvaliationBlock()
        self.hallucination_AB = AvaliationBlock()

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

    MAP_PERCEPTION_TO_AB = {
        'illusion1': self.illusion1_AB,
        'illusion2': self.illusion2_AB,
        'hallucination': self.hallucination_AB,
    }

    def process_perceptions(perceptions):
        
        have_anomaly = False
        
        # Add each perception to it's respective avaliation block
        for perception in perceptions:
            perception_type = __classify_perception(perception)

            if perception_type in MAP_PERCEPTION_TO_AB:
                MAP_PERCEPTION_TO_AB[perception_type].push(perception)
                have_anomaly = True
        
        if not have_anomaly:
            return

