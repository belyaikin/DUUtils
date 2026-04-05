from enum import Enum


class BachelorFaculties(Enum):
    SoftwareEngineering = "SE"
    Cybersecurity = "CS"
    SmartSecurityTechnologies = "SST"
    BigDataAnalysis = "BDA"
    MathematicalAndComputationalScience = "MCS"
    IndustrialInternetOfThings = "IoT"
    ElectronicEngineering = "EE"
    SmartTechnologies = "ST"
    ITManagement = "ITM"
    ITEnterpreneurship = "ITE"
    AIBusiness = "AIB"
    MediaTechnologies = "MT"
    DigitalJournalism = "DJ"
    DigitalPublicAdministration = "DPA"


class Lesson:
    def __init__(
        self, subject, tutor, room, type, teams_meeting_url, day_of_the_week, from_to
    ) -> None:
        self.subject = subject
        self.tutor = tutor
        self.room = room
        self.type = type
        self.teams_meeting_url = teams_meeting_url
        self.day_of_the_week = day_of_the_week
        self.from_to = from_to


class Schedule:
    def __init__(self, group, lessons: list[Lesson]):
        self.group = group
        self.lessons = lessons
