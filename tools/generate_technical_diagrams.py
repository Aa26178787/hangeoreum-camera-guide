from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parents[1] / "docs" / "images"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1600, 900
FONT = "'Noto Serif KR','Malgun Gothic',serif"
COLORS = {
    "ink": "#17324f",
    "text": "#33475b",
    "muted": "#68798b",
    "blue": "#315f91",
    "blue_bg": "#edf4fb",
    "green": "#3f856c",
    "green_bg": "#edf7f3",
    "orange": "#b47722",
    "orange_bg": "#fff5e6",
    "purple": "#765a9f",
    "purple_bg": "#f4f0fa",
    "red": "#b64a4a",
    "red_bg": "#fff0f0",
    "line": "#b8c5d1",
}


def header(title, subtitle, number):
    return f"""
    <text x="800" y="72" text-anchor="middle" class="title">{escape(title)}</text>
    <text x="800" y="112" text-anchor="middle" class="subtitle">{escape(subtitle)}</text>
    <text x="800" y="856" text-anchor="middle" class="caption">그림 {number}. {escape(title)}</text>
    """


def wrap(body, title, subtitle, number):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">
    <defs>
      <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0 0 L12 6 L0 12 Z" fill="{COLORS['blue']}"/></marker>
      <marker id="arrow-red" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0 0 L12 6 L0 12 Z" fill="{COLORS['red']}"/></marker>
      <style>
        .title{{font:700 44px {FONT};fill:{COLORS['ink']}}}
        .subtitle{{font:400 22px {FONT};fill:{COLORS['muted']}}}
        .head{{font:700 26px {FONT};fill:{COLORS['ink']}}}
        .body{{font:400 21px {FONT};fill:{COLORS['text']}}}
        .small{{font:400 18px {FONT};fill:{COLORS['muted']}}}
        .label{{font:600 20px {FONT};fill:{COLORS['ink']}}}
        .caption{{font:400 18px {FONT};fill:{COLORS['muted']}}}
        .arrow{{fill:none;stroke:{COLORS['blue']};stroke-width:5;marker-end:url(#arrow)}}
        .thin{{fill:none;stroke:{COLORS['line']};stroke-width:3}}
      </style>
    </defs>
    <rect width="1600" height="900" fill="#ffffff"/>
    {header(title, subtitle, number)}
    {body}
    </svg>"""


def save(name, svg):
    (OUT / name).write_text(svg, encoding="utf-8")


camera_body = f"""
  <rect x="80" y="235" width="260" height="310" rx="24" fill="{COLORS['blue_bg']}" stroke="{COLORS['blue']}" stroke-width="3"/>
  <text x="210" y="290" text-anchor="middle" class="head">CameraX</text>
  <rect x="125" y="325" width="170" height="105" rx="12" fill="#ffffff" stroke="{COLORS['line']}" stroke-width="2"/>
  <circle cx="210" cy="365" r="22" fill="none" stroke="{COLORS['blue']}" stroke-width="4"/>
  <path d="M175 415 L245 415 L225 383 L195 383 Z" fill="none" stroke="{COLORS['blue']}" stroke-width="4"/>
  <text x="210" y="495" text-anchor="middle" class="body">카메라 프레임 입력</text>

  <path d="M340 340 L455 250" class="arrow"/>
  <path d="M340 430 L455 520" class="arrow"/>

  <rect x="470" y="170" width="300" height="205" rx="22" fill="{COLORS['green_bg']}" stroke="{COLORS['green']}" stroke-width="3"/>
  <text x="620" y="225" text-anchor="middle" class="head">Preview</text>
  <text x="620" y="275" text-anchor="middle" class="body">카메라 화면을 끊김 없이 표시</text>
  <text x="620" y="320" text-anchor="middle" class="small">촬영자에게 실시간 영상 제공</text>

  <rect x="470" y="445" width="300" height="235" rx="22" fill="{COLORS['orange_bg']}" stroke="{COLORS['orange']}" stroke-width="3"/>
  <text x="620" y="500" text-anchor="middle" class="head">ImageAnalysis</text>
  <text x="620" y="550" text-anchor="middle" class="body">최신 프레임만 AI에 전달</text>
  <text x="620" y="595" text-anchor="middle" class="small">KEEP_ONLY_LATEST</text>
  <g transform="translate(530 625)">
    <rect x="0" y="0" width="42" height="28" fill="#d2deea"/><rect x="56" y="0" width="42" height="28" fill="#d2deea"/>
    <rect x="112" y="0" width="42" height="28" fill="{COLORS['orange']}"/><rect x="168" y="0" width="42" height="28" fill="#d2deea"/>
  </g>

  <path d="M770 560 L900 560" class="arrow"/>
  <rect x="915" y="445" width="280" height="235" rx="22" fill="{COLORS['purple_bg']}" stroke="{COLORS['purple']}" stroke-width="3"/>
  <text x="1055" y="500" text-anchor="middle" class="head">비동기 AI 분석</text>
  <text x="1055" y="550" text-anchor="middle" class="body">Pose Landmarker</text>
  <text x="1055" y="590" text-anchor="middle" class="body">Object Detector</text>
  <text x="1055" y="635" text-anchor="middle" class="small">UI 스레드와 분리</text>

  <path d="M770 270 C1030 270 1020 310 1245 310" class="arrow"/>
  <path d="M1195 560 C1260 560 1250 475 1300 475" class="arrow"/>
  <rect x="1305" y="265" width="225" height="315" rx="22" fill="{COLORS['blue_bg']}" stroke="{COLORS['blue']}" stroke-width="3"/>
  <text x="1417" y="320" text-anchor="middle" class="head">화면 합성</text>
  <rect x="1350" y="350" width="135" height="150" rx="10" fill="#ffffff" stroke="{COLORS['line']}" stroke-width="2"/>
  <rect x="1375" y="380" width="85" height="90" fill="none" stroke="{COLORS['green']}" stroke-width="3"/>
  <path d="M1365 520 L1470 520" stroke="{COLORS['blue']}" stroke-width="5" marker-end="url(#arrow)"/>
  <text x="1417" y="555" text-anchor="middle" class="small">영상 + 안내 오버레이</text>
"""
save("camera-frame-pipeline.svg", wrap(camera_body, "CameraX 기반 프레임 처리 구조", "미리보기와 AI 분석을 분리하고 최신 프레임을 우선 처리", 2))


pose_points = [(350,220),(325,250),(375,250),(305,270),(395,270),(350,300),(290,330),(410,330),(260,400),(440,400),(235,475),(465,475),(315,455),(385,455),(305,555),(395,555),(295,670),(405,670)]
pose_lines = [(0,5),(5,6),(5,7),(6,8),(8,10),(7,9),(9,11),(5,12),(5,13),(12,13),(12,14),(14,16),(13,15),(15,17)]
pose_svg = []
for a,b in pose_lines:
    x1,y1=pose_points[a]; x2,y2=pose_points[b]
    pose_svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{COLORS["blue"]}" stroke-width="8" stroke-linecap="round"/>')
for x,y in pose_points:
    pose_svg.append(f'<circle cx="{x}" cy="{y}" r="10" fill="#ffffff" stroke="{COLORS["blue"]}" stroke-width="5"/>')
pose_body = f"""
  <rect x="110" y="165" width="500" height="600" rx="24" fill="{COLORS['blue_bg']}" stroke="{COLORS['blue']}" stroke-width="3"/>
  <text x="360" y="205" text-anchor="middle" class="head">인물 랜드마크 검출</text>
  <ellipse cx="350" cy="270" rx="58" ry="72" fill="#d8e3ee" opacity="0.7"/>
  <path d="M285 315 Q350 275 415 315 L440 480 Q350 530 260 480 Z" fill="#d8e3ee" opacity="0.55"/>
  {''.join(pose_svg)}
  <rect x="215" y="190" width="270" height="520" fill="none" stroke="{COLORS['green']}" stroke-width="3" stroke-dasharray="12 8"/>
  <text x="350" y="742" text-anchor="middle" class="small">랜드마크·인물 경계·가시성 신뢰도</text>

  <path d="M610 460 L750 460" class="arrow"/>
  <rect x="770" y="165" width="720" height="600" rx="24" fill="#ffffff" stroke="{COLORS['line']}" stroke-width="3"/>
  <text x="1130" y="215" text-anchor="middle" class="head">한걸음에서 사용하는 특징값</text>
  <rect x="820" y="265" width="290" height="160" rx="18" fill="{COLORS['green_bg']}" stroke="{COLORS['green']}" stroke-width="2"/>
  <text x="965" y="310" text-anchor="middle" class="label">전신 검출 여부</text>
  <text x="965" y="355" text-anchor="middle" class="body">머리·무릎·발목·발끝</text>
  <text x="965" y="390" text-anchor="middle" class="small">필수 관절의 가시성 확인</text>
  <rect x="1150" y="265" width="290" height="160" rx="18" fill="{COLORS['orange_bg']}" stroke="{COLORS['orange']}" stroke-width="2"/>
  <text x="1295" y="310" text-anchor="middle" class="label">인물 위치·크기</text>
  <text x="1295" y="355" text-anchor="middle" class="body">중심점·점유율·경계</text>
  <text x="1295" y="390" text-anchor="middle" class="small">전후·좌우 이동 판단</text>
  <rect x="820" y="470" width="290" height="160" rx="18" fill="{COLORS['purple_bg']}" stroke="{COLORS['purple']}" stroke-width="2"/>
  <text x="965" y="515" text-anchor="middle" class="label">신체 절단</text>
  <text x="965" y="560" text-anchor="middle" class="body">화면 경계와 관절 비교</text>
  <text x="965" y="595" text-anchor="middle" class="small">머리·손·발 잘림 판정</text>
  <rect x="1150" y="470" width="290" height="160" rx="18" fill="{COLORS['blue_bg']}" stroke="{COLORS['blue']}" stroke-width="2"/>
  <text x="1295" y="515" text-anchor="middle" class="label">인물 마스크</text>
  <text x="1295" y="560" text-anchor="middle" class="body">인물과 배경 영역 분리</text>
  <text x="1295" y="595" text-anchor="middle" class="small">윤곽·여백 계산 보조</text>
"""
save("pose-landmark-analysis.svg", wrap(pose_body, "신체 랜드마크 기반 전신 인물 분석", "Pose Landmarker 출력값을 구도 평가에 필요한 특징으로 변환", 3))


object_body = f"""
  <rect x="90" y="165" width="900" height="600" rx="24" fill="#eef3f6" stroke="{COLORS['line']}" stroke-width="3"/>
  <path d="M90 570 Q300 440 520 540 T990 500 L990 765 L90 765 Z" fill="#dbe6dc"/>
  <rect x="160" y="250" width="170" height="350" fill="none" stroke="{COLORS['muted']}" stroke-width="4"/>
  <circle cx="245" cy="330" r="45" fill="#b9c5cf"/><path d="M185 570 Q245 370 305 570" fill="#b9c5cf"/>
  <text x="245" y="625" text-anchor="middle" class="small">주변 사람</text>
  <rect x="395" y="195" width="300" height="510" fill="none" stroke="{COLORS['green']}" stroke-width="6"/>
  <circle cx="545" cy="300" r="58" fill="#8fb6a5"/><path d="M445 655 Q545 360 645 655" fill="#8fb6a5"/>
  <text x="545" y="735" text-anchor="middle" class="label">주 피사체</text>
  <rect x="650" y="245" width="210" height="400" fill="none" stroke="{COLORS['red']}" stroke-width="5"/>
  <circle cx="745" cy="330" r="48" fill="#cfaaaa"/><path d="M675 610 Q745 385 820 610" fill="#cfaaaa"/>
  <rect x="650" y="250" width="95" height="120" fill="{COLORS['red_bg']}" opacity="0.8" stroke="{COLORS['red']}" stroke-width="3" stroke-dasharray="9 6"/>
  <text x="755" y="680" text-anchor="middle" class="small" fill="{COLORS['red']}">얼굴 주변 실제 겹침</text>
  <rect x="865" y="390" width="90" height="185" rx="8" fill="#ccb78c" stroke="{COLORS['orange']}" stroke-width="3"/>
  <text x="910" y="610" text-anchor="middle" class="small">조형물</text>

  <path d="M990 460 L1090 460" class="arrow"/>
  <rect x="1110" y="190" width="400" height="520" rx="24" fill="#ffffff" stroke="{COLORS['line']}" stroke-width="3"/>
  <text x="1310" y="245" text-anchor="middle" class="head">간섭 판단 원칙</text>
  <circle cx="1170" cy="315" r="20" fill="{COLORS['green']}"/><text x="1210" y="323" class="body">존재 자체는 감점하지 않음</text>
  <circle cx="1170" cy="395" r="20" fill="{COLORS['red']}"/><text x="1210" y="403" class="body">얼굴·신체 겹침은 우선 경고</text>
  <circle cx="1170" cy="475" r="20" fill="{COLORS['orange']}"/><text x="1210" y="483" class="body">윤곽 구분 방해 여부 확인</text>
  <line x1="1160" y1="550" x2="1460" y2="550" stroke="{COLORS['line']}" stroke-width="2"/>
  <text x="1310" y="600" text-anchor="middle" class="label">관광지의 군중·조형물 보존</text>
  <text x="1310" y="645" text-anchor="middle" class="small">장소 특성은 유지하고 실제 방해만 평가</text>
"""
save("object-interference-analysis.svg", wrap(object_body, "주 피사체와 주변 객체의 간섭 판단", "사람이 많다는 이유가 아니라 얼굴·신체의 실제 가림 여부를 평가", 4))


movement_body = f"""
  <rect x="100" y="170" width="750" height="600" rx="24" fill="{COLORS['blue_bg']}" stroke="{COLORS['blue']}" stroke-width="3"/>
  <text x="475" y="220" text-anchor="middle" class="head">화면 변화로 촬영자 이동 판단</text>
  <rect x="310" y="300" width="330" height="300" rx="28" fill="#ffffff" stroke="{COLORS['ink']}" stroke-width="6"/>
  <circle cx="475" cy="375" r="35" fill="{COLORS['green_bg']}" stroke="{COLORS['green']}" stroke-width="4"/>
  <path d="M420 550 Q475 405 530 550" fill="{COLORS['green_bg']}" stroke="{COLORS['green']}" stroke-width="4"/>
  <line x1="475" y1="270" x2="475" y2="185" class="arrow"/>
  <line x1="475" y1="630" x2="475" y2="720" class="arrow"/>
  <line x1="280" y1="450" x2="185" y2="450" class="arrow"/>
  <line x1="670" y1="450" x2="765" y2="450" class="arrow"/>
  <text x="475" y="165" text-anchor="middle" class="label">앞으로: 인물 크게</text>
  <text x="475" y="755" text-anchor="middle" class="label">뒤로: 인물 작게</text>
  <text x="155" y="458" text-anchor="end" class="label">왼쪽</text>
  <text x="795" y="458" class="label">오른쪽</text>

  <rect x="900" y="170" width="600" height="600" rx="24" fill="{COLORS['purple_bg']}" stroke="{COLORS['purple']}" stroke-width="3"/>
  <text x="1200" y="220" text-anchor="middle" class="head">센서로 카메라 각도 판단</text>
  <rect x="1100" y="310" width="200" height="330" rx="28" fill="#ffffff" stroke="{COLORS['ink']}" stroke-width="6" transform="rotate(-9 1200 475)"/>
  <path d="M1015 405 A205 205 0 0 1 1375 370" fill="none" stroke="{COLORS['red']}" stroke-width="6" marker-end="url(#arrow-red)"/>
  <text x="1200" y="330" text-anchor="middle" class="label">Roll</text>
  <path d="M1360 470 A180 120 0 0 1 1320 610" fill="none" stroke="{COLORS['orange']}" stroke-width="6" marker-end="url(#arrow)"/>
  <text x="1395" y="550" class="label">Pitch</text>
  <text x="1200" y="700" text-anchor="middle" class="body">Game Rotation Vector Sensor</text>
  <text x="1200" y="735" text-anchor="middle" class="small">위치 센서가 아니라 상대 기울기 측정에 사용</text>
"""
save("movement-orientation.svg", wrap(movement_body, "촬영자 이동과 카메라 각도 판단", "인물 크기·중심점 변화와 회전 벡터 센서를 결합", 5))


score_body = f"""
  <text x="360" y="175" text-anchor="middle" class="head">항목별 정규화 점수</text>
  <g>
    <rect x="105" y="220" width="510" height="80" rx="16" fill="{COLORS['blue_bg']}" stroke="{COLORS['blue']}" stroke-width="2"/><text x="135" y="270" class="label">P 인물 위치</text><rect x="340" y="248" width="220" height="20" rx="10" fill="#d4dfeb"/><rect x="340" y="248" width="170" height="20" rx="10" fill="{COLORS['blue']}"/>
    <rect x="105" y="320" width="510" height="80" rx="16" fill="{COLORS['green_bg']}" stroke="{COLORS['green']}" stroke-width="2"/><text x="135" y="370" class="label">S 인물 크기</text><rect x="340" y="348" width="220" height="20" rx="10" fill="#d4dfeb"/><rect x="340" y="348" width="150" height="20" rx="10" fill="{COLORS['green']}"/>
    <rect x="105" y="420" width="510" height="80" rx="16" fill="{COLORS['orange_bg']}" stroke="{COLORS['orange']}" stroke-width="2"/><text x="135" y="470" class="label">M 여백</text><rect x="340" y="448" width="220" height="20" rx="10" fill="#d4dfeb"/><rect x="340" y="448" width="125" height="20" rx="10" fill="{COLORS['orange']}"/>
    <rect x="105" y="520" width="510" height="80" rx="16" fill="{COLORS['purple_bg']}" stroke="{COLORS['purple']}" stroke-width="2"/><text x="135" y="570" class="label">L 수평·기울기</text><rect x="340" y="548" width="220" height="20" rx="10" fill="#d4dfeb"/><rect x="340" y="548" width="195" height="20" rx="10" fill="{COLORS['purple']}"/>
    <rect x="105" y="620" width="510" height="80" rx="16" fill="{COLORS['red_bg']}" stroke="{COLORS['red']}" stroke-width="2"/><text x="135" y="670" class="label">B 절단·간섭</text><rect x="340" y="648" width="220" height="20" rx="10" fill="#d4dfeb"/><rect x="340" y="648" width="75" height="20" rx="10" fill="{COLORS['red']}"/>
  </g>
  <path d="M615 460 L760 460" class="arrow"/>
  <circle cx="900" cy="460" r="125" fill="{COLORS['blue_bg']}" stroke="{COLORS['blue']}" stroke-width="5"/>
  <text x="900" y="430" text-anchor="middle" class="head">가중 합산</text>
  <text x="900" y="485" text-anchor="middle" class="body">C = Σ wᵢxᵢ</text>
  <text x="900" y="525" text-anchor="middle" class="small">항목별 허용 범위 적용</text>
  <path d="M1025 460 L1160 460" class="arrow"/>
  <rect x="1175" y="260" width="330" height="400" rx="24" fill="#ffffff" stroke="{COLORS['line']}" stroke-width="3"/>
  <text x="1340" y="320" text-anchor="middle" class="head">우선순위 결정</text>
  <rect x="1225" y="365" width="230" height="75" rx="14" fill="{COLORS['red_bg']}" stroke="{COLORS['red']}" stroke-width="3"/><text x="1340" y="413" text-anchor="middle" class="label">1. 신체 절단·가림</text>
  <rect x="1225" y="465" width="230" height="75" rx="14" fill="{COLORS['orange_bg']}" stroke="{COLORS['orange']}" stroke-width="2"/><text x="1340" y="513" text-anchor="middle" class="label">2. 크기·위치</text>
  <rect x="1225" y="565" width="230" height="55" rx="14" fill="{COLORS['blue_bg']}" stroke="{COLORS['blue']}" stroke-width="2"/><text x="1340" y="601" text-anchor="middle" class="label">3. 수평·여백</text>
"""
save("composition-score.svg", wrap(score_body, "항목별 구도 점수 산출 구조", "설명 가능한 규칙 기반 점수로 문제의 크기와 안내 우선순위를 결정", 6))


guidance_body = f"""
  <rect x="610" y="145" width="380" height="80" rx="18" fill="{COLORS['blue_bg']}" stroke="{COLORS['blue']}" stroke-width="3"/><text x="800" y="195" text-anchor="middle" class="head">현재 화면 분석 결과</text>
  <path d="M800 225 L800 285" class="arrow"/>
  <polygon points="800,280 1010,370 800,460 590,370" fill="{COLORS['red_bg']}" stroke="{COLORS['red']}" stroke-width="3"/>
  <text x="800" y="362" text-anchor="middle" class="label">신체가 잘렸거나</text><text x="800" y="394" text-anchor="middle" class="label">얼굴이 가려졌는가?</text>
  <path d="M590 370 L360 370" class="arrow"/><text x="490" y="348" text-anchor="middle" class="small">예</text>
  <rect x="95" y="315" width="265" height="110" rx="18" fill="{COLORS['red_bg']}" stroke="{COLORS['red']}" stroke-width="3"/><text x="228" y="360" text-anchor="middle" class="label">최우선 안내</text><text x="228" y="395" text-anchor="middle" class="body">뒤로 이동·가림 회피</text>
  <path d="M800 460 L800 505" class="arrow"/><text x="830" y="490" class="small">아니오</text>
  <polygon points="800,500 1010,580 800,660 590,580" fill="{COLORS['orange_bg']}" stroke="{COLORS['orange']}" stroke-width="3"/>
  <text x="800" y="572" text-anchor="middle" class="label">인물 크기와 위치가</text><text x="800" y="604" text-anchor="middle" class="label">허용 범위인가?</text>
  <path d="M590 580 L360 580" class="arrow"/><text x="490" y="558" text-anchor="middle" class="small">아니오</text>
  <rect x="95" y="525" width="265" height="110" rx="18" fill="{COLORS['orange_bg']}" stroke="{COLORS['orange']}" stroke-width="3"/><text x="228" y="570" text-anchor="middle" class="label">이동 안내</text><text x="228" y="605" text-anchor="middle" class="body">전후·좌우 한 동작</text>
  <path d="M1010 580 L1235 580" class="arrow"/><text x="1110" y="558" text-anchor="middle" class="small">예</text>
  <rect x="1240" y="505" width="270" height="150" rx="18" fill="{COLORS['green_bg']}" stroke="{COLORS['green']}" stroke-width="3"/><text x="1375" y="555" text-anchor="middle" class="label">각도·여백 확인</text><text x="1375" y="595" text-anchor="middle" class="body">필요 시 미세 조정</text><text x="1375" y="630" text-anchor="middle" class="small">충족하면 촬영 가능</text>
  <rect x="500" y="720" width="600" height="65" rx="16" fill="{COLORS['purple_bg']}" stroke="{COLORS['purple']}" stroke-width="2"/>
  <text x="800" y="762" text-anchor="middle" class="label">한 번에 가장 중요한 행동 하나만 표시</text>
"""
save("guidance-priority.svg", wrap(guidance_body, "구도 문제 우선순위에 따른 안내 결정", "치명적 오류를 먼저 해결하고 한 번에 하나의 행동만 제시", 7))


frames = []
for i in range(12):
    x = 145 + i * 112
    fill = COLORS['blue_bg'] if i in (0,3,6,9) else "#f2f4f6"
    stroke = COLORS['blue'] if i in (0,3,6,9) else COLORS['line']
    frames.append(f'<rect x="{x}" y="245" width="78" height="70" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="3"/><text x="{x+39}" y="289" text-anchor="middle" class="small">F{i+1}</text>')
    if i in (0,3,6,9):
        frames.append(f'<circle cx="{x+39}" cy="390" r="18" fill="{COLORS["green"]}"/><text x="{x+39}" y="430" text-anchor="middle" class="small">Pose</text>')
    if i in (0,6):
        frames.append(f'<rect x="{x+21}" y="485" width="36" height="36" rx="6" fill="{COLORS["orange"]}"/><text x="{x+39}" y="545" text-anchor="middle" class="small">Object</text>')
    if i in (3,9):
        frames.append(f'<path d="M{x+15} 610 L{x+30} 625 L{x+63} 590" fill="none" stroke="{COLORS["purple"]}" stroke-width="7"/><text x="{x+39}" y="665" text-anchor="middle" class="small">UI 갱신</text>')
optimization_body = f"""
  <text x="95" y="288" class="label">카메라 프레임</text>
  <text x="95" y="400" class="label">자세 검출</text>
  <text x="95" y="510" class="label">객체 검출</text>
  <text x="95" y="620" class="label">안내 갱신</text>
  <line x1="130" y1="335" x2="1500" y2="335" stroke="{COLORS['line']}" stroke-width="3"/>
  {''.join(frames)}
  <rect x="200" y="710" width="1200" height="70" rx="18" fill="{COLORS['blue_bg']}" stroke="{COLORS['blue']}" stroke-width="2"/>
  <text x="800" y="755" text-anchor="middle" class="label">모든 프레임을 처리하지 않고 최신 결과와 안정적으로 유지된 안내만 화면에 반영</text>
"""
save("realtime-optimization.svg", wrap(optimization_body, "모바일 실시간 분석 주기와 최적화", "카메라·자세 검출·객체 검출·UI 갱신 주기를 분리", 8))

print("generated", 7, "SVG files in", OUT)
