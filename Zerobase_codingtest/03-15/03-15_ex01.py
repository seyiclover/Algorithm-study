<정답 코드 >
def solution(cards):
    """
    :param cards: int[]
    :return: int
    """

    while len(cards) > 1:
        # 정렬
        cards.sort()
        battle(cards)

    return cards[0] if len(cards) == 1 else 0


def battle(cards):
    # 정렬된 배열에서 가장 큰 2개의 값을 제외해주고 변수로 저장해준다. 
    life1 = cards.pop()
    life2 = cards.pop()
    
    # 가장 큰 두 개의 값의 차이를 저장한다. 
    leftLife = abs(life1 - life2)

    # 남은 카드 추가
    if leftLife > 0: cards.append(leftLife)
