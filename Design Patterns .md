# 📘 Design Patterns — Training Handout

---

## 🧠 What Are Design Patterns?

> “Design patterns are **reusable solutions** to commonly occurring problems in software design.”

They capture expert knowledge in reusable forms that:

* Improve code quality
* Foster communication
* Support maintainability

### 🔍 Why Use Them?

* Reduce design effort
* Promote consistency across projects
* Improve readability and extensibility
* Encode best practices

---

## 📢 What Message Do Patterns Convey?

| Message                           | Interpretation                                       |
| --------------------------------- | ---------------------------------------------------- |
| You’re not alone                  | The problem has been solved before                   |
| Think in structure                | Patterns are blueprints for modularity               |
| Design is about trade-offs        | Patterns clarify consequences of choices             |
| Shape architecture through design | Micro-design decisions affect system-level structure |

---

## 🤩 Categories (Gang of Four - GoF)

| Type       | Example Patterns                      | What They Do                            |
| ---------- | ------------------------------------- | --------------------------------------- |
| Creational | Singleton, Factory Method, Builder    | Control object creation                 |
| Structural | Adapter, Facade, Composite, Decorator | Define relationships between components |
| Behavioral | Observer, Strategy, Command, State    | Define communication between objects    |

---

## 🏢 Component Patterns (Beyond GoF)

Component patterns describe how to structure and relate **independent, reusable modules** in a system. These are especially relevant in **modular architectures**, **plugin systems**, and **distributed services**.

### Examples:

| Pattern              | Description                                         | Use Case Example                       |
| -------------------- | --------------------------------------------------- | -------------------------------------- |
| Microkernel (Plugin) | Core system with pluggable components               | IDE with language support plugins      |
| Proxy Component      | Intercepts calls to add behavior or redirection     | Security/authentication wrappers       |
| Component Container  | Manages component lifecycle and dependencies        | Dependency Injection frameworks        |
| Service Registry     | Discover and bind components at runtime             | Service Locator in distributed systems |
| Mediator Component   | Central coordination between independent components | UI controls communication              |

> Component patterns help **scale design patterns to systems-level modularity**.

---

## 📊 Patterns vs Principles

> **Principles guide design**, **patterns implement it**.

| Principle             | Example Pattern                   |
| --------------------- | --------------------------------- |
| Single Responsibility | Strategy, Chain of Responsibility |
| Open/Closed           | Decorator, Factory Method         |
| Dependency Inversion  | Adapter, Bridge                   |
| Liskov Substitution   | Template Method, State            |

---

## 🧠 Thinking in Patterns

### ✅ Don't Start with Patterns

1. **Understand the real problem**
2. **Apply core design principles (e.g., SOLID)**
3. **Let patterns emerge through refactoring**

### 🛝 Problem → Pattern Mapping

| Design Problem                       | Suggested Pattern        |
| ------------------------------------ | ------------------------ |
| Need interchangeable behavior        | Strategy                 |
| Want to hide complex object creation | Factory Method / Builder |
| Interface mismatch between systems   | Adapter                  |
| Undo/Redo functionality              | Command                  |
| Notify others of changes             | Observer                 |

---

## 📚 Can You Use Patterns Just by Reading?

> Reading ≠ Mastery

| Reading Helps With     | Reading Fails at                |
| ---------------------- | ------------------------------- |
| Understanding concepts | Knowing when/how to apply them  |
| Vocabulary             | Adapting to real-world problems |

### 🏋️ Practice is Key:

* Implement patterns manually
* Refactor toward patterns
* Solve real design challenges

---

## ↺ Evolving Design Patterns

### 🌱 When Patterns Should Appear:

* Duplication and conditional complexity
* Low testability
* Tight coupling
* Repeating boilerplate

### 🛠️ Steps to Evolve:

1. Keep design simple
2. Identify hot spots during changes
3. Refactor toward appropriate patterns
4. Avoid overengineering

---

## 🏗️ Evolving Architectural Patterns (GoF Foundation)

> “Architecture is patterns at scale.”

### From Design to Architecture:

| GoF Patterns Used  | Emergent Architectural Style      |
| ------------------ | --------------------------------- |
| Factory + Command  | Plugin / Microkernel Architecture |
| Adapter + Strategy | Hexagonal / Ports & Adapters      |
| Mediator + Facade  | Layered Architecture              |

### Principles Behind the Evolution:

* Encapsulation of change
* Dependency direction management
* Interface separation
* Component decoupling

---

## ✅ Quick Tips for Effective Pattern Use

| Do                               | Avoid                            |
| -------------------------------- | -------------------------------- |
| Use patterns as tools, not goals | Blindly applying every pattern   |
| Refactor toward a pattern        | Designing with pattern obsession |
| Keep the context in focus        | Using patterns out of context    |
| Explain *why*, not just *what*   | Copy-pasting pattern examples    |

---

## 🧠 Final Thoughts

> **"Think in principles. Let patterns emerge."**

Design patterns:

* Help build robust systems
* Are best learned through **implementation and reflection**
* Evolve over time as **your design matures**

---

## 📃 Suggested Reading

* **GoF – Design Patterns**
* **Martin Fowler – Refactoring**
* **Shalloway & Trott – Design Patterns Explained**
* **POSA – Pattern-Oriented Software Architecture**
