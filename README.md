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

