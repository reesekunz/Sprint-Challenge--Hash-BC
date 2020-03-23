

#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


class Ticket:
    def __init__(self, source, destination):
        self.source = source  # source is starting airport
        self.destination = destination  # destination is next airport

# ticket for first flight has source of NONE
# ticket for final flight has a destination of NONE (no next airport)

# EXAMPLE
# tickets = [
#   Ticket{ source: "PIT", destination: "ORD" },
#   Ticket{ source: "XNA", destination: "CID" },
#   Ticket{ source: "SFO", destination: "BHM" },
#   Ticket{ source: "FLG", destination: "XNA" },
#   Ticket{ source: "NONE", destination: "LAX" },
#   Ticket{ source: "LAX", destination: "SFO" },
#   Ticket{ source: "CID", destination: "SLC" },
#   Ticket{ source: "ORD", destination: "NONE" },
#   Ticket{ source: "SLC", destination: "PIT" },
#   Ticket{ source: "BHM", destination: "FLG" }
# ]

# Your function should output an array of strings with the entire route of your trip. For the above example, it should look like this:
# ```
# ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]

# Hints
# * The crux of this problem requires us to 'link' tickets together to reconstruct the entire trip. For example, if we have a ticket `('SJC', 'BOS')` that has us flying from San Jose to Boston, then there exists another ticket where Boston is the starting location, `('BOS', 'JFK')`.
# * We can hash each ticket such that the starting location is the key and the destination is the value. Then, when constructing the entire route, the `i`th location in the route can be found by checking the hash table for the `i-1`th location.


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # insert is looking for (hash_table, key = x.source , value = x.destination)
    for x in tickets:
        hash_table_insert(hashtable, x.source, x.destination)

    # instantiate source as NONE. Setting source as key, so first trip will start from NONE.
    source = "NONE"

    # retrieve is looking for (hash_table, key), where key is the source.
    for x in range(0, (length-1)):
        route[x] = hash_table_retrieve(hashtable, source)
        print("route[x]", route[x])
        # set source to the next index value on list.
        source = route[x]
        print("source = ", source)
    # -1 cause dont return None at the end
    return route[:-1]
