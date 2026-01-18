# 🃏 Piro Card Game

피로그래밍 24기 4주차 팀 과제 - 숫자 카드 게임

## 📖 프로젝트 소개

1~10 사이의 숫자 카드로 다른 유저와 대결하는 웹 게임입니다.  
랜덤으로 결정되는 승부 규칙(큰 숫자 승리 또는 작은 숫자 승리)에 따라 승패가 결정되며,
승리 시 자신의 카드 숫자만큼 점수를 획득하고, 패배 시 점수를 잃게 됩니다.

### 🎮 게임 방식

1. **공격자**가 5장의 랜덤 카드 중 1장을 선택하고 상대를 지정
2. **수비자**가 5장의 랜덤 카드 중 1장을 선택하여 반격
3. 승부 규칙이 랜덤으로 결정됨 (큰 숫자 승리 / 작은 숫자 승리)
4. 승자는 자신의 카드 숫자만큼 점수 획득, 패자는 점수 차감
5. 누적 점수로 랭킹 결정

## 🛠️ 기술 스택

- **Backend**: Django 5.2.10
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite3
- **Authentication**: Django Allauth (소셜 로그인)

## 📦 설치 및 실행

### 1. 저장소 클론

```bash
git clone https://github.com/your-team/Piro24_CardGame_2.git
cd Piro24_CardGame_2
```

### 2. 가상환경 생성 및 활성화

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 마이그레이션

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. 슈퍼유저 생성

```bash
python manage.py createsuperuser
```

입력 예시:
```
Username: admin
Password: admin
```

### 6. 서버 실행

```bash
python manage.py runserver
```

브라우저에서 `http://127.0.0.1:8000` 접속

## 🎯 테스트 방법

### 테스트 유저 생성

1. `http://127.0.0.1:8000/admin` 접속
2. admin으로 로그인
3. **Users** → **ADD USER +** 클릭
4. 유저 2~3명 생성 (Username/Password: user1/fortest1, user2/fortest2)

### 게임 플레이

**브라우저 1 (user1):**
- 로그인 → 게임 시작 → 카드 선택 → 상대 선택(user2) → 공격

**브라우저 2 (user2):**
- 로그인 → 게임 전적 → 반격하기 → 카드 선택 → 결과 확인

## 📂 프로젝트 구조

```
Piro24_CardGame_2/
├── config/                # Django 설정
├── games/                 # 게임 앱
│   ├── models.py          # Game, PlayerScore 모델
│   ├── services.py        # 게임 로직
│   ├── views/             # 뷰 함수들
│   └── templates/games/   # HTML 템플릿
├── accounts/              # 인증 앱
├── manage.py
└── requirements.txt
```

## 🎨 주요 기능

- ⚔️ **게임 생성/공격**: 5장 중 1장 선택, 상대 지정
- 🛡️ **반격**: 공격받은 게임에 카드 선택
- 📋 **게임 전적**: 진행중/반격대기/완료 게임 확인 (최신순)
- 🎮 **게임 상세**: 카드, 승부 규칙, 결과 표시
- 🏆 **랭킹**: 누적 점수 순위
- ❌ **게임 취소**: 반격 전 취소 가능

## 🎯 게임 규칙

### 승부 규칙 (랜덤)
- **큰 숫자 승리**: 더 큰 카드가 승리
- **작은 숫자 승리**: 더 작은 카드가 승리

### 점수 계산
- **승리**: 자신의 카드 숫자만큼 점수 획득
- **패배**: 자신의 카드 숫자만큼 점수 차감
- **무승부**: 점수 변동 없음

## 🐛 트러블슈팅

**ModuleNotFoundError 발생 시:**
```bash
pip install requests PyJWT cryptography python3-openid oauthlib requests-oauthlib
```

**DB 초기화 (데이터 삭제 주의):**
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

**피로그래밍 24기 2조**