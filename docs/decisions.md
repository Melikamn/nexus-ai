# Architecture Decisions

This document records significant architectural decisions made throughout the development of Nexus AI.

---

# ADR-001

## Title

Use FastAPI as the Backend Framework

## Status

Accepted

## Context

The backend requires a modern Python framework with high performance, asynchronous support, automatic API documentation, and strong type safety.

## Decision

FastAPI has been selected as the primary backend framework.

## Rationale

- High performance
- Excellent documentation
- Built-in OpenAPI support
- Native async support
- Type hints
- Large community

---

# ADR-002

## Title

Use PostgreSQL as the Primary Database

## Status

Accepted

## Context

The application requires a reliable relational database capable of handling structured data and future scalability.

## Decision

PostgreSQL has been selected.

## Rationale

- ACID compliance
- Reliability
- Scalability
- Excellent indexing
- Mature ecosystem

---

# ADR-003

## Title

Adopt Clean Architecture

## Status

Accepted

## Context

The project is expected to grow into a production SaaS platform.

## Decision

Separate business logic from infrastructure using layered architecture.

## Rationale

- Easier maintenance
- Better testing
- Loose coupling
- Scalability
- Clear responsibilities
