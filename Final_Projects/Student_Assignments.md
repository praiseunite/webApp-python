# 🎓 Final Capstone Projects — Application Based Programming in Python

> **This is your most important piece of work for this course.**
> It is not just a coding exercise — it is a real software product with a real business behind it.
> Build something you are proud to show an employer, an investor, or a client.

---

## 🏗️ The Golden Rule — One Feature at a Time

> **"Never build Feature 2 until Feature 1 is working and tested."**

Every student MUST follow this development methodology throughout the project:

1. **Plan the feature** — write in a comment block what it should do.
2. **Build only that feature** — do not touch other parts of the code.
3. **Test it manually** — confirm it works as expected with real data.
4. **Commit it** — save your progress (`git add . && git commit -m "feat: add [feature name]"`).
5. **Then** — move to the next feature.

This mirrors how professional software teams work (Agile sprints). **Projects that show evidence of this approach (via git commit history or feature log) will receive bonus marks.**

---

## 📋 What Your Project MUST Include

Every project, regardless of the assigned topic, must deliver ALL of the following layers:

### 🔧 Layer 1 — Technical Requirements

| # | Requirement | Tool |
|---|---|---|
| 1 | **Data Collection:** Scrape live data from the web | `requests`, `BeautifulSoup` |
| 2 | **Storage:** Persist all scraped data in a database | `MySQL` + `mysql-connector-python` |
| 3 | **Data Engineering:** Load, clean, and transform data | `Pandas` |
| 4 | **ML Preparation:** Apply at least one preprocessing step | `Scikit-Learn` (`StandardScaler`, `LabelEncoder`, `SimpleImputer`, etc.) |
| 5 | **Visualisation:** At least two meaningful charts | `Matplotlib` / `Seaborn` |
| 6 | **User Interface:** A working frontend for the user | `Flask` (web) or `Tkinter` (desktop) |

### 💼 Layer 2 — Business Requirements *(Mandatory)*

Your project is not just code — it is a **product**. You must include a `BUSINESS_PLAN.md` file in your project folder that answers the following:

#### Section A — The Problem
- What real-world problem does your app solve?
- Who suffers from this problem today? (your target users)
- How are people currently solving it, and why is that not good enough?

#### Section B — Your Solution
- What exactly does your app do to solve this problem?
- What is your **Unique Value Proposition (UVP)** — the one sentence that explains why someone would choose YOUR app?

#### Section C — Business Model (How You Make Money)

You must choose **at least one** monetisation model and explain how it works for your specific product:

| Model | Description | Example |
|---|---|---|
| **Subscription (SaaS)** | Users pay monthly/yearly for access | ₦2,500/month for premium features |
| **Freemium** | Basic free, premium features paid | Free: 5 listings/day. Pro: Unlimited |
| **Transaction Fee** | Take a % of each deal made via the app | 2.5% commission on every booking |
| **Pay-Per-Report** | Users pay for each export or detailed report | ₦500 per PDF market analysis report |
| **Advertising** | Show relevant ads to free users | Display job ads to job seekers |
| **Data Licensing** | Sell aggregated/anonymised data to companies | Sell pricing trends to real estate firms |
| **Lead Generation** | Connect buyers and sellers, charge the seller | ₦5,000 per qualified lead sent to an agent |

#### Section D — Revenue Projections *(Basic)*
Make a simple estimate:
- If you had **100 paying users** at your chosen price, how much monthly revenue would you earn?
- What would you need to spend to run the service (server costs, domain, etc.)?
- At what number of users do you **break even**?

#### Section E — Go-to-Market Strategy
- How will you get your first 10 users?
- What channels will you use? (Social media, WhatsApp groups, university campuses, cold emails?)
- Who is one specific company or organisation you could partner with?

---

## 🌟 Bonus Marks — "More Ideas" Scheme

The base project earns you up to **70 marks**. The remaining **30 marks** are **bonus marks** for extra ideas and features. **The more ideas you implement, the higher you score.**

