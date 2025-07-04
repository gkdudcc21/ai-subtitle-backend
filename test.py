## 파일 실행 폴더 생성
##==============================================
import os
# print('subtitle 폴더 생성(추가) 시작')

# output_dir = './source/subtitle'
# os.makedirs(output_dir, exist_ok=True)

# print('subtitle 폴더 생성(추가) 완료')

# # output_path = output_dir + '/test.txt'
# output_path = os.path.join(output_dir,'test.txt' )
# print(output_path)

## segments를 test.json 저장
# output_path = os.path.join(output_dir,'segments')

## =======================================================
from datetime import timedelta

'''
* 초 단위 시간을 SRT 형식 (HH:MM:SS,mmm)으로 변환
* datetime.timedelta() 
    : float 초 반환
    : 내부적으로 days, seconds, microseconds 등을 관리
    : ex) 3662.567초 -> 0 days, 1hour, 1 minute, 2 seconds + 567 milliseconds
'''
seconds = 3662.567


## 1:01:02.567000 로바뀜
td = timedelta(seconds=seconds)
print('td >> ',td)

'''
* 전체 초를 3660(1시간)으로 나눠 '시간'만 추출
* // 는 나눗셈 후 소수점 버림
'''

## 원래상태로 돌아옴
hours = td.total_seconds()

# hours = td.total_seconds() / 3600  ## 1.0173797222222223
# hours = td.total_seconds() // 3600 ## 1.0
hours = int(td.total_seconds() // 3600) ## 시 1
# print(hours)

'''
* 전체 초에서 시간 부분을 뺀 나머지 -> 366.567 % 3600 = 62.567
* 이 중 60으로 나눈 몫 =  1분
'''
# minutes = td.total_seconds() % 3600 ## minutes >>  62.56700000000001
minutes = int((td.total_seconds() % 3600) // 60) ## minutes >>  1
print('minutes >> ',minutes)

'''
* 전체 초에서 60으로 나눈 나머지 = '초'만 추출
'''
# seconds = td.total_seconds() % 60 ## 2.5670000000000073
seconds = int(td.total_seconds() % 60) ## 2
print('second>> ',seconds)

'''
* 소수점 아래 (1초미만) 부분 추출: -> 밀리초로 변환
* 3662.567 % 1 = 0.567 -> 0.567 * 1000 = 567
* milliseconds
'''

milliseconds = int((td.total_seconds() % 1) * 1000) ## 567
print('milliseconds >> ',milliseconds)

result = f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"
print(result)

