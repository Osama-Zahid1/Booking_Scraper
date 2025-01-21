from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the sample Booking.com hotel reviews page
driver.get("https://www.booking.com/reviews/us/hotel/nexus.en-gb.html")

# Wait for the page to load completely
time.sleep(5)

# Scraping hotel information

# Hotel name: Adjust the selector to match the current page structure
hotel_name = driver.find_element(By.CSS_SELECTOR, 'h2').text

# Number of reviews: Look for the correct class here
number_of_reviews = driver.find_element(By.CSS_SELECTOR, '.review_list_score_count').text

# Average rating: Use the class for rating
average_rating = driver.find_element(By.CSS_SELECTOR, '.review-score-badge').text

# Collecting reviews
reviews = driver.find_elements(By.CSS_SELECTOR, 'li.review_item')

# Prepare a list to store review data
reviews_data = []
for review in reviews:
    guest_id = review.find_element(By.CSS_SELECTOR, '.review_item_reviewer').text
    country = review.find_element(By.CSS_SELECTOR, '.review_item_header_content_container').text
    review_date = review.find_element(By.CSS_SELECTOR, '.review_staydate').text
    
    # Review pros and cons
    review_content_pros = review.find_element(By.CSS_SELECTOR, '.review_pos').text if len(review.find_elements(By.CSS_SELECTOR, '.review_pos')) > 0 else ''
    review_content_cons = review.find_element(By.CSS_SELECTOR, '.review_neg').text if len(review.find_elements(By.CSS_SELECTOR, '.review_neg')) > 0 else ''
    
    # Rating score: Look for review score within each review
    rating_score = review.find_element(By.CSS_SELECTOR, '.review-score-widget').text

    # Append data to the list
    reviews_data.append({
        'Guest ID': guest_id,
        'Country': country,
        'Review Date': review_date,
        'Pros': review_content_pros,
        'Cons': review_content_cons,
        'Rating': rating_score
    })

# Close the driver (browser)
driver.quit()

# Create a DataFrame and save data to a CSV file
df = pd.DataFrame(reviews_data)
df.to_csv('hotel_reviews_sample.csv', index=False)

print("Scraping completed and data saved to CSV!")