| Bonus Idea | Marks |
|---|---|
| A working **user login / registration** system (Flask sessions or Tkinter auth) | +5 |
| **Email or WhatsApp alert** when a threshold is met (e.g., price drop, flight delay) | +5 |
| **PDF/CSV export** of data or a report generated from within the app | +5 |
| A real **Machine Learning prediction** (trained model that outputs a useful result) | +8 |
| **Git commit history** showing one-feature-at-a-time methodology (min. 8 commits) | +4 |
| A **second data source** scraped and merged with the first | +5 |
| A mobile-responsive Flask design OR polished Tkinter UI with colours and icons | +3 |
| Deploying the Flask app **live online** (PythonAnywhere, Render, or Railway) | +8 |
| **Third-party API integration** (WhatsApp API, currency API, weather API, etc.) | +6 |
| A proper **README.md** with screenshots and installation instructions | +3 |

> ⚠️ **You cannot exceed 100 marks total.** Pick bonus features that genuinely improve your product.

---

## 📊 Marking Rubric

| Area | Marks |
|---|---|
| Data Collection (scraper works, stores data correctly) | 15 |
| Database Design (proper schema, queries work) | 10 |
| Data Cleaning & Engineering (Pandas used correctly) | 10 |
| ML Preprocessing (at least one technique applied correctly) | 5 |
| Visualisations (2 meaningful, well-labelled charts) | 10 |
| Frontend / UI (functional, user can interact with data) | 10 |
| Business Plan (`BUSINESS_PLAN.md` — all 5 sections complete) | 10 |
| **Total Base Marks** | **70** |
| **Bonus Marks** (see table above) | up to +30 |
| **Maximum** | **100** |

---

## 📁 Required Project Folder Structure

```
YourName_FinalProject/
│
├── BUSINESS_PLAN.md          ← Your full business plan (Sections A-E)
├── README.md                 ← How to install and run your project
├── requirements.txt          ← pip freeze > requirements.txt
│
├── scraper.py                ← Web scraping script
├── database.py               ← MySQL connection & table creation
├── data_processing.py        ← Pandas cleaning & ML preprocessing
├── visualisations.py         ← Chart generation functions
│
├── app.py                    ← Flask app OR Tkinter main app
├── templates/                ← (Flask only) HTML templates
│   └── index.html
├── static/                   ← (Flask only) CSS, JS, images
│
└── feature_log.md            ← Your one-feature-at-a-time build log
```

---

## 🗓️ Submission Format

- **Submit:** A link to your **GitHub repository** (public or shared with instructor).
- **Demonstrate:** A 5–10 minute live demo of your running application.
- **Present:** A 2-minute business pitch to the class — *imagine you are presenting to investors.*

---

## 👩‍💻 Assigned Projects

| # | Code / Student | Project Title | Domain |
|---|---|---|---|
| 1 | **VE** | Real Estate Price Predictor & Analyzer | Real Estate |
| 2 | **AA** | E-Commerce Price Drop Tracker | E-Commerce |
| 3 | **VI** | Job Market Skill Analyzer | Employment/Careers |
| 4 | **VO** | Cryptocurrency Market Monitor | Finance |
| 5 | **UP** | Movie Review & Rating System | Entertainment |
| 6 | **RC** | Flight & Weather Correlation Hub | Travel & Logistics |
| 7 | **ME** | Sports Player Statistics Aggregator | Sports |
| 8 | **IDEABASI** | Local Business Discovery & Review Aggregator | Local Commerce |
| 9 | **IDONG** | Student Tutoring Marketplace & Session Tracker | EdTech |

---

### 1. VE — Real Estate Price Predictor & Analyzer
- **Domain:** Real Estate
- **Data Source:** Scrape property listings (Title, Location, Number of Beds/Baths, Price).
- **Backend:** Store properties in MySQL.
- **Frontend:** Build a **Flask Web App** showing a dashboard of current listings.
- **Data & ML:** Use Pandas to clean prices (remove currency symbols/commas). Use `StandardScaler` on the price and beds.
- **Visualization:** Create a Scatter Plot of Beds vs. Price, and a Bar Chart of average price per Location.

**💡 Business Starter Ideas:**
- Charge estate agents ₦10,000/month to list their properties as "Featured" at the top.
- Charge buyers ₦1,500 per PDF report on a property's fair market value vs. listed price.

---

