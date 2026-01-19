# Greyhound Dashboard

Greyhound Dashboard is a Django-based monitoring and control panel designed to manage and visualise multiple self-hosted services from a single unified interface.

It provides a service registry, live status views, and enhanced metadata from supported platforms such as Navidrome, Portainer, Vikunja and other API-driven services. The architecture is intentionally extensible through pluggable service modules, allowing new integrations to be added easily.

![Dashboard Screenshot](images/dashboard.png)

---

## Features

- Service registry for multiple platforms  
- Enhanced service data (e.g. media activity, task metrics, service health)  
- Dynamic UI powered by HTMX  
- Django admin integration for service management  
- Modular service plugin architecture  
- Designed for self-hosted environments  

---

## Project Structure

```
greyhoundDashboard/
    core/
        admin.py
        models.py
        views.py
        services/
        static/
        templates/
    services/
        basic_services.py
        service_base.py
        navidrome/
        portainer/
        vikunja/
    tests/
    manage.py
    db.sqlite3
    greyhoundDashboard/
        settings.py
        urls.py
        wsgi.py
requirements.txt
readme.md
```


---

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- virtualenv (recommended)

---

### Installation

```bash
git clone git@github.com:JTSG1/GreyhoundDash.git
cd GreyhoundDash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```