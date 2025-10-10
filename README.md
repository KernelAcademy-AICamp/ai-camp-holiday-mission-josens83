<<<<<<< HEAD
# 🎊 추석 연휴 AI 미션 챌린지

## 📋 이벤트 개요

추석 연휴 기간 동안 AI/LLM 서비스 개발 실습을 진행하는 이벤트입니다.

### 🎁 리워드
- **5개 모두 제출**: 스타벅스 1만원권 💟
- **3~4개 제출**: 스타벅스 아메리카노 ☕

---

## 📅 미션 일정

| 미션 | 날짜 | 학습 범위 | 마감 기한 |
|------|------|-----------|-----------|
| [미션 1](./mission1_20251003/) | 10.03 (금) | Part4: 야놀자 리뷰 요약 | 10.03 23:59 |
| [미션 2](./mission2_20251006/) | 10.06 (월) | Part5: 카카오 대화 요약 | 10.06 23:59 |
| [미션 3](./mission3_20251007/) | 10.07 (화) | Part7: RAG 기초 이론 & 실습 | 10.07 23:59 |
| [미션 4](./mission4_20251008/) | 10.08 (수) | Part8: 실전 RAG | 10.08 23:59 |
| [미션 5](./mission5_20251009/) | 10.09 (목) | Part14: 배민 리뷰기반 메뉴/맛집 추천 | 10.09 23:59 |

---

## 📝 제출 방법

### 1️⃣ 레포지토리 생성
- AI심화 오가니제이션에 레포지토리를 생성합니다
- 레포지토리명: `holiday-mission_이름` (예: `holiday-mission_홍길동`)

### 2️⃣ 미션 제출
각 미션은 해당 날짜의 폴더에 제출합니다:

```
holiday-mission_이름/
├── README.md
├── mission1_20251003/     # 미션 1 제출 폴더
│   ├── 실습코드.ipynb
│   └── README.md
├── mission2_20251006/     # 미션 2 제출 폴더
│   ├── 실습코드.ipynb
│   └── README.md
├── mission3_20251007/     # 미션 3 제출 폴더
│   ├── 실습코드.ipynb
│   └── README.md
├── mission4_20251008/     # 미션 4 제출 폴더
│   ├── 실습코드.ipynb
│   └── README.md
└── mission5_20251009/     # 미션 5 제출 폴더
    ├── 실습코드.ipynb
    └── README.md
```

### 3️⃣ 제출 내용
각 미션 폴더에는 다음을 포함해야 합니다:
- **실습 코드** (Jupyter Notebook 또는 Python 파일)
- **실행 결과** (스크린샷 또는 출력 결과)
- **학습 내용 정리** (README.md에 작성)

### 4️⃣ 마감 시간
- 각 미션은 해당 날짜 **23:59**까지 제출
- Git commit 시간을 기준으로 인정

---

## ✅ 체크리스트

- [ ] 미션 1: 야놀자 리뷰 요약 (10.03)
- [ ] 미션 2: 카카오 대화 요약 (10.06)
- [ ] 미션 3: RAG 기초 이론 & 실습 (10.07)
- [ ] 미션 4: 실전 RAG (10.08)
- [ ] 미션 5: 배민 리뷰기반 메뉴/맛집 추천 (10.09)

---

## 📚 학습 강의

**프롬프트 엔지니어링으로 시작하는 AI/LLM 서비스 개발: 9개 프로젝트로 챗봇부터 AI**

각 미션에 해당하는 Part를 학습한 후 실습을 진행해주세요.

---

## 💡 Tips

1. **매일 조금씩**: 하루에 한 미션씩 꾸준히 진행하세요
2. **코드 주석**: 주요 코드와 함수에는 주석을 달아주세요
3. **학습 정리**: 배운 내용을 README에 정리하면 복습에 도움이 됩니다
4. **질문하기**: 막히는 부분이 있다면 주저하지 말고 질문하세요

---

## 🚀 시작하기

1. 이 템플릿을 fork하거나 다운로드합니다
2. 온라인 강의를 수강합니다
3. 실습을 진행하고 해당 미션 폴더에 코드를 작성합니다
4. README를 작성하고 commit/push합니다
5. 다음 미션으로 넘어갑니다!

