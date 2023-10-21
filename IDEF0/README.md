## Test 4
<code>
+----------------------------------+
|            FastAPI Server        |
+----------------------------------+
| - model: YOLO                    |
| - database: SQL                  |
+----------------------------------+
| + detect_potholes(image: Image)  |
| + store_detection(result: JSON)  |
+----------------------------------+
                  |
                  |
                  | API Calls
                  |
                  v
+----------------------------------+
|        Telegram Bot Client       |
+----------------------------------+
| - api_client: FastAPI API Client |
| - chat_id: int                   |
+----------------------------------+
| + receive_image()                |
| + send_result()                  |
+----------------------------------+
</code>


## Test 3
```mermaid
classDiagram
    class FastAPIServer {
        -model: YOLO
        -database: SQL
        +detect_potholes(image: Image)
        +store_detection(result: JSON)
    }
    class TelegramBotClient {
        -api_client: FastAPI API Client
        -chat_id: int
        +receive_image()
        +send_result()
    }
    FastAPIServer --|> TelegramBotClient: API Calls
```


## Test 2

```mermaid
classDiagram
    FastAPIServer --|> YOLOModel : Uses
    TelegramBot --|> FastAPIServer : Sends Requests
    YOLOModel : +predictPotholes(image)
    FastAPIServer : +getPotholes(image)
    FastAPIServer : +respondWithLocations()
    TelegramBot : +sendMessage()
    TelegramBot : +receiveMessage()
    class YOLOModel{
        +loadModel()
        +predict(image)
    }
    class FastAPIServer{
        +processImage(image)
        +handleRequest(request)
    }
    class TelegramBot{
        +startBot()
        +sendReport()
    }
```

## Test 1

```mermaid
graph TD;
  A0[Recognition of road defects using YOLO]
  K1[Standards for a specific country] --> A0
  K2[Performance KPI] --> A0
  K3[Accuracy score] --> A0
  K4[Requirements for data labeling] --> A0
  Image[Image/Video data] --> A0
  
  A1[Data Preprocessing] --> A0
  A2[YOLO Model Training] --> A0
  A3[Model Testing & Evaluation] --> A0
  
  R1[Dataset with road images] --> A1
  R2[Annotated Bounding Boxes] --> A1
  
  R3[Preprocessed Data] --> A2
  R4[YOLO Base Model] --> A2
  R5[Hardware GPU/CPU] --> A2
  
  R6[Trained YOLO Model] --> A3
  R7[Test Data] --> A3
  
  M1[Data Augmentation Tools] --> A1
  M2[Model Optimization Tools] --> A2
  M3[Evaluation Metrics] --> A3
```

---


## Test0

```mermaid
graph TD;
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
