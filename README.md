# step 1. 구글 가입 및 Dialogflow 서비스 이용

  https://dialogflow.com/ 접속

  1. 접속 후 new agent 생성
  
  2. Entitie 생성
      - smart_plug라는 요소를 생성 한다.
      - 실습지원 프린터 : 실습지원 프린터, 실습지원프린터
      - 조명3 : 조명3
      
      - electric라는 요소를 생성 한다.
      - 전력 사용량 : 전력 사용량, 전력사용량
      
      - act라는 요소를 생성 한다.
      - 얼마 : 얼마, 얼마야, 알려줘
      - 설정 : 설정, 설정해줘
      
      - 기타 등등 개인이 추가 하고 싶은 부분 추가 할것
      
  3. Intents 생성
      - power_searching라는 Intents를 생성 한다.
      - User says 항목에 '실습지원 프린터 전력사용량이 얼마야' 라는 문장을 친후 엔터
      - action 의 제목을 get으로 지정한후 'smart_plug','electric','act'요소에 REQUIRED 항목을 체크한다.
      - 저장 후 Try it 항목에서 테스트 해본다.

# step 2. python을 이용한 webhook 서버 구현

- testing_server_2.py 에서 # 코드수정 # 부분 수정 하기
- 서버 구동하기


# step 3. ngrok을 이용한 로컬서버 연결

- ngrok 설치
- 터미널창에 ngrok http 5000 입력
- 터미널창에 나오는 포워딩된 주소를 복사
- Dialogflow에서 Fulfillment 항목을 들어간후 webhook 부분을 활성화 시킨 후 복사  한 주소를 입력 하고 뒤에 /webhook 을 추가한 후 저장
- Intents 항목에 power_searching을 들어간후 Fulfillment가 생긴 부분에 Use webhook 을 활성화 한 후 저장

# step 4. 최종 TEST

- Integrations 항목으로 이동
- 본인이 원하는 항목으로 테스트 진행

