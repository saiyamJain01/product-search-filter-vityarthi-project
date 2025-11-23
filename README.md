# Product Search Filter Application 🔍
## Overview
This project is a full-stack web application that demonstrates a robust product filtering system. It allows users to browse products and filter them dynamically by category, price range, and color without reloading the page. It uses Flask for the backend API and database management, and vanilla JavaScript for the client-side logic.
### Features
 - Dynamic Filtering: Updates product results instantly without page reloads.
 - Multi-Criteria Search: Filter by Category, Color, and Max Price simultaneously.
 - Price Range Slider: Interactive slider to adjust the maximum price threshold.
 - Responsive Design: Mobile-friendly grid layout that adapts to screen size.
 - Database Integration: Uses SQLite to store product data, managed via SQLAlchemy.
 - Real-time Feedback: Shows "Loading" states and "No results found" messages when appropriate.
 - Reset Functionality: A button to instantly clear all active filters.
### Technology Tools Used
 - Backend: Python 3, Flask (Web Framework)
 - Database: SQLite (Relational DB), SQLAlchemy (ORM)
 - Frontend: HTML5, CSS3
 - Testing/Dev: VS Code, Git

## Steps to Install and Run
### Prerequisites
 - Ensure **Python 3.x** is installed on your system.
 - (Recommended) Move the project folder outside of OneDrive/Dropbox to avoid file sync locking issues.

**Step 1: *Set Up the Project Structure*** 
```
Ensure your folder looks exactly like this:
/product-filter-app
│
├── app.py
├── shop.db                (Auto-generated on first run)
├── templates/
│   └── index.html
└── static/
    └── style.css
```

**Step 2: *Create a Virtual Environment (Recommended)***

Open your terminal in the project folder and run:
```
Windows:
python -m venv .venv
.venv\Scripts\activate
```
```
Mac/Linux:
python3 -m venv .venv
source .venv/bin/activate
```
**Step 3: *Install Dependencies***

Install the required Python libraries:
```
pip install -r requirements.txt
```
**Step 4: *Run the Application***

Start the Flask server:
```
python app.py
```

You should see output indicating the server is running on http://127.0.0.1:5000.

**Step 5: *Instructions for Testing***
 - Open the App: Open your web browser and go to http://127.0.0.1:5000.
 - Verify Data: You should see a grid of 8 sample products (T-shirts, Electronics, etc.).
 - Test Category Filter:
   - Select "Electronics" from the dropdown.
   - Result: Only the Smart Watch and Earbuds should appear.
 - Test Price Slider:
   - Drag the slider down to $50.
   - Result: Expensive items like the Sneakers ($120) should disappear.
 - Test Combination:
   - Select Category: "Clothing" AND Color: "Blue".
   - Result: Only the "Blue Hoodie" and "Denim Jacket" should show.
 - Test "No Results":
   - Select Category: "Electronics" and Color: "Red".
   - Result: The grid should clear, and a "No products found matching your filters" message should appear.
 - Reset:
   - Click the "Reset Filters" button.
   - Result: All controls should revert to default, and all products should reappear.