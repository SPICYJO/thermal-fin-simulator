# thermal-fin-simulator

## 만든 이유
기계공학실험 보고서를 쓰다가 만들게 되었다...

## 구현 방식
- settings.py : 실험 조건 값, 해석 조건 설정
- main.py : 실행 파일
- fin_conf.py : 핀 설정 파일, I/O 담당
- solve.py : 수치해석 수행
- plot.py : 화면 표시 담당

## 설치 방식
- python 설치
- pip install -r requirement.txt

## 실행 방법
- settings.py 파일에서 원하는 조건값, 해석조건 입력
- python main.py로 프로그램 실행
- 조작 키에 따라 캔버스에서 원하는 동작 수행

## 조작 키
- 키보드로 r 입력시, 직사각형 그리기 모드
- 키보드로 l 입력시, 선 그리기 모드
- 그리기 모드에서 마우스로 그리기 <br /><br />

- 선 그리기 모드 상에서, 키보드로 + 입력시, 두께 증가
- 선 그리기 모드 상에서, 키보드로 - 입력시, 두께 감소 <br /><br />

- 키보드로 f 입력시, 그리기의 결과 -> fin
- 키보드로 b 입력시, 그리기의 결과 -> base
- 키보드로 a 입력시, 그리기의 결과 -> ambient <br /><br />

- 키보드로 q 입력시, 다시 핀 디자인하기 <br /><br />

- 키보드로 s 입력시, steady-state 분석 후, 화면에 표시
- 키보드로 t 입력시, transient 분석 후, 화면에 애니메이션으로 표시
- 분석을 다 한 뒤, 화면에 표시하기 때문에, s나 t 입력 후에는 잠시 기다려야함 <br /><br />

## 실행 결과
![demo.gif](https://github.com/SPICYJO/thermal-fin-simulator/blob/mechlab2/demo/thermal_fin_simulator_demo.gif)
위 gif는 transient 분석을 수행하는 모습이다.

## TODO
- solve 시, 계산 성능 개선 요망 ㅠㅠ
- transient로 많은 시간프레임에 대해 분석 시, 메모리 부족 현상 해결 요망
