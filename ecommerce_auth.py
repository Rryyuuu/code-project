'''
로그인 후 해당 유저가 가진 예산 안에서
모자 2개, 원피스1개, 귀걸이 1개 을 하는 알고리즘을 짜라

- 상품 리스트 존재 (모자, 신발, 상의, 하의, 원피스, 목걸이, 귀걸이)
- 상품을 구매할 시 해당 가격만큼 현금에서 차감됨
- 할인쿠폰은 5,000원
- 할인쿠폰은 목걸이와 귀걸이에만 적용 됨
- 같은 물품을 여러개 주문해야 할 경우 같은이름을 원하는 갯수만큼 입력해야 함
-------------------------------------------------------------
- input 은 아이디, 비밀번호, 살려고 하는 물품목록
- return 은 남은 금액
'''

accountList = [
    ['test1', '1234', 100000],
    ['test2', '12345', 50000],
    ['test3', '123456', 30000],
]
catalogList = {
    'Hat': 2000,
    'Shoes': 1000,
    'Top': 6000,
    'Bottom': 3000,
    'Dress': 4000,
    'Necklace': 9000,
    'Rings': 10000,
}

def getPrice(basketItem):
    if basketItem not in catalogList:
        return 0

    price = catalogList[basketItem]
    if basketItem == 'Necklace' or basketItem == 'Rings':
        price -= 5000

    return price

def signIn():
    username = input('아이디를 입력해 주세요: ')

    selectedAccount = None
    for accoount in accountList:
        if username == accoount[0]:
            selectedAccount = accoount
            break
    if selectedAccount == None:
        print('존재하지 않는 아이디 입니다.')
        return None

    password = input('비밀번호를 입력해 주세요: ')
    if password != selectedAccount[1]:
        print('비밀번호를 다시 확인해 주세요.')
        return None

    return selectedAccount[2] 

def main(budget, basketList):
    totalPrice = 0
    for basketItem in basketList:
        totalPrice += getPrice(basketItem)

    if totalPrice > budget:
        print('예산이 부족합니다.')
        return
    
    print('물품 구입이 완료되었습니다.')
    print('남은 잔액은 {} 원입니다.'.format(str(budget - totalPrice)))

if __name__ == '__main__':
    budget = signIn()
    if budget != None:
        basketList = list(map(str, input('구입할려는 상품을 입력하세요: ').split()))
        main(budget, basketList)
