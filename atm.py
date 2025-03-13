receipts = []

# 원금을 담는 변수
balance = 3000

while True:
    num = input("사용하실 기능의 번호를 입력해주세요(1.입금, 2.출금, 3.영수증 보기, 4.종료): ")

    if num == "1":
        deposit_amount = input("입금할 금액을 입력해주세요: ")
        if deposit_amount.isdigit() and int(deposit_amount) > 0:
            balance += int(deposit_amount)
            print(f"고객님이 입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원입니다.")

            #영수증에 데이터 넣기
            receipts.append(["입금",deposit_amount, balance])
        else:
            print("정신차리고, 제대로된 숫자형태로 입금금액을 작성해줘!!!")  
    if num == "2":
        withdraw_amount = input("출금할 금액을 입력하세요")
        if withdraw_amount.isdigit() and int(withdraw_amount) > 0:
            withdraw_amount = min(balance, int(withdraw_amount))
            balance - withdraw_amount
            print(f"고객님이 출금한 금액은 {withdraw_amount}원이고, 현재 잔액은{balance}원 입니다.")

            #영수증에 데이터 넣기
            receipts.append(["출금",withdraw_amount, balance])
    if num == "3":
        if receipts:
            print("====영수증====")
            for i in receipts:
                print(f"{i[0]} : {i[1]}원 |잔액 {i[2]}원")
        else:
            print("야... 영수증에 아무내역도 없습니다.")
    if num == "4":
        print("서비스를 종료합니다.")
        break