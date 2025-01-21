# Hotel Reviews Scraper for Booking.com

This Python script automates the process of scraping hotel reviews from a Booking.com hotel page. It retrieves essential details about the hotel, along with individual reviews, and saves the extracted data to a CSV file for further analysis.

---

## Features

- **Scrapes Hotel Information:** 
  - Hotel Name
  - Number of Reviews
  - Average Rating
- **Scrapes Individual Reviews:**
  - Guest ID
  - Country of Reviewer
  - Review Date
  - Pros and Cons of the Stay
  - Rating Score
- **Data Storage:** Saves the scraped data in a structured CSV file.

---

## Prerequisites

1. **Python:** Ensure Python 3.7 or higher is installed.
2. **Selenium:** Install Selenium using the following command:
   ```bash
   pip install selenium
   ```
3. **Pandas:** Install Pandas for data manipulation:
   ```bash
   pip install pandas
   ```
4. **ChromeDriver:** Download the appropriate version of ChromeDriver for your Chrome browser from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/) and ensure it’s added to your system PATH.

---

## Setup and Usage

### 1. Clone or Download the Script
Save the script on your local machine.

### 2. Update the Target URL
Replace the URL in the script with the desired Booking.com hotel reviews page:
```python
driver.get("https://www.booking.com/reviews/us/hotel/nexus.en-gb.html")
```

### 3. Run the Script
Execute the script in your terminal or IDE:
```bash
python script_name.py
```

### 4. Output
- The script creates a CSV file named `hotel_reviews_sample.csv` in the same directory as the script.
- The file contains the following columns:
  - **Guest ID**
  - **Country**
  - **Review Date**
  - **Pros**
  - **Cons**
  - **Rating**

---

## Script Workflow

1. **Initialize WebDriver:** Sets up a Chrome WebDriver instance and navigates to the target Booking.com hotel reviews page.
2. **Extract Hotel Information:**
   - Scrapes the hotel name, number of reviews, and average rating.
3. **Extract Individual Reviews:**
   - Iterates through all reviews on the page and retrieves details such as guest ID, country, review date, pros/cons, and ratings.
   - Handles missing data gracefully using conditional checks.
4. **Save Data:** Compiles the extracted data into a Pandas DataFrame and saves it to a CSV file.
5. **Close WebDriver:** Ensures the browser instance is properly closed after scraping.

---

## Limitations

- **Dynamic Website Structure:** If Booking.com changes its HTML structure or class names, the script may require adjustments to selectors.
- **Pagination:** This script only scrapes reviews on the initial page. Adding support for pagination can enable scraping reviews across multiple pages.
- **Rate Limiting:** Excessive scraping may trigger rate limiting or captchas. Consider adding delays or randomization to avoid detection.

---

## Future Enhancements

- Implement support for pagination to scrape all reviews for a hotel.
- Add functionality to scrape additional data, such as reviewer's profile picture or stay details.
- Use a headless browser to run the script in the background for increased efficiency.

---

## Disclaimer

This script is intended for educational purposes only. Ensure compliance with Booking.com's terms of service before using it for scraping data. Use responsibly and at your own risk.
