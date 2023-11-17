import simpy
import random

class Anchor:
    def __init__(self, env, name):
        self.env = env
        self.name = name
        self.available = True
        self.missed_requests = 0
        self.total_requests = 0
        self.resource = simpy.Resource(env, capacity=1)
        self.env.process(self.listen())

    def listen(self):
        while True:
            yield self.env.timeout(1)  # Adjust timeout based on your simulation
            # Simulating anchor availability randomly
            self.available = random.choice([True, False])
            print(f"Anchor {self.name} is available: {self.available}")

class Tag:
    def __init__(self, env, name, anchors):
        self.env = env
        self.name = name
        self.anchors = anchors
        self.env.process(self.send_request())

    def send_request(self):
        while True:
            yield self.env.timeout(3)  # Adjust timeout based on your simulation
            selected_anchor = random.choice(self.anchors)
            with selected_anchor.resource.request() as req:
                yield req
                selected_anchor.total_requests += 1
                if selected_anchor.available:
                    print(f"Tag {self.name} requesting ranging from Anchor {selected_anchor.name}")
                    # Ranging routine would go here
                else:
                    selected_anchor.missed_requests += 1
                    print(f"Tag {self.name} couldn't range with Anchor {selected_anchor.name} (unavailable)")

def run_simulation(env, num_anchors, num_tags):
    anchors = [Anchor(env, f"Anchor {i}") for i in range(num_anchors)]
    tags = [Tag(env, f"Tag {i}", anchors) for i in range(num_tags)]

    env.run(until=20)  # Adjust simulation time as needed
    
    total_missed_requests = sum(anchor.missed_requests for anchor in anchors)
    total_requests = sum(anchor.total_requests for anchor in anchors)
    if total_requests > 0:
        missed_percentage = (total_missed_requests / total_requests) * 100
        print(f"Percentage of missed range requests: {missed_percentage:.2f}%")

if __name__ == "__main__":
    env = simpy.Environment()
    num_anchors = 3
    num_tags = 5
    run_simulation(env, num_anchors, num_tags)
