# Python OOP Practice – Problems & Starter Kit

Sharpen your object‑oriented design skills in Python with small, focused exercises. Each problem emphasizes different OOP principles—inheritance, encapsulation, polymorphism, abstraction, and SOLID.

---

## Quick Start

1. **Requirements**: Python 3.10+ recommended.
2. **Create a virtual env**

   ```bash
   python -m venv .venv && source .venv/bin/activate   # on macOS/Linux
   # or
   .venv\Scripts\activate                              # on Windows
   ```
3. **Install dev tools (optional but recommended)**

   ```bash
   pip install -U pytest black ruff
   ```
4. **Run tests** (once you add them):

   ```bash
   pytest -q
   ```

---

## Repository Layout (suggested)

```
.
├── problems/
│   ├── problem_01_parking/
│   │   └── parking.py
│   ├── problem_02_cart/
│   │   └── cart.py
│   └── problem_03_notes/
        └── notes.py
└── README.md
```

> Feel free to rename files/modules. Keep the structure consistent so tests and examples are easy to find.

---

## How to Work Through the Problems

* **Read the problem** → **Sketch the design** → **Write tests** → **Implement** → **Refactor**.
* Use **type hints** and **docstrings** to make intent explicit.
* Prefer **composition over inheritance** unless inheritance cleanly models an "is‑a" relationship.
* Keep the **public API small** and hide internals (encapsulation).

---

## Problem 1 — Parking Fee System

**Goal**: Model a parking system with different vehicle types and a ticket that calculates total fee.

### Requirements

* Create a base class `Vehicle` with read‑only properties (e.g., `plate`, `base_fee`).
* Subclasses: `Car`, `Bike` (add more later).
* A `Gate` issues a `Ticket(entry_time, exit_time, vehicle)`.
* `Ticket.total_fee()` computes the amount due using the vehicle’s base fee and time parked.

  * Suggested rule: **ceiling** to whole hours; total = `vehicle.base_fee + hourly_rate * hours`.
  * Keep `hourly_rate` configurable (e.g., passed to `Ticket` or owned by `Gate`).
* Encapsulate times and fee calculation—don’t let external code mutate ticket internals.

### Why this tests OOP

* **Inheritance**: `Car` and `Bike` derive from `Vehicle`.
* **Polymorphism**: Different vehicles expose the same interface but different fees.
* **Encapsulation**: Ticket controls its own state and fee calculation.

### Example Usage (illustrative)

```python
from datetime import datetime, timedelta

car = Car(plate="ABC123", base_fee=5.0)
entry = datetime(2025, 1, 1, 8, 15)
exit_  = datetime(2025, 1, 1, 10, 02)

gate = Gate(hourly_rate=2.0)
ticket = gate.issue_ticket(vehicle=car, entry_time=entry)
ticket.close(exit_time=exit_)
print(ticket.total_fee())  # 5.0 + 2 * ceil(1.78h) = 5.0 + 2*2 = 9.0
```

> Design tip: keep `Ticket` immutable **after** closing (no changing exit time or vehicle).

---

## Problem 2 — Shopping Cart with Discount Rules

**Goal**: Apply discounts without modifying cart code (Open/Closed Principle).

### Requirements

* `Item(name, price, quantity=1)` and `ShoppingCart` with `add_item`, `subtotal`, and `total`.
* Define an abstract `DiscountRule` with `apply(cart) -> float` (returns **discount amount**, not price).
* Implement at least:

  * `PercentageDiscount(percent)` (e.g., 10% off entire order)
  * `BuyXGetYDiscount(item_name, buy_qty, free_qty)` (e.g., Buy 2 Get 1 on apples)
* `ShoppingCart` should accept a list of `DiscountRule` objects and compute total:

  * Default approach: `total = max(0, subtotal - sum(rule.apply(cart)))`.
  * Avoid cart knowing rule details.

### Why this tests OOP

* **Abstraction & Interfaces**: `DiscountRule` defines a contract.
* **Open/Closed Principle**: Add new discounts by adding new classes; **no cart changes**.
* **Polymorphism**: Cart treats all discounts uniformly via the interface.

### Example Usage (illustrative)

```python
cart = ShoppingCart()
cart.add_item(Item("apple", 1.00, quantity=3))
cart.add_item(Item("milk", 3.50, quantity=1))

rules = [
    PercentageDiscount(10),          # 10% off everything
    BuyXGetYDiscount("apple", 2, 1) # Buy 2 apples, get 1 free
]

print(cart.subtotal())  # 6.50
print(cart.total(rules)) # subtotal - sum(discounts)
```

> Decision note: If you want **sequential** discounting (each rule applied on the remaining amount), define `PriceRule` with `apply(cart, running_total) -> running_total` instead. Document your chosen strategy in code comments.

---

## Problem 3 — Versioned Notes

**Goal**: Store immutable notes with version history; expose only safe operations.

### Requirements

* `Note` is **immutable** (e.g., `@dataclass(frozen=True)`) with fields: `id`, `text`, `version`.
* `NoteBook` keeps an internal history per `note_id` but exposes APIs:

  * `add_note(note_id, text) -> Note` (version = 1)
  * `update_note(note_id, new_text) -> Note` (version += 1)
  * `get_latest(note_id) -> Note`
  * `get_history(note_id) -> tuple[Note, ...]` (return a **copy/tuple**, not the internal list)
* Users should not mutate stored notes or internal structures.

### Why this tests OOP

* **Immutability**: Once created, a `Note` instance never changes.
* **Encapsulation**: `NoteBook` hides its storage and returns safe views.
* **Version Control Logic**: Append‑only history; latest is easily retrievable.

### Example Usage (illustrative)

```python
nb = NoteBook()
nb.add_note("n1", "first")     # v1
nb.update_note("n1", "second")  # v2
latest = nb.get_latest("n1")
assert latest.version == 2
for n in nb.get_history("n1"):
    print(n.version, n.text)
```

> Safety tip: raise clear errors for unknown IDs; never return internal mutable lists.

---

## Coding Standards (recommended)

* **Type hints** everywhere; run `ruff` and `black` to keep code clean.
* **Docstrings** describing responsibilities and invariants.
* Prefer **properties** over public attributes when invariants matter.
* Keep functions **small**; single responsibility per class/method.

---

## Testing Hints

* Parking: parameterize tests over multiple vehicle types and durations (rounding edge cases).
* Cart: test stacking discounts, zero/negative totals, and unrelated items.
* Notes: test immutability (attempted mutation raises), history order, and unknown IDs.

Example `pytest` pattern:

```python
import pytest
from problems.problem_01_parking.parking import Car, Gate

@pytest.mark.parametrize("minutes, expected_hours", [(1,1),(59,1),(60,1),(61,2)])
def test_hour_ceiling(minutes, expected_hours):
    # ... construct ticket and assert fee uses expected_hours ...
    pass
```

---

## Adding More Problems

Duplicate `problems/problem_template` and update both the module and tests. Use this checklist:

* Clear **goal** and **OOP concepts** targeted.
* Public **API** sketch with types.
* **Edge cases** to test.
* A short **example usage**.

**Ideas**

* Library/Lending System (interfaces, composition)
* Plugin‑based Report Generator (Strategy, DIP)
* Task Scheduler (encapsulation, invariants)
* Bank Accounts with Transfers (polymorphism, transactional integrity)

---

## License

MIT (or your choice).
