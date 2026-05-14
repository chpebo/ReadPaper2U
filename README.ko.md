# ReadPaper2U

[English](./README.md) · [简体中文](./README.zh-CN.md) · **한국어**

> 학술 논문을 비주얼 노벨 형식의 대화 동반자로 만든다.

ReadPaper2U는 PDF 학술 논문을 대화형 읽기 경험으로 바꿔주는 단일
파일 웹 애플리케이션이다. 사용자가 직접 설정할 수 있는 동반자
캐릭터가 비주얼 노벨 스타일의 스크립트로 논문을 한 턴씩 풀어주며,
다 읽은 뒤에는 Q&A 패널에서 후속 질문을 이어갈 수 있다. 수식과
도표, 표는 즉시 렌더링되거나 요약되어 표시되며, 대화 상태는 모두
로컬에 저장된다.

애플리케이션 전체가 `index.html` 한 파일에 들어 있어 빌드 단계가
필요 없으며, 정적 파일을 호스팅할 수 있는 서버라면 어디서든 동작
한다.

첫 실행용 데모(Attention Is All You Need, 완전 오프라인, API 설정
불필요)가 내장되어 있어, 모델을 연결하기 전에도 전체 읽기 흐름을
먼저 체험해 볼 수 있다.

---

## 주요 기능

- **브라우저 내 PDF 파싱** — PDF.js를 통해 클라이언트 측에서 논문을
  파싱하며, arXiv 링크도 입력으로 받는다.
- **비주얼 노벨 모드** — 논문 내용을 동반자 캐릭터가 한 턴씩 풀어
  내는 대화 스크립트로 재구성한다.
- **Q&A 모드** — 비주얼 노벨 모드를 마친 뒤 모델에게 후속 질문을
  이어서 던질 수 있다.
- **내장 오프라인 데모** — 업로드 화면에 원클릭 데모 카드
  (Attention Is All You Need)가 있다. 한국어/영어/중국어 세 가지
  사전 번역 버전이 미리 들어 있어 API 설정 없이도 전체 읽기
  흐름을 그대로 체험할 수 있다.
- **스크립트 번역 (script translation)** — 인터페이스 언어와
  스크립트 언어가 다를 때 원클릭 버튼이나 자동 안내 창을 통해
  스크립트를 장면 단위로 현재 UI 언어로 번역하고 그 결과를
  저장한다.
- **마인드맵 (mind map)** — 생성된 대화 스크립트를 바탕으로 논문의
  논증 구조 마인드맵을 한 번에 만들 수 있으며, SVG / PNG로 내보내어
  노트나 슬라이드에 그대로 삽입할 수 있다.
- **도표·표 처리** — 끄기, 캡션만 표시, 비전 모델로 설명 생성, 대화
  속에 도표 설명을 끼워 넣기의 네 가지 모드 중에서 선택할 수 있다.
- **수식 렌더링** — KaTeX로 LaTeX 수식을 렌더링한다.
- **다국어** — 인터페이스와 대화는 간체 중국어, 영어, 한국어를
  지원한다.
- **다크/라이트 테마** — 설정에서 전환할 수 있고, 상단 바의
  아이콘으로도 바로 토글할 수 있다. 두 테마는 동일한 CSS 변수
  체계를 공유한다.
- **키보드 단축키** — 다음/이전 대사, 자동 재생, 대화 로그, 그리고
  단축키 안내 패널을 제공한다 (`?` 키로 언제든지 안내 패널을 열 수
  있다).
- **자동 재생 시간 자동 조정 (adaptive auto-play)** — 각 장면의
  대기 시간을 텍스트 길이와 스크립트의 주된 문자
  (CJK 글자 수/분 vs. 라틴 단어 수/분)에 따라 자동으로 조절한다.
  짧은 내레이션은 빨리 넘어가고 긴 설명에는 읽을 시간을 충분히
  남긴다.
- **감정별 캐릭터 애니메이션 (emotion-specific character animations)**
  — 동반자 캐릭터의 입체화가 대화 흐름에 따라 미묘한 모션으로
  반응한다.
- **대화 저장** — 대화 상태를 IndexedDB에 보관하며, File System
  Access API를 통해 로컬 폴더로 내보낼 수도 있다.
- **블랙보드 패널** — 사이드바에 핵심 용어, 수식, 논문의 논증
  흐름을 함께 추적한다.
