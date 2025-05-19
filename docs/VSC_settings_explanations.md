

**Настройки проекта в VSC**
=====================================

### cSpell.words

Список слов, которые не будут подсвечены как ошибки орфографии.

```json
"cSpell.words": [
    "blogapp",
    "endcomment",
    "endfor",
    "firstof",
    "forloop",
    "mysite",
    "promocode",
    "Pupkina",
    "shopapp"
],
```

### files.associations

Соответствие файлов и языков программирования. В данном случае, все файлы `.html` в папках `templates` будут восприниматься как файлы Django-шаблонов.

```json
"files.associations": {
    "**/templates/**/*.html": "django-html",
    "**/blogapp/templates/**/*.html": "django-html"
},
```

### emmet.includeLanguages и emmet.triggerExpansionOnTab

Настройки Emmet для автоматического завершения кода. В данном случае, Emmet будет включен для языков HTML и Django-шаблонов, и будет активирован при нажатии клавиши Tab.

```json
"emmet.includeLanguages": {
    "django-html": "html"
},
"emmet.triggerExpansionOnTab": true,
```

### python.languageServer и python.defaultInterpreterPath

Настройки языкового сервера Python. В данном случае, используется Pylance, и путь к интерпретатору Python указан явно.

```json
"python.languageServer": "Pylance",
"python.defaultInterpreterPath": "/home/uservm/PycharmProjects/Django_repo_shop/shop_env_py_3_12/bin/python",
```

### python.analysis.extraPaths и python.autoComplete.extraPaths

Дополнительные пути для анализа и автодополнения кода Python.

```json
"python.analysis.extraPaths": [
    "/home/uservm/PycharmProjects/Django_repo_shop/shop_env_py_3_12/lib/python3.12/site-packages"
],
"python.autoComplete.extraPaths": [
    "/home/uservm/PycharmProjects/Django_repo_shop/shop_env_py_3_12/lib/python3.12/site-packages"
],
```

### python.analysis.autoImportCompletions и python.analysis.autoSearchPaths

Включение автоматических импортов и поиска путей для анализа кода Python.

```json
"python.analysis.autoImportCompletions": true,
"python.analysis.autoSearchPaths": true,
```

### [html] и [django-html]

Настройки редактора для HTML и Django-шаблонов. В данном случае, табуляция установлена в 2 пробела, и включено вставка пробелов вместо табуляции.

```json
"[html]": {
    "editor.tabSize": 2,
    "editor.insertSpaces": true
},
"[django-html]": {
    "editor.tabSize": 2,
    "editor.insertSpaces": true
},
```

### python.analysis.completeFunctionParens и python.analysis.useLibraryCodeForTypes

Включение подсказок для Pylance и использование библиотечного кода для типов.

```json
"python.analysis.completeFunctionParens": true,
"python.analysis.useLibraryCodeForTypes": true,
```

### editor.quickSuggestions

Включение быстрых подсказок для редактора.

```json
"editor.quickSuggestions": {
    "other": true,
    "comments": true,
    "strings": true
}
```