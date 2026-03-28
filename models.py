from pydantic import BaseModel, Field


class ScheduleInfo(BaseModel):
    name: str = Field(description="스케줄의 이름")
    schedule_date: str = Field(description="스케줄의 날짜(YYYY-MM-DD 형식)")
    start_time: str = Field(description="스케줄이 시작하는 시간(HH:MM 형식)")
    end_time: str = Field(description="스케줄이 끝나는 시간(HH:MM 형식)")
    place: str = Field(description="스케줄이 있는 장소")
    importance: int = Field(description="스케줄의 중요도(1 | 2 | 3)")


class TravelTime(BaseModel):
    place1: str = Field(description="첫번째 장소")
    place2: str = Field(description="두번째 장소")
    required_time: int = Field(description="두 장소 사이를 이동하는 데 걸리는 시간(minute)")