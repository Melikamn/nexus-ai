# Architecture

## Overview

Nexus AI follows a layered architecture inspired by Clean Architecture principles.
The goal is to separate responsibilities, improve maintainability, and make the system scalable and testable as it grows.

---

## Layers

### Presentation Layer

The Presentation Layer is responsible for handling HTTP requests and responses.
It exposes REST APIs through FastAPI and communicates with the Application Layer.

Responsibilities:

- Receive client requests
- Validate input
- Return HTTP responses
- Route requests to services

---

### Application Layer

The Application Layer contains the business use cases of the system.

Responsibilities:

- Execute business logic
- Coordinate workflows
- Validate business rules
- Communicate with repositories

---

### Domain Layer

The Domain Layer contains the core business models and rules.

Responsibilities:

- Business entities
- Domain rules
- Core business logic
- Independent from frameworks

---

### Infrastructure Layer

The Infrastructure Layer handles communication with external systems.

Responsibilities:

- Database
- External APIs
- AI Providers
- File Storage
- Cache

---

## Dependency Flow

Dependencies always point inward.

```text
Presentation
      │
Application
      │
Domain
      │
Infrastructure
```

The Domain Layer must never depend on frameworks or external services.

---

## Backend Request Flow

```text
Client
    │
FastAPI
    │
API Layer
    │
Service Layer
    │
Repository Layer
    │
PostgreSQL
```

---

## Planned Backend Structure

```text
backend/
└── app/
    ├── api/
    ├── core/
    ├── models/
    ├── repositories/
    ├── schemas/
    ├── services/
    ├── utils/
    └── main.py
```

---

## Benefits

- Clear separation of concerns
- Easier testing
- Better maintainability
- Scalable architecture
- Framework-independent business logic
- Cleaner codebase
