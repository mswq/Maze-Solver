from bfs import QueueFrontier

class StackFrontier(QueueFrontier):
    def __init__(self):
        super().__init__()

    def remove(self):
        if self.is_empty():
            raise Exception("frontier is empty")   
        return self.frontier.pop()
    
    def top(self):
        return self.frontier[-1]