from dotenv import load_dotenv

from langchain_openai import OpenAI  # Completion 모델
from langchain_openai import ChatOpenAI  # Chat 모델 (QA모델)
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

llm2 = ChatOpenAI(model="gpt-3.5-turbo")

prompt = [
    SystemMessage(content="당신은 모든것을 3줄로 요약하는 직업을 가졌습니다."),
    HumanMessage(content="""
애플이 올해 가을 출시 예정인 아이폰17 프로 라인업에 고성능 이미지 센서, 향상된 배터리 설계, AI 최적화를 위한 사양 업그레이드를 대거 적용한다.

4일(현지시간) 복수의 미국IT전문매체들에 따르면 애플은 아이폰17 프로 및 프로 맥스에 자사 설계의 커스텀 이미지 센서를 도입하고, 48MP 망원 카메라 및 24MP 전면 카메라 등 카메라 전면 개편을 시도한다고 전했다. AI 처리 성능을 강화하기 위해 최대 12GB RAM을 탑재하고, 발열 제어를 위한 베이퍼 챔버와 그래파이트 냉각시트를 적용하는 등 AI 하드웨어 플랫폼으로서의 완성도를 높이고 있다는 설명이다.
    """)
]
result = llm2.invoke(prompt)
print(result.content)

llm3 = ChatOpenAI(model="gpt-3.5-turbo")

prompt = [
    SystemMessage(content="한국어를 영어로 번역하는 것을 직업으로 가지고 있습니다."),
    HumanMessage(content="""
    애플이 올해 가을 출시 예정인 아이폰17 프로 라인업에 고성능 이미지 센서
    """)
]

result = llm3.invoke(prompt)
print(result.content)

llm4 = ChatOpenAI(model="gpt-3.5-turbo")

prompt = [
    SystemMessage(content="다음 수신자에게 주제의 내용에 해당하는 회사의 공식 이메일 형태로 작성해주세요.\n\n수신자: {recipient}\n\n주제: {topic}. 그리고 100자 미만으로"),
    HumanMessage(content='recipient": "CEO", "topic": "회사의 중요 인재인 개발자를 해고시킨 인사팀장 해고')
]

result = llm4.invoke(prompt)
print(result.content)
