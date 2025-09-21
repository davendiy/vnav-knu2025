
# Практичне заняття 3. Знайомство з ZeroMQ

Рекомендовані ресурси:
- https://zeromq.org/languages/python/
- https://zguide.zeromq.org/docs/chapter5/
- презентації Обвінцева по будові глобальних мереж і сокетах: https://github.com/krenevych/applied-programming/blob/main/%D0%A2%D0%B5%D0%BC%D0%B0%205.%20%D0%97%D0%B0%D0%B3%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%20%D0%B1%D1%83%D0%B4%D0%BE%D0%B2%D0%B0%20%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D1%85%20%D0%BC%D0%B5%D1%80%D0%B5%D0%B6/Pres_apcm_05.pdf
- презентації Обвінцева по паралельним обчисленням: https://github.com/krenevych/applied-programming/blob/main/%D0%A2%D0%B5%D0%BC%D0%B0%204.%20%D0%9F%D0%B0%D1%80%D0%B0%D0%BB%D0%B5%D0%BB%D1%8C%D0%BD%D1%96%20%D0%BE%D0%B1%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F/Pres_apcm_04.pdf
- приклади паралельних обчислень Обвінцева: https://github.com/krenevych/applied-programming/tree/main/%D0%A2%D0%B5%D0%BC%D0%B0%204.%20%D0%9F%D0%B0%D1%80%D0%B0%D0%BB%D0%B5%D0%BB%D1%8C%D0%BD%D1%96%20%D0%BE%D0%B1%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F


---


- Будем використовувати ZMQ
- є на всі мови
- можна пікльом надсилати
- проблеми з пікльом
- приклад з REQ-REP
- приклад з SUB-PUB
- особливості SUB-PUB сокетів
- приклад з використанням потоків в фоні


---

### Встановлення

Встановити треба через pip:
```bash 
pip install pyzmq 
```

https://zguide.zeromq.org/docs/chapter1/


## REQ-REP сокети

Далі типовий програма сервера ([example_server.py](./example_server.py)):

```python
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
  p = socket.recv_pyobj()
  print(p)
  socket.send_pyobj("pong")
```


І типова програма клієнта ([example_client.py](./example_client.py)):

```python
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
  socket.send_pyobj("ping")
  print(socket.recv_pyobj())
```

Спершу ми створюєм контекст `zmq.Context()`. Всередині цього
контексту мусять бути всі сокети, які ви юзаєте. Якщо контекст
закриється, то всі сокети викинуть помилку. Тому треба використовувати
глобальний контекст менеджер (про це трохи далі).

Сокети мають різні типи, тут ми використали REQ-REP шаблон підключення.

```python
socket = context.socket(zmq.REP)
```

REQ-REP означає request-responce. Цей тип підключення
корисний тоді, коли треба визначити якийсь конкретний порядок
роботи кількох програм.

- REQ-REP використовуєм тільки парою клієнт-сервер (1 клієнт і 1 сервер)
- REQ-REP гарантує, що повідомлення дійдуть до отримувача
- REQ-REP вимагає, щоб клієнт і сервер спілкувались по черзі. Якщо ж
хтось з них надішле два повідомлення підряд, то вилетить помилка.
- в REQ-REP хтось один має забіндитись, а хтось інший приєднатись:
```python
# server.py
socket.bind("tcp://*5555")

# client.py
socket.connect("tcp://*5555")
```
- біндиться зазвичай сервер, а клієнт приєднується (насправді можна й навпаки)
- в даному випадку ми використали tcp порт 5555, хоча могли й будь-який інший.
Порт -- це просто якесь число, зазвичай не більш як 4-значне. Головне, щоб
ваш порт ніяка інша програма вже не використовувала, тому обирайте якесь рандомне.
- в лінуксі можна використати так звані `ipc` (Inter Process Communication) сокети --
спеціальні сокети, які придумали для спілкування різних програм друг з другом. Ми
будемо їх далі використовувати, приклад ([./pub_linux.py](./pub_linux.py)):
```python
socket.bind("ipc://@example.socket")  
```
- кайф zmq в тому, що приєднуватись можна однаково як і з локальної машини
(тобто на тому самому компʼютері) через `localhost:5555`, так і десь з інтернету, якщо
відома ip-адреса. Приклад: нехай у нас є разбері, яка працює в тій самій
мережі, що й компʼютер з ip адресою `192.168.0.111`. Нехай на ній працює [example_server.py](./example_server.py),
який ми розглядали вище. Тоді з компʼютера можна приєднатись до неї через
```python
socket.connect("tcp://192.168.0.111:5555")
```
