import requests
import time
from utils.logs import logger
from utils.session import create_session

class Faucet:
    def __init__(self, token, address, proxy=None):
        self.token = token  # 2Captcha API ключ
        self.address = address
        self.taskId = ""
        self.captcha = ""

        self.acc_name = f"{self.address[:5]}..{self.address[-5:]}"
        self.session = create_session(proxy)

    def create_task(self):
        logger.info(f"{self.acc_name} создаем задачу для решения капчи..")

        # Отправляем задачу на 2Captcha
        resp = requests.post("http://2captcha.com/in.php", data={
            "key": self.token,
            "method": "turnstile",  # Изменен на turnstile для Cloudflare
            "sitekey": "0x4AAAAAAARdAuciFArKhVwt",  # Ваш siteKey
            "pageurl": "https://bartio.faucet.berachain.com/"  # URL страницы
        })

        if resp.status_code == 200 and "OK|" in resp.text:
            self.taskId = resp.text.split('|')[1]
            logger.info(f"{self.acc_name} задача на решение капчи создана {self.taskId}..")
        else:
            logger.error(f"{self.acc_name} ошибка создания задачи: {resp.text}")

    def task_status(self):
        for i in range(15):
            try:
                time.sleep(5)  # Ждем 5 секунд

                # Проверяем статус задачи
                resp = requests.get("http://2captcha.com/res.php", params={
                    "key": self.token,
                    "action": "get",
                    "id": self.taskId
                })

                if resp.text == "CAPCHA_NOT_READY":
                    logger.info(f"{self.acc_name} капча еще не решена, повторяю попытку..")
                    continue
                elif "OK|" in resp.text:
                    self.captcha = resp.text.split('|')[1]
                    logger.info(f"{self.acc_name} капча решена")
                    return True
                else:
                    logger.error(f"{self.acc_name} ошибка решения капчи: {resp.text}")
                    return False
            except Exception as e:
                logger.error(f"{self.acc_name} {self.taskId} {e}")

        return False

    def get_token(self):
        # Получаем токен от сервера с использованием решения капчи
        self.session.headers["Authorization"] = f"Bearer {self.captcha}"
        resp = self.session.post(f"https://bartiofaucet.berachain.com/api/claim?address={self.address}", json={"address": self.address})

        status_code = resp.status_code
        if status_code == 200:
            logger.success(f"{self.acc_name} получили токены BERA")
            return True
        elif status_code == 429:
            logger.info(f"{self.acc_name} получение токенов на перезарядке")
        elif status_code == 402:
            logger.info(f"{self.acc_name} на балансе менее 0.001 ETH")

        return False

    def faucet(self):
        while True:
            self.create_task()  # Создаём задачу на решение капчи
            if self.task_status():  # Проверяем статус задачи
                break

        return self.get_token()  # Получаем токен
