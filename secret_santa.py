import random


def verify_conditions(participants, outcome):
    for o in outcome:
        participant = o[0]
        assignee = o[1]
        participant_partner = participants[participant]

        # participant does not get themselves nor their partners
        if participant == assignee or participant_partner == assignee:
            return False
    # all participants get an assignee that match with the conditions
    return True


def match_participants(participants):
    matches_conditions = False
    participant_emails = list(participants.keys())
    assignee_emails = participant_emails.copy()
    outcome = []

    while not matches_conditions:
        random.shuffle(assignee_emails)
        outcome = list(zip(participant_emails, assignee_emails))
        matches_conditions = verify_conditions(participants, outcome)
    return outcome
