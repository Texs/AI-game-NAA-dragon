# AI-game-NAA-dragon
CI/CD project - Mathematical Operations Library

This project demonstrates a comprehensive CI/CD setup with automated testing for both JavaScript and Python applications. It provides basic arithmetic functions with input validation and extensive test coverage.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Input validation with appropriate error handling
- Comprehensive test coverage for both JavaScript and Python implementations
- CI/CD integration for automated testing

## Project Structure

```
├── app.js          # JavaScript implementation
├── app.py          # Python implementation  
├── test.js         # JavaScript tests
├── test.py         # Python tests
├── package.json    # Node.js configuration
├── .eslintrc.json  # JavaScript linting configuration
├── CONTRIBUTING.md # Contribution guidelines
└── README.md       # This file
```

## Setup Instructions

### Prerequisites
- Node.js (v14 or higher)
- Python (v3.6 or higher)

### Installation
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies (if any): `npm install`

## Usage

### Running JavaScript Tests
```bash
npm test
```

### Running Python Tests
```bash
python test.py
```

Or using npm script:
```bash
npm run test:py
```

### Using the Library

#### JavaScript
```javascript
const { sum, subtract, multiply, divide } = require('./app');

console.log(sum(2, 3));      // 5
console.log(divide(10, 2));  // 5
```

#### Python
```python
from app import sum, subtract, multiply, divide

print(sum(2, 3))      # 5
print(divide(10, 2))  # 5.0
```

## Contributing

# AI-game-NAA-dragon
CI/CD project
Часть 2: Настройка GitHub Actions и GitLab CI – первый workflow и деплой

В первой статье мы разобрались с основами CI/CD: что это такое, зачем нужно и какие инструменты существуют. Теперь пришло время перейти от теории к практике – создадим наши первые рабочие CI/CD-конвейеры на GitHub Actions и GitLab CI.

Вот небольшая карта для навигации между частями:

Часть 1: Основы CI/CD – что это и зачем нужно; GitHub Actions и GitLab CI

Часть 2: Настройка GitHub Actions и GitLab CI – первый workflow и деплой

^ Вы сейчас здесь ^

Часть3: CI/CD – ветки, условия, секреты и окружения

Терминология
В мире CI/CD используется множество специфических терминов. Вот краткий словарик, который поможет вам лучше понимать документацию и обсуждения:

Workflow – сценарий автоматизации, описанный в YAML-файле на GitHub Actions.

Job – отдельная задача в workflow или pipeline, которая выполняется на одном runner-е.

Runner – виртуальная машина или контейнер, на котором исполняются задачи.

Step – отдельный шаг внутри job-а, например, команда или action.

YAML – формат файла, используемый для описания workflow и pipeline. Отступы в нём критически важны!

Script – раздел с командами в GitLab CI-файле.

Action – готовое действие на GitHub, которое можно использовать в своих workflow, например, actions/checkout.

Stage – этап pipeline в GitLab, например, build, test, deploy.

Artifact – файл или набор файлов, созданный во время выполнения job-а и сохранённый для использования в других job-ах или для скачивания.

Environment – среда, в которую выполняется деплой, например, staging или production.

Не переживайте, если сразу не запомните все термины – они станут понятнее по мере практики.

Итоги
В этой статье мы:

Создали репозитории на GitHub и GitLab.

Настроили первые workflow и pipeline.

Автоматизировали деплой статического сайта.

Добавили автоматические тесты.

Построили полноценный CI/CD-конвейер, который проверяет и публикует код при каждом изменении.

Теперь при каждом пуше в ветку main автоматически выполняются тесты, и если они проходят успешно, сайт обновляется. Команде больше не нужно вручную запускать проверку – теперь ошибки видны сразу, а деплой происходит автоматически.

Это только начало вашего путешествия в мир CI/CD. В следующей статье мы рассмотрим более сложные сценарии: работу с разными ветками, условное выполнение шагов, использование секретов для безопасного хранения чувствительных данных и лучшие практики настройки CI/CD для реальных проектов.

А пока – экспериментируйте с тем, что вы узнали сегодня. Добавьте больше тестов, попробуйте другие actions, настройте деплой для своего проекта. Практика – лучший способ закрепить знания.

До встречи в следующей статье!

Теги:
github actions
gitlab-ci
cic
devops
automation
Хабы:DevOpsGitHubPythonJavaScript
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License.