---

**Good Luck! 🍀**
=======
# AI Camp Holiday Mission

야놀자 리뷰 크롤링 및 AI 분석 프로젝트

## 프로젝트 개요

이 프로젝트는 야놀자 숙소 리뷰를 크롤링하고, OpenAI를 활용하여 리뷰를 분석하고 요약하는 시스템입니다.

## 주요 기능

- 🕷️ **리뷰 크롤링**: Selenium을 사용한 야놀자 리뷰 자동 수집
- 📊 **데이터 분석**: Pandas를 활용한 리뷰 데이터 전처리 및 시각화
- 🤖 **AI 요약**: OpenAI GPT를 사용한 리뷰 자동 요약
- 🌐 **웹 인터페이스**: Gradio를 활용한 사용자 친화적 웹 UI
- 📓 **Jupyter 노트북**: 데이터 분석 및 시각화를 위한 인터랙티브 환경

## 프로젝트 구조

```
ai-camp-holiday-mission/
├── crawler.py              # 야놀자 리뷰 크롤링 스크립트
├── demo.py                 # Gradio 웹 인터페이스
├── sample_demo.py          # 샘플 데모
├── requirements.txt        # Python 패키지 목록
├── setup_venv.bat          # 가상환경 설정 스크립트 (Windows)
├── ai_camp_demo.ipynb      # Jupyter 노트북 데모
├── README.md               # 프로젝트 문서
├── venv/                   # Python 가상환경 (설정 후 생성)
└── res/                    # 리뷰 데이터 저장소
    ├── reviews.json
    ├── ninetree_pangyo.json
    ├── ninetree_yongsan.json
    └── prompt_1shot.pickle
```

## 설치 및 실행

### 1. 가상환경 설정

Windows에서 자동 설정:
```bash
setup_venv.bat
```

수동 설정:
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate.bat

# 가상환경 활성화 (Linux/Mac)
source venv/bin/activate

# 패키지 설치
pip install -r requirements.txt
```

### 2. 환경 변수 설정

OpenAI API 키를 설정하세요:
```bash
# Windows
set OPENAI_API_KEY=your-api-key-here

# Linux/Mac
export OPENAI_API_KEY=your-api-key-here
```

### 3. 실행 방법

#### Jupyter Lab 실행
```bash
jupyter lab
```

#### Gradio 웹 인터페이스 실행
```bash
python demo.py
```

#### 리뷰 크롤링 실행
```bash
python crawler.py [숙소명] [야놀자_URL]
```

예시:
```bash
python crawler.py "인사동" "https://www.yanolja.com/hotel/12345"
```

## 사용된 기술

- **Python 3.8+**
- **Selenium**: 웹 크롤링
- **BeautifulSoup4**: HTML 파싱
- **OpenAI API**: 리뷰 요약
- **Gradio**: 웹 인터페이스
- **Pandas**: 데이터 분석
- **Matplotlib/Seaborn**: 데이터 시각화
- **Jupyter Lab**: 인터랙티브 개발 환경

## 주요 파일 설명

### crawler.py
야놀자 웹사이트에서 리뷰를 크롤링하는 스크립트입니다.
- Selenium WebDriver를 사용하여 동적 콘텐츠 로딩
- 자동 스크롤을 통한 모든 리뷰 수집
- JSON 형태로 리뷰 데이터 저장

### demo.py
Gradio를 사용한 웹 인터페이스입니다.
- 숙소 선택 드롭다운
- 긍정/부정 리뷰 요약 결과 표시
- OpenAI API를 통한 실시간 리뷰 분석

### ai_camp_demo.ipynb
Jupyter 노트북으로 프로젝트의 모든 기능을 시연합니다.
- 데이터 로드 및 전처리
- 시각화 및 분석
- API 호출 예제

## 요구사항

- Python 3.8 이상
- Chrome 브라우저 (Selenium용)
- OpenAI API 키
- 인터넷 연결

## 라이선스

이 프로젝트는 교육 목적으로 제작되었습니다.

## 문의

프로젝트에 대한 문의사항이 있으시면 이슈를 등록해주세요.
>>>>>>> 97de7dd1 (Initial commit: AI Camp Holiday Mission project)

