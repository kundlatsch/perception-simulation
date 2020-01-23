REASONING_CYCLE_TIME = 1
AUTO_PLANNING_TIME = 4

from pr_system import PerceptionRevision
from structures import OrderedList

def main():
    # a = PerceptionRevision("agent.txt")
    a = OrderedList()
    a.insert('co')
    a.insert('co')
    a.insert('co')
    a.insert('cac')
    print(a.get_top())
    

if __name__ == "__main__":
    main()
