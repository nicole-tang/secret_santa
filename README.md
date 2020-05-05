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