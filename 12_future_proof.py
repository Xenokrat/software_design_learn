import tomllib
import sys
from datetime import datetime, timedelta, date
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def do_report(template: str, report_date_start: date, report_date_end: date) -> None:
    """
    Логика создания отчета
    """
    print(f"""
        Report Used:
        date_start: {report_date_start}
        date_end: {report_date_end}
        template: {template}
    """)

def set_and_do_report() -> None:
    try:
        with open("config.toml", "rb") as f:
            config = tomllib.load(f)
    except FileNotFoundError:
        logger.error("Config file not found")
        sys.exit(-1)

    # Используем дефолтные значения, если их вдруг не оказалось в конфиге
    default_template   = "file://some/path/to/report"
    default_date_start = datetime.now() - timedelta(days=2)
    default_date_end   = datetime.now() - timedelta(days=1)

    # Получаем значения из конфига
    # Таким образом, бы готовы к изменениям по пути расположения данных в отчёте, благодаря возможности настраивать их в файле-конфиге.
    report_date_start: date = config.get("report_date_start", default_date_start)
    report_date_end:   date = config.get("report_date_end", default_date_end)
    template:          str  = config.get("report_file_path_template", default_template)
    logger.info(f"Used start date: {report_date_start}")
    logger.info(f"Used end date: {report_date_end}")

    # Запускаем формирование отчёта
    do_report(template, report_date_start, report_date_end)


if __name__ == "__main__":
    set_and_do_report()
