import pyautogui


    # 시작 좌표와 끝 좌표를 입력받음
start_x, start_y = pyautogui.position(4285,100)
end_x, end_y = pyautogui.position(7240,2075)

# 시작 좌표와 끝 좌표로 스크린샷을 찍음
screenshot = pyautogui.screenshot(
    region=(start_x, start_y, end_x-start_x, end_y-start_y))

# 이미지 파일 이름에 사용될 번호 초기화
num = 1

# 이미지 파일 이름에 사용될 경로 설정
path = "C:/Users/User/Desktop/scan"

# 무한 반복
check = 0
while check<2:
    # 이미지 파일 이름 설정
    filename = path + "screenshot" + str(num) + ".png"

    # 이미지 파일 저장
    screenshot.save(filename)

    # 번호 증가
    num += 1

    # 클릭할 위치 입력받음
    click_x, click_y = pyautogui.position(7625, 1085)

    # 클릭할 위치로 마우스 이동
    pyautogui.moveTo(click_x, click_y)

    # 클릭
    pyautogui.click()

    check +=1