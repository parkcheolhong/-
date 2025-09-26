# AI 통역 및 코드 분석 프로그램 
# AI Translation and Code Analysis Program

GPT AI를 활용한 고급 통역 프로그램과 소스 코드 분석 도구입니다.
Advanced translation program and source code analysis tool powered by GPT AI.

## 주요 기능 / Features

### 🌐 번역 기능 / Translation Features
- **다국어 지원**: 한국어, 영어, 일본어, 중국어, 스페인어, 프랑스어, 독일어, 러시아어 등
- **자동 언어 감지**: 소스 언어 자동 인식
- **문화적 맥락 고려**: 단순 번역을 넘어선 문화적 맥락 제공
- **고품질 번역**: GPT AI 모델을 통한 자연스러운 번역

### 🔍 코드 분석 기능 / Code Analysis Features
- **다양한 프로그래밍 언어 지원**: Python, JavaScript, Java, C/C++, Go 등
- **포괄적 코드 리뷰**: 품질, 보안, 성능 분석
- **개선 제안**: 구체적인 코드 개선 방향 제시
- **베스트 프랙티스**: 업계 표준에 따른 권장사항

## 설치 및 설정 / Installation & Setup

### 1. 의존성 설치 / Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. OpenAI API 키 설정 / Configure OpenAI API Key
```bash
# .env 파일 생성 / Create .env file
cp .env.example .env

# .env 파일에 API 키 입력 / Add your API key to .env
OPENAI_API_KEY=your_openai_api_key_here
```

## 사용법 / Usage

### 📝 텍스트 번역 / Text Translation

```bash
# 한국어로 번역 / Translate to Korean
python translator.py translate "Hello, how are you?" --target ko

# 영어로 번역 / Translate to English  
python translator.py translate "안녕하세요, 어떻게 지내세요?" --target en

# 특정 언어에서 번역 / Translate from specific language
python translator.py translate "こんにちは" --source ja --target ko
```

### 🔍 코드 분석 / Code Analysis

```bash
# 파일 분석 / Analyze file
python translator.py analyze --file example.py

# 표준 입력으로 분석 / Analyze from stdin
echo "def hello(): print('world')" | python translator.py analyze

# 특정 언어로 분석 / Analyze with specific language
python translator.py analyze --file script.js --language javascript
```

### 📋 지원 언어 확인 / Check Supported Languages

```bash
# 번역 지원 언어 / Translation languages
python translator.py languages

# 코드 분석 지원 언어 / Programming languages  
python translator.py prog-languages
```

## 지원 언어 / Supported Languages

### 번역 언어 / Translation Languages
- **ko**: 한국어 (Korean)
- **en**: 영어 (English)
- **ja**: 일본어 (Japanese)
- **zh**: 중국어 간체 (Chinese Simplified)
- **zh-tw**: 중국어 번체 (Chinese Traditional)
- **es**: 스페인어 (Spanish)
- **fr**: 프랑스어 (French)
- **de**: 독일어 (German)
- **ru**: 러시아어 (Russian)
- **it**: 이탈리아어 (Italian)
- **pt**: 포르투갈어 (Portuguese)
- **ar**: 아랍어 (Arabic)
- **hi**: 힌디어 (Hindi)

### 프로그래밍 언어 / Programming Languages
- Python, JavaScript, TypeScript, Java
- C, C++, C#, Go, Rust
- PHP, Ruby, Kotlin, Swift, Scala
- R, SQL, HTML, CSS
- Bash, PowerShell

## 예제 / Examples

### 번역 예제 / Translation Examples

```bash
# 영어 → 한국어
$ python translator.py translate "Good morning" --target ko
=== Translation Result ===
Source Language: Auto-detect
Target Language: Korean
Model Used: gpt-3.5-turbo

Original Text:
Good morning

Translation:
좋은 아침입니다.

# 한국어 → 일본어
$ python translator.py translate "안녕하세요" --source ko --target ja
```

### 코드 분석 예제 / Code Analysis Examples

```bash
# Python 코드 분석
$ python translator.py analyze --file example.py
=== Code Analysis Result ===
Language: python
Model Used: gpt-3.5-turbo

Analysis:
이 Python 코드에 대한 분석 결과:

1. **감지된 프로그래밍 언어**: Python

2. **코드 품질 평가**: 
   - 기본적인 Python 구조는 올바름
   - 함수와 클래스 정의가 적절함

3. **잠재적 문제점**:
   - fibonacci 함수: 재귀 호출로 인한 성능 문제 (지수적 시간 복잡도)
   - divide_numbers 함수: 0으로 나누기 예외 처리 없음
   - get_average 메서드: 빈 리스트에 대한 예외 처리 없음

4. **개선 제안**:
   - fibonacci: 메모이제이션 또는 동적 프로그래밍 사용
   - 모든 함수에 적절한 예외 처리 추가
   - 입력 검증 로직 추가

5. **보안 고려사항**:
   - 현재 코드에서 심각한 보안 문제는 없음
   - 입력 검증 강화 권장

6. **성능 고려사항**:
   - fibonacci 함수 최적화 필요
   - 큰 데이터셋 처리 시 메모리 사용량 고려
```

## 파일 구조 / File Structure

```
.
├── translator.py        # 메인 프로그램 / Main program
├── config.py           # 설정 파일 / Configuration
├── utils.py            # 유틸리티 함수 / Utility functions
├── example.py          # 코드 분석 예제 / Code analysis example
├── requirements.txt    # Python 의존성 / Dependencies
├── .env.example       # 환경변수 예제 / Environment variables example
├── .gitignore         # Git 무시 파일 / Git ignore rules
└── README.md          # 이 파일 / This file
```

## 기여하기 / Contributing

이 프로젝트에 기여하고 싶으시다면:
If you'd like to contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 라이선스 / License

이 프로젝트는 MIT 라이선스 하에 배포됩니다.
This project is distributed under the MIT License.

## 문제 해결 / Troubleshooting

### API 키 관련 문제 / API Key Issues
- OpenAI API 키가 올바르게 설정되었는지 확인하세요
- `.env` 파일이 프로젝트 루트에 있는지 확인하세요

### 의존성 문제 / Dependency Issues
- Python 3.7 이상이 설치되어 있는지 확인하세요
- `pip install -r requirements.txt`로 모든 의존성을 설치하세요

### 인코딩 문제 / Encoding Issues
- 파일이 UTF-8로 인코딩되어 있는지 확인하세요
- 특수 문자가 포함된 텍스트는 따옴표로 감싸주세요