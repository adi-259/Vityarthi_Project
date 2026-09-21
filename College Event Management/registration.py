def register(participants, student):
    if student not in participants:
        participants.append(student)
        return True
    return False

def cancel(participants, student):
    if student in participants:
        participants.remove(student)
        return True
    return False
