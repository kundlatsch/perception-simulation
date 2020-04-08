from pr_system import PerceptionRevision
from shutil import copyfile

class Simulation():

    def __init__(self, reasoning_at, autoplanning_at, debug=0):
        self.perception_queue = []
        
        perceptions = open('perceptions.txt', 'r')

        content = perceptions.readlines()        
        for c in content:
            self.perception_queue.append(c.replace('\n', ''))

        perceptions.close()
        
        # A copy of the base agent is created because the autoplanner
        # will change the file.
        copyfile('base-agent.txt', 'agent.txt')

        self.model = PerceptionRevision("agent.txt", reasoning_at, autoplanning_at)
    
    def start(self):

        for i in range(len(self.perception_queue)):
            self.model.process_perceptions([self.perception_queue.pop(0)])