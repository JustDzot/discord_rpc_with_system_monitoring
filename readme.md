![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

![CPU](https://img.shields.io/badge/CPU-Monitoring-blue)
![RAM](https://img.shields.io/badge/RAM-Monitoring-blue)
![Swap](https://img.shields.io/badge/Swap-Monitoring-blue)

# Discord RPC with System Monitoring

Мониторинг системных ресурсов с отображением в Discord статусе.
!(Системный мониторинг)[img/system_monitoring.jpg]

## Текущие возможности

### Отслеживаемые метрики:
- **CPU**: 
  - загрузка процессора (`cpu_percent`)
  - текущая частота процессора MHz (`cpu_freq_current`)
  - максимальная частота процессора (`cpu_freq_max`)
- **RAM**: 
  - процент использования (`memory_percent`)
  - использовано ГБ (`memory_used`)
  - всего ГБ (`memory_total`)
  - доступно ГБ (`memory_available`)
  - свободно ГБ (`memory_free`)
- **Swap**:
  - процент использования (`swap_percent`)
  - использовано ГБ (`swap_used`)
  - всего ГБ (`swap_total`)
  - свободно ГБ (`swap_free`)

## Настройка

### Файл `config/settings.json`:

```json
{
    "client_id": "YOUR_APPLICATION_CLIENT_ID_HERE",
    "update_interval": 5,
    "monitoring_1": "cpu_percent",
    "monitoring_2": "memory_percent",
    "monitoring_3": "memory_used", 
    "monitoring_4": "swap_percent"
}
```


# Примечания
  - Discord CLIENT ID можно получить на [Discord Developer Portal](https://discord.com/developers/applications)
  - Библиотеки: [pypresence](https://github.com/qwertyquerty/pypresence) и [psutil](https://github.com/giampaolo/psutil)
![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

# Ближайшие обновления:

- Автоматический реконнект к Discord — при потере соединения или ошибках программа будет автоматически переподключаться, чтобы статус не пропадал

- Графический интерфейс (GUI) — удобное окно с настройками, где можно:

  - Выбирать отображаемые параметры из выпадающих списков

  - Менять Client ID без редактирования файлов

  - Настраивать интервал обновления ползунком

  - Сохранять несколько профилей настроек

# В следующих версиях:

- Мониторинг дисков

    - Мониторинг GPU

    - Сетевой мониторинг

    - Более гибкая настройка отображения (порядок элементов, разделители)