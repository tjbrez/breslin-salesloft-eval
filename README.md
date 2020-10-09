# Breslin SalesLoft Eval

This application is part of a coding evalution for SalesLoft engineering. It's a small Django + React project that conducts some basic interactions with the SalesLoft API. 

## Demo
Live demo running at: https://breslin-salesloft-eval.herokuapp.com/

## Development

### Prerequisites
- Python 3.8
- NPM (Node package manager)
- Poetry (Python package manager)

### Running
```
npm run build
poetry shell
python manage.py runserver
```

*Note: You'll need to run the frontend app seperately with `npm start` if you want frontend hot-reloading*

### Testing
```
poetry shell
python manage.py test
```

### Code Styling
- Auto-formatted by Black
- Linting by Flake8