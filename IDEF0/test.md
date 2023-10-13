## Test1

``` graph TD;
    subgraph A0[Распознавание объектов на дороге с помощью YOLO]
        subgraph A1[Ввод данных]
            video[Видеопоток с камеры] -->|Видеоданные| preprocessing[Предобработка данных]
        end
        
        subgraph A2[Обработка данных]
            preprocessing -->|Предобработанные данные| analysis[Анализ данных]
        end
        
        subgraph A3[Анализ данных]
            analysis -->|Результаты анализа| postprocessing[Постобработка данных]
        end
        
        subgraph A4[Вывод результатов]
            postprocessing -->|Распознанные объекты| output[Выходные данные]
        end
    end
```
