from langchain_core.tools import tool
from models import ScheduleInfo
from mock_db import get_store
from datetime import datetime


@tool
def save_schedule(
    name: str,
    schedule_date: str,
    start_time: str,
    end_time: str,
    place: str,
    importance: int
) -> ScheduleInfo:
    """
    새로운 스케줄을 저장합니다.

    Args:
        name: 스케줄의 이름
        schedule_date: 스케줄의 날짜
        start_time: 스케줄의 시작시간
        end_time: 스케줄의 종료시간
        place: 스케줄 장소
        importance: 스케줄의 중요도

    Return:
        ScheduleInfo: 스케줄의 정보
    """

    schedule = ScheduleInfo(
        name=name,
        schedule_date=schedule_date,
        start_time=start_time,
        end_time=end_time,
        place=place,
        importance=importance
    )

    store = get_store()
    store["schedules"].append(schedule)

    return schedule


@tool
def adjust_schedule(
    name: str,
    schedule_date: str,
    start_time: str,
    end_time: str,
    place: str,
    importance: int
) -> ScheduleInfo:
    """
    기존 스케줄을 지우고 수정된 스케줄을 저장합니다

    Args:
        name: 스케줄의 이름
        schedule_date: 스케줄의 날짜
        start_time: 스케줄의 시작시간
        end_time: 스케줄의 종료시간
        place: 스케줄 장소
        importance: 스케줄의 중요도

    Return:
        ScheduleInfo: 스케줄의 정보
    """

    schedule = ScheduleInfo(
        name=name,
        schedule_date=schedule_date,
        start_time=start_time,
        end_time=end_time,
        place=place,
        importance=importance
    )

    schedule_name = name
    store = get_store()
    store["schedules"] = [i for i in store["schedules"] if i.name != schedule_name]

    store["schedules"].append(schedule)

    return schedule


@tool
def remove_schedule(
    schedule_date: str,
    start_time: str
) -> list:
    """
    기존 스케줄을 지웁니다.

    Args:
        schedule_date: 삭제할 스케줄의 날짜
        start_time: 삭제할스케줄의 시작시간

    Rutern:
        삭제되지 않은 다른 스케줄
    """

    store = get_store()
    store["schedules"] = [i for i in store["schedules"] if i.date != schedule_date or i.start_time != start_time]

    return store["schedules"]


@tool
def get_user_schedule(
    schedule_date: str,
    start_time: str,
) -> list:
    """
    저장된 사용자의 스케줄들 중 새로운 스케줄과 같은 날의 스케줄을 조회합니다.
    새로운 스케줄 이전 스케줄과 이후 스케줄을 반환합니다.
    모델이 새로운 스케줄을 저장하기 이전에 호출하여 사용자의 스케줄을 바로 저장할 수 있는지 파악합니다.

    Args:
        schedule_date: 새로운 스케줄의 날짜
        start_time: 새로운 스케줄의 시작시간

    Return:
        새로운 스케줄 이전 스케줄과 이후 스케줄
        만약 새로운 스케줄과 같은 날에 기존 스케줄이 없다면 빈 리스트
    """

    store = get_store()
    same_date = [i for i in store["schedules"] if i.schedule_date == schedule_date]
    
    sorted_schedule = sorted(same_date, key=lambda x: datetime.strptime(x.start_time, "%H:%M").time())

    if sorted_schedule.count == 0:
        result = []
    elif sorted_schedule.count == 1:
        result = sorted_schedule
    else:
        for i in range(len(sorted_schedule)):
            if start_time > sorted_schedule[i].start_time:
                result = [sorted_schedule[i], sorted_schedule[i+1]]
                break
            else:
                continue
        
    return result


@tool
def surch_distance(
    place1: str,
    place2: str
) -> int:
    """
    두 개의 장소를 이동하는 데 걸리는 시간을 조회합니다.

    Args:
        place1: 첫번쨰 장소
        place2: 두번쨰 장소

    Return:
        두 장소를 이동하는 데 걸리는 시간(분)
    """

    store = get_store()
    travel_time = [i for i in store["travel_times"] if (i.place1 == place1 and i.place2 == place2) or (i.place1 == place2 and i.place2 == place1)]

    return travel_time[0].required_time