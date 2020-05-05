Secret santa: assign  a person for each participant.
Condition:
1. participants cannot be assigned to themselves
2. participants cannot be assigned to their partners

The structure of the input is a dictionary of {participant: their partner}

input = {
    "a@santa.com": "a1@outsider.com",
    "b@santa.com": "b1@outsider.com",
    "c@santa.com": "c1@outsider.com",
    "d@santa.com": "d1@outsider.com",
    "a1@outsider.com": "a@santa.com",
    "b1@outsider.com": "b@santa.com",
    "c1@outsider.com": "c@santa.com",
    "d1@outsider.com": "d@santa.com",
}

The structure of the output is a list of (participant, person they have to get the gift to)
output = [
('a@santa.com', 'b1@outsider.com'), 
('b@santa.com', 'd1@outsider.com'), 
('c@santa.com', 'a1@outsider.com'), 
('d@santa.com', 'c1@outsider.com'), 
('a1@outsider.com', 'd@santa.com'), 
('b1@outsider.com', 'c@santa.com'), 
('c1@outsider.com', 'a@santa.com'), 
('d1@outsider.com', 'b@santa.com')
]