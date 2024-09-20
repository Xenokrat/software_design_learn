"""
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DateExample {
    public static void main(String[] args) {
        String dateString = "2024-05-13 14:30:00";
        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        try {
            Date date = format.parse(dateString);
            System.out.println("Date: " + date);
        } catch (ParseException e) {
            e.printStackTrace();
        }
    }
}
"""
# Изначальный код
from datetime import datetime

class DateExample:

    @staticmethod
    def main() -> None:
        date_string: str = "2024-05-13 14:30:00"
        format: str = "yyyy-MM-dd HH:mm:ss"
        try:
            date = datetime.strptime(date_string, format)
            print(f"Date: {date}")
        except ValueError as e:
            print(e)

# Потенциальные проблемы
# 0. Из того, что пишут про import java.util.Date; - это будто бы устаревшее API и нужно использовать java.time, но тут не могу быть уверен
#    также java.util.Date не thread-safe, но в питоновской datetime такой проблемы нет.
# 1. Возможно, не учитываем таймзоны, для фикса можно использовать pytz
# 2. Код довольно хрупкий с точки зрения того, что можно получить другой формат даты (корректный) и он все равно выдаст исключение, потому что форматирование
#    отличается. Потенциально можно исправить библиотекой dateutil
import pytz
from dateutil import parser

class DateExampleFix:

    @staticmethod
    def main() -> None:
        date_string: str = "2024-05-13 14:30:00"
        format: str = "%Y-%m-%d %H:%M:%S"
        timezone = pytz.timezone(zone='UTC')
        try:
            date = datetime.strptime(date_string, format)
            # Добавили эксплицитно таймзону
            date = timezone.localize(date)
            # Альтернативный вариант с использованием dateutil
            date_dateutil = parser.parse(date_string)
            print(f"Date: {date}")
            print(f"Date (dateutil): {date_dateutil}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    date_example_fix = DateExampleFix()
    date_example_fix.main()