- **LLM 엔드포인트는 본인이 가져온다** — DeepSeek, OpenAI,
  Moonshot/Kimi 등 OpenAI 호환 chat completion 엔드포인트라면 무엇
  이든 사용할 수 있다. API 키는 브라우저의 `localStorage`에만 저장
  되며, 사용자가 지정한 엔드포인트로만 직접 전송된다.

---

## 영감의 출처와 차이점

ReadPaper2U는 [Paper2Gal](https://paper2gal.com/), 즉 학술 논문을 갈게임
(Galgame) 스타일의 비주얼 노벨로 변환하는 웹 애플리케이션에서 영감을 받아
부분적으로 재구현한 프로젝트이다. 두 프로젝트는 동반자 캐릭터를 통해
논문을 읽는다는 핵심 아이디어를 공유한다. ReadPaper2U는 ACG 미학에 묶이지
않고 좀 더 실용성에 무게를 두며, 다음 세 가지 구체적인 설계 차이가 있다:

- **오픈소스이며 셀프 호스팅 가능.** ReadPaper2U는 MIT 라이선스로 배포
  되는 단일 정적 HTML 파일이다. 가입해야 할 서비스도, 사용량 제한도,
  LLM 앞단의 프록시도 존재하지 않는다. 파일은 브라우저에서 사용자가
  지정한 OpenAI 호환 엔드포인트로 직접 요청을 보낸다.
- **"동반자" 캐릭터의 범위가 더 넓다.** 캐릭터 에디터는 12개의 차원
  (종, 외형, 에너지 수준, 격식 정도, 유머 스타일, 시그니처 말투, 전문
  분야, 그리고 네 가지 섹션별 진행 전략)을 노출한다. 기본 아바타는
  작성자가 직접 키우는 고양이의 사진이다. 아니메 풍 캐릭터도 물론 잘
  작동하며, 멘토, 동료, 가상의 연구자, 반려동물도 마찬가지로 가능하다.
  본 앱은 특정한 미학 전통에 묶여 있지 않다.
- **도표를 함께 읽는 모드.** 비전 (vision) 모델을 설정한 경우, 앱은 각
  도표를 한 번 짧게 설명한 뒤 그 설명을 대화에 주입하거나, 스크립트
  생성 호출에 도표 이미지 자체를 함께 보낼 수 있다. 텍스트 전용 모델을
  쓰거나 비용을 통제하고 싶을 때를 위해 캡션만 표시하는 모드와 도표
  추출을 끄는 모드도 함께 제공된다.

ReadPaper2U가 현재 포함하지 않는 것: 배경 음악 (BGM), 음성 합성, 내장
캐릭터 아트 의뢰. 비주얼 노벨은 오로지 텍스트와 한 장의 정적 아바타
위에서만 동작한다.

---

## 빠른 시작

본체는 HTML 한 파일이다. 가장 간단한 방법은 로컬 정적 서버를 띄워
열어보는 것이다 (File System Access API와 PDF.js worker는 모두
`file://`보다 `http://`를 선호한다):

```bash
# Python 3 (모든 플랫폼)
python -m http.server 8765
# 이후 http://localhost:8765 접속
```

첫 실행 시에는 메인 화면이 먼저 뜬다. START를 눌러 업로드 화면으로
들어간 뒤 가운데 있는 "데모 보기: Attention Is All You Need" 카드를
클릭하면 32 장면짜리 사전 번역 데모가 바로 열린다. **API 설정 없이도
처음부터 끝까지 진행할 수 있다.**

직접 가져온 논문으로 사용하려면 **설정**(우측 상단 톱니바퀴 아이콘
또는 메인 화면의 SETTINGS 버튼)을 열고 다음 세 가지를 입력한다:

1. **API 기본 주소 (base URL)** — 예: `https://api.deepseek.com/v1`,
   `https://api.openai.com/v1`, 또는 OpenAI 호환 엔드포인트.
2. **모델 이름** — 예: `deepseek-chat`, `gpt-4o-mini` 등.
3. **API 키** — 현재 기기의 `localStorage`에만 저장된다.

설정을 마친 뒤 PDF를 업로드 영역에 드롭하거나 arXiv 링크를 붙여
넣으면 된다.

### 오프라인 / 폐쇄망 환경

기본 설정에서 PDF.js, KaTeX, 그리고 마인드맵 기능에서만 사용되는
Mermaid는 공개 CDN(`cdnjs.cloudflare.com`, `cdn.jsdelivr.net`)에서
로드된다. CDN에 도달할 수 없을 때는 로컬 `lib/` 폴더로 자동 폴백된다.
완전한 오프라인 사용을 원하면 다음 파일들을 `index.html`과 같은
디렉터리에 배치한다:

```
lib/
├── pdf.min.js
├── pdf.worker.min.js
├── mermaid.min.js              # 마인드맵 기능에서만 필요
└── katex/
    ├── katex.min.js
    ├── katex.min.css
    └── fonts/...
```

내장 데모는 위 파일들이 없어도 완전히 오프라인에서 동작한다
(PDF를 파싱하지 않고 마인드맵도 그리지 않기 때문이다).

해당 파일들은 PDF.js, KaTeX, Mermaid의 공식 릴리스에서 받을 수
있으며, [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)에 자세한
안내가 있다.

---

## 개인정보

애플리케이션은 전적으로 브라우저 안에서 동작한다. 구체적으로:

- PDF는 로컬에서 파싱되며, 그렇게 추출된 텍스트가 chat completion
  요청과 함께 **사용자가 설정한** LLM 엔드포인트로 전송된다.
- API 키는 사용자가 지정한 엔드포인트로 향하는 요청의
  `Authorization` 헤더 외에는 브라우저를 벗어나지 않는다.
- 대화 저장본은 브라우저의 IndexedDB에 보관되며, 사용자가 지정한
  폴더로 내보낼 수도 있다.
- 내장 데모는 어떠한 네트워크 요청도 만들지 않는다.

**미발표** 원고를 업로드하기 전에는 사용 중인 LLM 제공자의 데이터
보존 정책과 학습 활용 정책을 먼저 확인할 것을 권장한다.

---

## 프로젝트 구조

```
readpaper2u/
├── index.html              # 애플리케이션 본체
├── banni.png               # 기본 동반자 캐릭터 아바타
├── find-section.py         # 섹션 마커 탐색 스크립트
├── process_avatar.py       # 일회성: HEIC 사진 → 배경 제거 PNG
├── LICENSE
├── README.md               # 영어 README
├── README.zh-CN.md         # 중국어 README
├── README.ko.md            # 본 파일
├── CHANGELOG.md
├── CONTRIBUTING.md
├── THIRD_PARTY_NOTICES.md
├── requirements.txt        # process_avatar.py 전용
└── .gitignore
```

`index.html`은 의도적으로 단일 파일 구조를 유지한다. 이 파일을
탐색하기 위한 섹션 마커 (section marker) 체계와 보조 스크립트
사용법은 [CONTRIBUTING.md](./CONTRIBUTING.md)에 정리되어 있다.

---

## 보조 스크립트

### `find-section.py`

`index.html` 상단에 삽입된 목차 블록을 나열, 필터링, 재생성한다.
Python 표준 라이브러리만 사용하므로 추가 설치는 필요하지 않다.

```bash
python find-section.py                # CSS와 JS의 모든 섹션 나열
python find-section.py --name api     # 부분 문자열로 필터
python find-section.py --update-toc   # 목차 블록을 그 자리에서 갱신
```

### `process_avatar.py`

HEIC 사진을 배경 제거, 크롭, 알파 채널을 가진 PNG로 변환하는
일회성 도구이다. 동반자 아바타로 새 이미지를 만들 때만 필요하며,
저장소에 포함된 `banni.png`만으로도 바로 사용할 수 있다.

```bash
pip install -r requirements.txt
# 스크립트 상단의 SRC 와 DST 상수를 수정한 뒤:
python process_avatar.py
```

---

## 라이선스

본 프로젝트는 MIT 라이선스로 배포된다. [LICENSE](./LICENSE) 참조.

기본 동반자 아바타 `banni.png`는 작성자가 직접 촬영한 본인의 고양이
사진이며, 동일한 MIT 라이선스로 함께 배포된다. 런타임에 로드되는
서드파티 라이브러리 (PDF.js, KaTeX, Mermaid)는 각자의 라이선스를
따르며, [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)에 정리되어
있다.

---

## 감사의 말

[PDF.js](https://mozilla.github.io/pdf.js/) (Apache 2.0),
[KaTeX](https://katex.org/) (MIT), 그리고
[Mermaid](https://mermaid.js.org/) (MIT) 위에서 만들어졌다. LLM
추론은 사용자가 지정한 OpenAI 호환 엔드포인트가 담당한다. 기본
동반자 캐릭터인 Banni는 실제로 존재하는 고양이이다.
