import  openpyxl  as  op  #openpyxl 모듈 import

def get_title():
    wb = op.load_workbook(r"20220915214411.xlsx") #워크북 객체 생성(파일명 : test.xlsx)
    ws = wb.active  #활성화 되어있는 시트 설정(시트명 : "업")
    for i in range(1, 101):
        print(i)

get_title()