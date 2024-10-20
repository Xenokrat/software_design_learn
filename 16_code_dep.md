# Знание кода 1

## Пример 1

```java
class Animal {
    public void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

class Cat extends Animal {
    // Переопределение метода makeSound
    public void makeSound() {
        System.out.println("Meow");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myCat = new Cat();
        myCat.makeSound();  // "Meow"
    }
}

// Но если

class Animal {
    // Изменен метод в суперклассе
    public void makeGenericSound() {
        System.out.println("Some generic animal sound");
    }
}
```

В первом случае класс `Cat` переопределяет метод `makeSound` класса `Animal`
и корректно выводится сообщение `Meow` в main.
Однако так как мы создаём `myCat` как объект класса `Animal`, то мы зависим от
его интерфейса.
Поэтому во втором случае мы получим ошибку, так как класс `Animal` не предоставляет
наме метода `makeSound`, поэтому код выведет ошибку.

## Пример 2

```java
class Animal {
    public void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

class Cat extends Animal {
    @Override
    public void makeSound(int numberOfSounds) {
        for (int i = 0; i < numberOfSounds; i++) {
            System.out.println("Meow");
        }
    }
    
    @Override
    public void makeSound() {
        System.out.println("Meow");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal cat = new Cat();
        cat.makeSound();
        cat.makeSound(3);
    }
}
```

И снова, класс `Cat` зависит от интерфейса класса `Animal`.
Потому что класс `Animal` предоставляет интерфейс только для 
метода `makeSound` БЕЗ аргумента `numberOfSounds`, то при
вызове `makeSound(3)` код упадёт с ошибкой, потому что мы обращаемся к `cat`
как к `Animal`.

## Пример 3

```java
/*
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.9.10</version>
</dependency>
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version>
</dependency>
*/

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // Создаем объект ObjectMapper для парсинга JSON
        ObjectMapper objectMapper = new ObjectMapper();

        String jsonString = "{\"name\":\"John\", \"age\":30}";

        try {
            // Парсим JSON-строку в HashMap
            Map<String, Object> result = objectMapper.readValue(jsonString, HashMap.class);

            System.out.println("Name: " + result.get("name"));
        } catch (IOException e) {
            // Обработка ошибки парсинга
            e.printStackTrace();
        }

        try {
            String prettyJson = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(result);
            System.out.println("Pretty JSON: " + prettyJson);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

Данный код зависит от 
- Внешней библиотеки `FastXML`, которая устанавливается отдельно.
- От реализации стандартной библиотеки (`Map`, `HashMap`)
- От методов объекта fastxml `objectMapper` 
(`readValue`, `writerWithDefaultPrettyPrinter`, `writeValueAsString`)
- От передачи данных между
  - String строкой в объект `Map` методами `objectMapper`
  - Обратно в String строку из `Map` также через методы `objectMapper`.
