# Selenium Python Automation Framework

## About
End-to-end test automation framework built with Selenium and Python
using Page Object Model design pattern, targeting AutomationExercise.com.

## Tech Stack
| Tool | Purpose |
|------|---------|
| Python 3.13 | Programming language |
| Selenium 4 | Browser automation |
| Pytest | Test framework |
| WebDriver Manager | Automatic ChromeDriver management |
| pytest-html | HTML report generation |

## Test Coverage
| Test File | Scenario | Status |
|-----------|----------|--------|
| test_01_login.py | Valid user login | ✅ Pass |
| test_01_login.py | Invalid credentials error | ✅ Pass |
| test_02_search.py | Add product to cart | ✅ Pass |
| test_03_register.py | New user registration | ✅ Pass |
| test_04_contact_us.py | Contact form submission | ✅ Pass |

## Project Structure

```
selenium_portfolio/
│
├── pages/
│   ├── base_page.py        # Parent class — reusable Selenium methods
│   ├── login_page.py       # Login page locators and actions
│   ├── account_page.py     # Account page verification
│   ├── home_page.py        # Product search and cart actions
│   ├── register_page.py    # Two-stage registration flow
│   ├── account_created.py  # Registration success verification
│   └── contact_us_page.py  # Contact form actions
│
├── tests/
│   ├── test_01_login.py
│   ├── test_02_search.py
│   ├── test_03_register_user.py
│   └── test_04_contact_us_page.py
│
├── conftest.py             # Browser fixture — setup and teardown
├── pytest.ini              # Pytest configuration and report settings
└── requirements.txt        # Project dependencies
```
## Framework Design Decisions

**Page Object Model** — Each page is a class containing locators
and action methods. Tests contain only user journey and assertions.
No locators or Selenium commands exist in test files.

**BasePage** — Parent class inherited by all page classes.
Contains reusable methods like click(), type_text(), get_text(),
is_visible(), js_click(). Centralises explicit waits so no
test ever uses raw find_element.

**Page Chaining** — Page methods return the next page object
after completing an action. login() returns AccountPage so
tests can chain actions across pages seamlessly.

**conftest.py** — Browser setup and teardown in one place.
Handles consent popup automatically before every test.

## How To Run

### Clone the repository
```bash
git clone https://github.com/shrutibhedasgaonkar/selenium-portfolio.git
cd selenium-portfolio
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/test_01_login.py -v
```

### Run with visible report
```bash
pytest --html=reports/report.html
```

## Key Challenges Solved

**Ad iframe interception** — Google Ad iframes intercepted
clicks on product buttons. Solved using JavaScript execution
which bypasses the visual layer and interacts with the DOM directly.

**Hover-dependent elements** — Add to Cart buttons only appear
on hover. Solved using ActionChains to simulate mouse hover
before clicking.

**Whitespace normalisation** — Product names had inconsistent
spacing. Solved using split() and join() to normalise all
whitespace before string comparison.

**Consent popup handling** — Site shows consent popup on load.
Handled automatically in conftest.py before every test runs.

## Author
Shruti Bhedasgaonkar
QA and Test Manager | Automation Engineer
[LinkedIn](https://www.linkedin.com/in/shruti-bhedasgaonkar)
