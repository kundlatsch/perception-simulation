from typing import List, Tuple


def parse_agent_plans(agent: str) -> List[str]:
    """Parse agent file to get it's plans.

    Args:
        agent: Agent file name. Must be on the root or contain the path.
    Returns:
        A list of the agent's plans.
    """
    with open(agent) as f:
        plans = f.read().splitlines()

    return plans


def get_perceptions_actions(plans: List[str]) -> List[str]:
    """Get all actions from given plans.

    This implementations parse an specific kind of plans, i.e. different
    agent oriented programming languages need different implementations of this
    function.

    Args:
        plans: List of plans. Can be get from parse_agent_plans().
    Returns:
        A list of all actions used in the given plans.
    """
    actions = set()
    for plan in plans:

        plan_body = plan.split("->")[1]
        plan_actions = plan_body.split(";")

        for action in plan_actions:
            action = action.replace(" ", "")
            actions.add(action)

    actions.remove("")
    return actions


def get_agent_context(plans: List[str]) -> Tuple[List[str], List[str]]:
    """Get the agent context (the domain of the perception function)
    
    Args:
        plans: List of plans. Can be get from parse_agent_plans().
    Returns:
        The agent's context, a 2-tuple of bodies and args.
    """
    bodies = set()
    args = set()
    for plan in plans:
        plan_head = plan.split("->")[0].replace(" ", "")

        body, arg = parse_perception(plan_head)

        bodies.add(body)
        args.add(arg)

    return (bodies, args)


def parse_perception(perception: str) -> Tuple[str, str]:
    """Get the perception body and arg.

    Args:
        perception: Perception or plan head in the format p(x).
    Returns:
        A 2-tuple of body and arg.
    """
    body, arg = perception.split("(")
    arg = arg.replace(")", "")

    return (body, arg)
