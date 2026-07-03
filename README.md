# DecodeLabs Project 3: Database Integration

This repository contains the third milestone of the DecodeLabs Industrial Training Program (Batch 2026). The objective of this phase is to establish **Data Longevity** by engineering a secure digital vault. It bridges the gap between backend application logic and permanent storage using Django's Object-Relational Mapping (ORM).

## 🗄️ The Architecture
This persistence layer transitions the application from temporary variables to a reliable database structure. It demonstrates mastery of state operations (CRUD), schema design, and strict data integrity enforcement.

## 🛡️ Core Engineering Principles
* **Relational Geometry:** Implements a structured **One-to-Many (1:Many)** relationship connecting `Customer` entities to their respective `Order` records.
* **The Final Source of Truth:** Enforces data integrity directly at the schema level using database constraints such as `UNIQUE` and `NOT NULL`. The database never trusts the application logic blindly.
* **Autonomic Defense:** Protects the system against SQL Injection attacks. By utilizing Django's native ORM methods, all user inputs are automatically treated as harmless data via **Parameterized Queries**, never as executable logic.
* **RESTful CRUD Mapping:** Database actions are strictly mapped to their corresponding HTTP methods (CREATE = POST, READ = GET, UPDATE = PUT, DELETE = DELETE).

## 📖 API Blueprint (Database Endpoints)

### 1. Retrieve Customers (READ)
* **Endpoint:** `/customers/` (All) or `/customers/<id>/` (Specific)
* **Method:** `GET`
* **Description:** Retrieves customer records from the database.
* **Success Response:** `200 OK`

### 2. Create a Customer (CREATE)
* **Endpoint:** `/customers/`
* **Method:** `POST`
* **Description:** Inserts a new customer record into the vault.
* **Request Body:**
  ```json
  {
    "name": "Jane Doe",
    "email": "jane@example.com"
  }
