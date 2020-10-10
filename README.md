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
1. Create a `backend/.env` file for passing your environment variables into the app. There is a `sample.env` file that can be used as a template.

2. Build the React app:
```
npm run build
```

3. Build and run the Django app:
```
poetry shell
poetry install
python manage.py runserver
```

4. The app will be running at http://127.0.0.1:8000

5. Optionally, you can also run the the React app with `npm start` (app will be running at http://127.0.0.1:3000).
This will allow you to make updates to the React app with hot-reloading instead of having to re-build the app
after every change.

### Testing
There are django unit tests for services and API endpoints. These can be run with:
```
poetry shell
python manage.py test
```

There are also some frontend jest unit tests for testing React component rendering. These can be run with:
```
npm test
```

### Code Styling
- Auto-formatted by Black
- Linting by Flake8