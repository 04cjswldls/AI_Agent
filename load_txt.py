from models import ScheduleInfo, TravelTime
from mock_db import get_store

def read_schedule():
    data = []
    with open ("schedules.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(" / ")

            name, date, start_time, end_time, place, importance = parts
            schedule = ScheduleInfo(
                name=name,
                schedule_date=date,
                start_time=start_time,
                end_time=end_time,
                place=place,
                importance=importance
            )

            get_store()["schedules"].append(schedule)

    return []

def read_distance():
    data = []
    with open ("distance.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(" / ")

            place1, place2, required_time = parts
            travel_time = TravelTime(
                place1=place1,
                place2=place2,
                required_time=required_time
            )

            get_store()["travel_times"].append(travel_time)

    return []
