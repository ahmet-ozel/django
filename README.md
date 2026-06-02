# Web ERP — Multi-Tenant Meeting & CRM Platform

[![Django](https://img.shields.io/badge/Django-REST-092E20?logo=django&logoColor=white)](https://www.djangoproject.com)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React-17-61DAFB?logo=react&logoColor=black)](https://react.dev)
[![Material UI](https://img.shields.io/badge/Material--UI-4-0081CB?logo=mui&logoColor=white)](https://mui.com)
[![Webpack](https://img.shields.io/badge/Webpack-5-8DD6F9?logo=webpack&logoColor=black)](https://webpack.js.org)

A multi-tenant meeting management and customer relationship (CRM) application built with Django and React. Each company manages its own users and contacts, meeting records are stored, and analysis results tied to meetings (such as emotion, age and gender predictions) are persisted in the database.

> Note: This is a learning/portfolio project. It shows how a Django REST backend can be combined with a React frontend (bundled via webpack) in a single project.

## Features

- Multi-tenant structure — each `Company` owns its own users and data
- Custom user model (`CustomUser`) built on `AbstractUser` with a custom `UserManager`
- Person (`Person`) and meeting (`Meeting`) management
- Storage of meeting analysis results (`MeetingDescription`: emotion, age, gender, accuracy score)
- Data management through the Django admin panel
- Single-page (SPA) interface with React + Material-UI, bundled with webpack

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django, Django REST Framework |
| Frontend | React 17, Material-UI 4, React Router, Axios |
| Build | Webpack 5, Babel |
| Database | SQLite (development) |

## Project Structure

```
web_erp/
├── manage.py
├── web_erp/          # Django project settings (settings, urls, wsgi)
├── api/              # REST API app — models, views, migrations
│   ├── models.py     # Company, CustomUser, Person, Meeting, MeetingDescription
│   ├── views.py
│   └── urls.py
└── frontend/         # React app (bundled with webpack)
    ├── src/          # React components
    ├── static/       # Compiled output (main.js)
    ├── package.json
    └── webpack.config.js
```

## Setup

### Backend

```bash
cd web_erp
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

pip install django djangorestframework
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The app runs at `http://127.0.0.1:8000` by default.

### Frontend

```bash
cd web_erp/frontend
npm install

# Development (watches file changes)
npm run dev

# Production build
npm run build
```

`npm run dev` runs webpack in watch mode and compiles the React source into `static/frontend/main.js`, which Django serves through a template.

## Data Model (overview)

- **Company** — Company information (subscription date, phone, etc.)
- **CustomUser** — Custom user model tied to a company
- **Person** — A person attending a meeting
- **Meeting** — Meeting record linking company, user and person
- **MeetingDescription** — Meeting analysis results (emotion, age, gender, accuracy)

## License

This is a learning project shared for educational/portfolio use.
