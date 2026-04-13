class Lesson:
    def __init__(
        self, subject, tutor, room, type, teams_meeting_url, time_from, time_to
    ) -> None:
        self.subject = subject
        self.tutor = tutor
        self.room = room
        self.type = type
        self.teams_meeting_url = teams_meeting_url
        self.time_from = time_from
        self.time_to = time_to
