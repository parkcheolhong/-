# Korean AI Translation Program - Task Scheduler
통역 프로그램 gpt ai 기능 + 작업 스케줄링

## 기능 (Features)
- 한국어 작업 요청 파싱 및 스케줄링
- "피곤할 때" 내일로 작업 연기 기능
- 작업 상태 관리 및 추적

## 사용법 (Usage)

### 기본 실행
```bash
python3 main.py
```

### 작업 스케줄러 직접 사용
```bash
python3 task_scheduler.py
```

## 예시 (Example)
입력: "내일 일어나서 작업합시다, 오늘은 너무 피곤해요."
출력: "이해합니다. 오늘은 휴식하시고 작업이 [날짜]로 예약되었습니다."

## 파일 구조 (File Structure)
- `main.py`: 메인 프로그램 진입점
- `task_scheduler.py`: 작업 스케줄링 핵심 모듈
- `scheduled_tasks.json`: 예약된 작업 저장 파일 (자동 생성)
- `requirements.txt`: 의존성 목록 (표준 라이브러리만 사용)
