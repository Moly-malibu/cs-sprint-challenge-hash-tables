"""
tickets = [
    Ticket{ source: "PIT", destination: "ORD" },
    Ticket{ source: "XNA", destination: "CID" },
    Ticket{ source: "SFO", destination: "BHM" },
    Ticket{ source: "FLG", destination: "XNA" },
    Ticket{ source: "NONE", destination: "LAX" },
    Ticket{ source: "LAX", destination: "SFO" },
    Ticket{ source: "CID", destination: "SLC" },
    Ticket{ source: "ORD", destination: "NONE" },
    Ticket{ source: "SLC", destination: "PIT" },
    Ticket{ source: "BHM", destination: "FLG" }
]
"""
#  Hint:  You may not need all of these.  Remove the unused functions.

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route=[]
    flight = {}
    for ticket in tickets:
        flight[ticket.source] = ticket.destination
    occurence = flight["NONE"]
    route.append(occurence)
    while occurence != "NONE":
       occurence = flight[occurence]
       route.append(occurence) 
    return route
