from .secret_santa import match_participants

participants = {
    "a@santa.com": "a1@outsider.com",
    "b@santa.com": "b1@outsider.com",
    "c@santa.com": "c1@outsider.com",
    "d@santa.com": "d1@outsider.com",
    "a1@outsider.com": "a@santa.com",
    "b1@outsider.com": "b@santa.com",
    "c1@outsider.com": "c@santa.com",
    "d1@outsider.com": "d@santa.com",
}


def test_assign():
    for i in range(len(participants) * len(participants)):
        outcome = match_participants(participants)
        print(outcome)
        for o in outcome:
            assert o[0] != o[1]
            assert o[1] != participants[o[0]]
