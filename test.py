import random
import logging

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def create_random_str(Number=127):
    """
    随机生成验证码
    :param Number: 需要生成的长度
    :return: 返回验证码
    """
    random_list = ["大","小","等"]
    random_Le = ""
    count = 0
    while True:
        random_Letter = random.sample(random_list,1)
        for Letter in random_Letter:
            random_Le+=Letter
            count+=1
        if count == Number:
            break
    # random_str = random_Letter + str(random.randint(0, 9))
    print(random_Le)
    print(len(random_Le))
    logger.info(random_Le)

create_random_str()
