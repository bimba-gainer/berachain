# === BERACHAIN 1.2 ===

### Функционал бота:  
- Получение токенов через [кран](https://bartio.faucet.berachain.com/)  
- [Свап](https://bartio.bex.berachain.com/swap) BERA на HONEY и WBERA  
- Добавление в [пулл](https://bartio.bex.berachain.com/add-liquidity/0xd28d852cbcc68dcec922f6d5c7a8185dbaa104b7)  
- [Стейкинг](https://bartio.station.berachain.com/gauge) HONEY-WBERA  
- Клейм [BGT](https://bartio.station.berachain.com/gauge)
- Просмотр баланса BGT

### Параметры:  
- Случайные задержки между действиями  
- Случайные задержки между стейкингом

### Установка для WINDOWS:  
- Устанавливаете python 3.11.9  
- Запускаете файл setup.bat

### Установка для MAC:
- Устанавливаем зависимости `pip install requirements.txt`
- Запускаем `python main.py`

### config.py 
- добавляем API-token для решения капчи https://www.2captcha.com

### Запуск:  
- В файле data>private_keys.txt указываете приватные ключи.  
- В файле data>proxies.txt указываете прокси. Первый ключ соответствует первому прокси в списке, второй к второму и тд. Если ключей больше чем прокси, то прокси пойдут по кругу.  
- Запускать бота файлом start.bat  

сказать спасибо за софт сюда [![Telegram](https://img.shields.io/badge/-Telegram-090909?style=for-the-badge&logo=telegram&logoColor=27A0D9&color=02223b)](https://t.me/next_softs)
