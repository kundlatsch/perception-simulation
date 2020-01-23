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

from structures import OrderedList

class PerceptionRevision:
    def __init__(self, agent):
        self.plans = parse_agent_plans(agent)
        self.actions = get_perceptions_actions(self.plans)
        
        self.context_bodies, self.context_args = get_agent_context(self.plans)
        self.context = self.context_bodies.union(self.context_args)

        self.illusion_OL = OrderedList()
        self.hallucination_OL = OrderedList()

    def __classify_perception(self, perception: str) -> int:
        """Classify if a perception is an illusion or hallucination.

        Args:
            perception: The perception string in the format p(x).
        Returns:
            An int, 1 for illusion class 1, 2 for illusion class 2 and 3 for hallucination.
        """
        body, arg = parse_perception(perception)
                
        if body in self.context and arg in self.context:
            return 'valid'
        
        if body in self.context:
            return 'illusion1'
        
        if arg in self.context:
            return 'illusion2'

        return 'hallucination'
    
    def avaliation_block(self, perception):
        pass