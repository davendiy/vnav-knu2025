
# Практичне заняття 2. Знайомство з логами Ardupilot


Рекомендовані ресурси: 
- https://mavlink.io/en/
- https://mavlink.io/en/mavgen_python/
- онлайн тулза для аналізу логів: https://plot.ardupilot.org/#/
- дока з ардупайлота по аналізу логів: https://ardupilot.org/copter/docs/common-downloading-and-analyzing-data-logs-in-mission-planner.html
- відос 12-річної давнини по аналіу логів: https://www.youtube.com/watch?v=62TmGiwFiDU&t=6s
- MAVExplorer: https://ardupilot.org/dev/docs/using-mavexplorer-for-log-analysis.html
- дока з ардупайлота по вібраціях: https://ardupilot.org/copter/docs/common-measuring-vibration.html


---

Найпростіше аналізувати логи через https://plot.ardupilot.org/#/ або напряму працювати з csv файлами.

Встановити `pymavlink` можна через `pip`: 

```bash
pip install pymavlink
```

тоді у вас зʼявиться такий сприптік

```bash
mavlogdump.py --help
```

В основному будем використовувати експорт в csv файл: 

```bash
mavlogdump.py --types=ATT --format=csv 01-wo-visp.bin > output.csv
```

Щоб подивитись всі можливі типи, які можна експортувати (використовуємо sort, щоб по алфавіту вивело): 
```bash
mavlogdump.py --show-types 01-wo-visp.bin | sort
```


