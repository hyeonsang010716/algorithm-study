# 🏆 알고리즘 스터디 (2025.01.01 - 2025.02.28)

프론트엔드는 `Streamlit`, 백엔드는 `Flask`와 `FastAPI`를 사용하여 API 통신을 통해 알고리즘 문제를 푸는 프로젝트입니다.  
이 과정에서 **백엔드 API 통신 기술과 알고리즘을 융합적으로 학습**하였습니다.

---

## 🚀 프로젝트 목표
- **API 통신을 활용한 알고리즘 문제 풀이**
- **파일 기반 및 DB 기반의 문제 입력 처리 학습**
- **GitHub 브랜치 컨벤션 및 PR 활용 실습**
- **협업을 통해 백엔드-프론트엔드 연동 경험 쌓기**

---

## 🛠 기술 스택

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 👥 팀 구성

| 역할 | 담당자 | 기술 |
|------|------|------|
| 프론트엔드 | - | `Streamlit` |
| 백엔드 | UH3135 | `Flask` |
| 백엔드 | sentryc0201 | `Flask` |
| 백엔드 | dbwognl123 | `FastAPI` |
| 백엔드 | hyeonsang010716 | `FastAPI` |

---

## 📆 스터디 진행 과정

### 📍 1~2주차: 백엔드 환경 세팅 및 API 통신 학습
- Python 가상환경 설정 및 FastAPI/Flask 설치
- API를 활용한 알고리즘 문제 풀이 방식 학습

### 📍 3~4주차: 파일 기반 API 통신 학습
- 문제 입력을 파일로 전달하고, API에서 파일을 처리하는 방식 구현

### 📍 5~6주차: DB 기반 API 통신 학습
- 문제를 DB에 저장하고, API를 통해 데이터를 가져와 문제 풀이 진행

### 📍 7~8주차: 종합 실습 및 문제 풀이
- 위에서 배운 기술을 활용하여 다양한 알고리즘 문제 해결

---

## 🔥 우리가 배운 것
✅ **API를 이용한 알고리즘 문제 해결 방식**  
✅ **FastAPI & Flask 활용법**  
✅ **파일 및 DB를 활용한 문제 입력 처리 방법**  
✅ **GitHub 협업 (브랜치 컨벤션, PR 방식 등)**  

---

## 🎯 프로젝트 실행 방법

```bash
# 가상환경 설정 (선택 사항)
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate  # Windows

# 패키지 설치
pip install -r requirements.txt

# 서버 실행 (예시)
uvicorn main:app --reload  # FastAPI 실행
python app.py  # Flask 실행
