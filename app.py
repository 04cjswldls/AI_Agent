from agents import get_schedule_manage_agent

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from load_txt import read_distance, read_schedule
from mock_db import get_store

load_dotenv()

model = ChatGroq(
    model = "openai/gpt-oss-20b"
)

read_schedule()
read_distance()

manager_agent = get_schedule_manage_agent(model)

result = manager_agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "2026년 4월 18일에 14시부터 16시까지 공주대 천안캠퍼스에서 프로젝트 회의를 해야 합니다. 중요도는 1로 설정해서 일정을 저장해주세요"
        }
    ]
})


print(result["messages"][-1].content)