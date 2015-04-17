# basic-wms
Basic Warehouse Management System built with Python on Flask

### Current State
The first version of database model and CRUD methods are finished.

### The Idea

The idea is to write a WMS with a strict modular and tierlike structure and with clearly defined interfaces; all of this within the MVC paradigm. The following tiers are planned:

- Backend
  - (SQL) Database
  - (Python/Flask-SQLAlchemy)
    - Database Model
    - CRUD interface defined independently of the database itself (this way SQL database can be interchanged with another persistent data-collection)
  - (Python/Flask) Controller for managing routing, RESTful methods and business logic
  - (Python/Flask) Views for managing the system (may be abandoned for the sake of REST + AngularJS)
  
- Frontend
  - (JavaScript/jQuery) Interactive client-side layer (possibly AngularJS in the future)
