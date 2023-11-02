## YOLOv8 Project in the form of SPARQL-like rules:

### 1. Class-Class Rules:
```
If ind belongs to class RoadImage:
Then ind belongs to class ProcessedData

If ind belongs to class DetectedPothole:
Then ind belongs to class RoadHazard

If ind belongs to class NeuralModelParameters:
Then ind belongs to class SystemKPI
```

### 2. Class-Property Rules:
```
If ind belongs to class DetectedPothole:
Then ind has areaValue of property DetectedArea

If ind belongs to class NeuralModelParameters:
Then ind has accuracyValue of property ModelAccuracy

If ind belongs to class NeuralModelParameters:
Then ind has modelName of property YOLO

If ind belongs to class FastAPI:
Then ind has serverFunctionality of property BackendFunctionality

If ind belongs to class TelegramBot:
Then ind has userInterface of property ClientUI
```

### 3. Property-Class Rules:
```
If ind has areaValue > 0.9 of property DetectedArea:
Then ind belongs to class CriticalPothole

If ind has accuracyValue > 0.95 of property ModelAccuracy:
Then ind belongs to class HighAccuracyModel
```

### 4. Property-Property Rules:
```
If ind has areaValue > 0.9 of property DetectedArea:
Then ind has criticalAlert of property HazardAlert

If ind has accuracyValue < 0.8 of property ModelAccuracy:
Then ind has tuningRecommendation of property ModelTuningAdvice
```

### 5. Property-Property Rules (Different Subjects):
```
If RoadImage has property DetectedPothole:
Then TelegramBot sends UserAlert

If NeuralModelParameters has accuracyValue < 0.8 of property ModelAccuracy:
Then FastAPI logs PerformanceIssue

If DetectedPothole has areaValue > 0.9 of property DetectedArea:
Then TelegramBot sends CriticalHazardAlert
```

This knowledge base is tailored to the specifics of the project, where the system processes road images to detect potholes, uses a neural model (YOLO) with certain accuracy parameters, and integrates with FastAPI and a Telegram Bot for user interaction.


---

## Example

![image](https://github.com/DmPanf/UML-DIA/assets/99917230/cd68bdf0-29ef-4a52-b62b-ee29e3b49926)
