# Спринт 11/19 → Тема 5/8: Библиотека pytest → Урок 1/6
# Бэкенд на Django
## 26. Библиотека pytest
### 1. Библиотека pytest. Выборочный запуск тестов

### Note:: Выборочный запуск тестов

Для выборочного запуска в pytest применяется такой синтаксис:
```
pytest file_name.py::TestClassName::test_method_name
```
```
pytest file_name.py
```

```
pytest file_name.py::TestClassName
```

```
pytest test_example.py::test_fail
```

```
pytest test_example.py::test_fail test_example.py::test_correct
```

```
pytest pytest_trial
```

```
pytest pytest_trial/test_example.py
```