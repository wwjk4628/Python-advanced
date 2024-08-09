import sys


def sys_module():
    # argv 속성: 명령행에서 넘어온 인수
    print(sys.argv)




def regexp_ex():
    """
    정규표현식 예제
    """
    import re


    namecard = """
    Email: hong@hwalbin.org
    Phone: 010-1234-5678
    
    Email: gildong@dooly.net
    Phone: 010-1234-5812
    
    Email: qwert@example.com
    Phone: 010-1246-7167
    """
    emaillist = re.findall(r"\w+[\w\.]*@\w+[\w\.]\.[a-z]+", namecard)
    print(emaillist)

    phonelist = re.findall(r"[0-9]{3}-[0-9]{4}-[0-9]{4}", namecard)
    print(phonelist)


def random_ex():
    import random

    random.seed()

    print(random.random())  # 0 ~ 1의 난수
    print(random.randint(1, 6))  # 1 ~ 6사이 정수 난수
    print(random.randrange(101))  # 0 ~ 100 사이의 난수
    print(random.randrange(1, 101, 3))  # 1 ~ 100 사이의 3간격 수 중에서 난수

    seqvar = ["짬뽕", "짜장면", "짬짜면", "마라탕"]
    print("seqvar:", seqvar)
    random.shuffle(seqvar)
    print("shuffle:", seqvar)
    print(random.choice(seqvar))

    # 샘플링
    for i in range(5):
        print(random.sample(range(1, 101), 10))
    print(random.sample(range(1, 46), 6))

if __name__ == "__main__":
    # sys_module()
    # regexp_ex()
    random_ex()