### 2. AA — E-Commerce Price Drop Tracker
- **Domain:** E-Commerce
- **Data Source:** Scrape a product catalog (Product Name, Current Price, Original Price, Rating).
- **Backend:** Store products in MySQL.
- **Frontend:** Build a **Tkinter Desktop App** where users can view the products in a Treeview.
- **Data & ML:** Use Pandas to calculate the "Discount Percentage". Use `SimpleImputer` to fill missing ratings.
- **Visualization:** Create a Histogram of product ratings, and a Bar chart of the top 5 highest-discounted products.

**💡 Business Starter Ideas:**
- Offer a ₦500/month WhatsApp/email alert whenever a tracked product drops in price.
- Earn 3-5% affiliate commission on every purchase made through the app.

---

### 3. VI — Job Market Skill Analyzer
- **Domain:** Employment/Careers
- **Data Source:** Scrape job postings (Job Title, Company, Location, Required Skills).
- **Backend:** Store job postings in MySQL.
- **Frontend:** Build a **Flask Web App** to search for jobs by title.
- **Data & ML:** Use Pandas to explode/split the Required Skills column. Use `OneHotEncoder` or dummy variables on Location.
- **Visualization:** Create a Bar Chart of the Top 10 most demanded skills, and a Pie Chart of job distributions by Location.

**💡 Business Starter Ideas:**
- Sell a ₦2,000 "CV Audit" feature that highlights missing high-demand skills on a job seeker's CV.
- Sell aggregated skill trend reports to HR agencies for ₦50,000/month.

---

### 4. VO — Cryptocurrency Market Monitor
- **Domain:** Finance
- **Data Source:** Scrape live crypto data (Coin Name, Price, 24h Change, Market Cap).
- **Backend:** Store coins in MySQL.
- **Frontend:** Build a **Tkinter Desktop Dashboard** with a "Refresh Data" button.
- **Data & ML:** Use Pandas to convert Market Cap from strings (e.g., "1.5B") to actual numbers. Use `StandardScaler` on Price and Market Cap.
- **Visualization:** Create a Line Plot comparing the 24h changes of the top 5 coins.

**💡 Business Starter Ideas:**
- Pro Trader Subscription (₦5,000/month) for SMS alerts, 30-day historical charts, and portfolio tracking.
- Sell automated buy/sell signal alerts for ₦3,000/month.

---

### 5. UP — Movie Review & Rating System
- **Domain:** Entertainment
- **Data Source:** Scrape movie data (Movie Title, Genre, Release Year, User Rating).
- **Backend:** Store movies in MySQL.
- **Frontend:** Build a **Flask Web App** allowing users to filter movies by Genre.
- **Data & ML:** Use Pandas to drop movies with missing ratings. Use `LabelEncoder` on the Genre column.
- **Visualization:** Create a Box Plot of User Ratings grouped by Genre, and a Line Plot of average rating by Release Year.

**💡 Business Starter Ideas:**
- Charge studios ₦50,000/month to feature Nollywood movies as "Promoted" picks.
- Cine-Pass (₦1,500/month) for weekly curated watchlists sent via WhatsApp.

---

### 6. RC — Flight & Weather Correlation Hub
- **Domain:** Travel & Logistics
- **Data Source:** Scrape airport departures (Flight Number, Destination, Status/Delay) AND current weather (Temperature, Condition).
- **Backend:** Store both flights and weather in MySQL.
- **Frontend:** Build a **Flask Web App** displaying a live flight board.
- **Data & ML:** Use Pandas to merge flights and weather based on time/location. Use `LabelEncoder` on Weather Condition.
- **Visualization:** Create a Bar Chart showing average delay time per Weather Condition.

**💡 Business Starter Ideas:**
- Travel Agent Pro (₦15,000/month) with unlimited tracking and client PDF export.
- Traveller Flight Delay Risk Alert (₦800/month).

---

### 7. ME — Sports Player Statistics Aggregator
- **Domain:** Sports
- **Data Source:** Scrape player stats (Player Name, Team, Points/Goals, Age, Games Played).
- **Backend:** Store player stats in MySQL.
- **Frontend:** Build a **Tkinter GUI** where users can select a Team from a dropdown to view its players.
- **Data & ML:** Use Pandas to calculate "Points per Game". Handle missing Age values using `SimpleImputer`.
- **Visualization:** Create a Scatter Plot of Age vs. Points per Game to analyze peak performance years.

**💡 Business Starter Ideas:**
- Automated Scout Reports (₦20,000/month) for football academies and coaches.
- Match predictions for fantasy league players at ₦500/week.

---

### 8. IDEABASI — Local Business Discovery & Review Aggregator
- **Domain:** Local Commerce
- **Data Source:** Scrape local business listings (Business Name, Category, Address, Rating, Review Count, Phone).
- **Backend:** Store businesses and reviews in MySQL.
- **Frontend:** Build a **Flask Web App** to browse businesses by Category and City with review breakdown.
- **Data & ML:** Clean ratings with Pandas. Apply `LabelEncoder` on Category. Use `KMeans` to cluster businesses into performance tiers.
- **Visualization:** Bar Chart of average rating per Category, Scatter Chart of Rating vs. Review Count.

**💡 Business Starter Ideas:**
- Free listings for all businesses to drive initial adoption.
- Verified Business Badge (₦3,000/month) to respond to reviews and upload photos.
- Pay-per-lead (₦500 per customer call/WhatsApp click).
- Business Analytics Dashboard (₦8,000/month).

---

### 9. IDONG — Student Tutoring Marketplace & Session Tracker
- **Domain:** EdTech / Education
- **Data Source:** Scrape tutor listings (Tutor Name, Subject, University, Hourly Rate, Rating, Availability).
- **Backend:** Store tutors, sessions, and bookings in MySQL.
- **Frontend:** Build a **Flask Web App** allowing students to search tutors and book sessions.
- **Data & ML:** Clean hourly rates with Pandas. Use `StandardScaler` on Rate and Rating. Train Logistic Regression to predict tutor 5-star review probability.
- **Visualization:** Scatter Plot of Hourly Rate vs. Rating, Bar Chart of top requested subjects.

**💡 Business Starter Ideas:**
- Free for students to search and book.
- 15% commission on every booked tutoring session.
- Tutor Pro Badge (₦2,500/month) for top search placement + group sessions.
- White-label university license for ₦500,000/year.

---

## 📝 `BUSINESS_PLAN.md` Template

Copy this template into your project folder and fill in every section:

```markdown
# Business Plan — [Your App Name]
**Student / Code:** [Your Name / Code]
**Date:** [Submission Date]

## A. The Problem
- **Problem Statement:** [1-2 sentences]
- **Who is affected:** [Your target users]
- **Current solutions & their flaws:** [How people cope today and why it fails]

## B. Your Solution
- **What your app does:** [Clear description]
- **Unique Value Proposition:**
  "For [target user] who [has the problem], [App Name] is a [product type]
   that [key benefit], unlike [alternatives] which [fall short]."

## C. Business Model — How We Make Money
- **Primary Model:** [e.g., Subscription / Freemium / Commission]
- **Price Point:** [e.g., N3,000/month per business]
- **Why users will pay:** [What value justifies the price?]
- **Secondary Revenue Stream:** [Any additional income source]

## D. Revenue Projections
| Scenario        | Users | Monthly Revenue | Monthly Costs | Profit |
|-----------------|-------|-----------------|---------------|--------|
| Month 3 (Early) | 10    | NX              | NY            | NZ     |
| Month 12        | 100   | NX              | NY            | NZ     |
| Year 3 (Scale)  | 1,000 | NX              | NY            | NZ     |

## E. Go-to-Market Strategy
- **First 10 users:** [Your specific plan]
- **Marketing channels:** [e.g., WhatsApp groups, Instagram, campus events]
- **Key partnership:** [One specific company or organisation to target]
```

---

## 💡 `feature_log.md` Template

Track your one-feature-at-a-time build progress:

```markdown
# Feature Build Log — [Your Name / Code]

| Date       | Feature Built                        | Test Performed                              | Status  |
|------------|--------------------------------------|---------------------------------------------|---------|
| 2026-07-25 | MySQL database setup + table created | Inserted 1 test row, SELECT confirmed       | Done    |
| 2026-07-26 | scraper.py — scrapes 20 listings     | Printed all 20 to console, no errors        | Done    |
| 2026-07-27 | Pandas cleaning — removed NaN prices | df.isnull().sum() returns 0 nulls           | Done    |
| ...        | ...                                  | ...                                         | ...     |
```
