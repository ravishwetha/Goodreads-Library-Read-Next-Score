# Goodreads-Library-Read-Next-Score

## Motivation

Read as many popular high quality books quickly.<br />

## Formula

Uses 3 data points
1. num_rating (popular)
2. avg_rating (high quality)
3. num_pages (quickly)

High ratings are rewarded, More ratings are rewarded but very long books are penalised.

## Copy HTML of Goodreads library

1. Choose infinite scroll
2. Load every entry by scrolling
3. Copy this html tag with id="books" and save in book_list.html<br />
<img width="611" alt="Screenshot 2024-06-13 at 11 47 45 PM" src="https://github.com/ravishwetha/Goodreads-Library-Read-Next-Score/assets/18163420/c026545f-6f01-41ca-91a1-a663d023ff63">

Not using the default Goodreads export because it does not include num_pages

## Convert HTML to CSV

1. Place your book_list.txt in the same folder as convert.sh
2. Run convert.sh, uncomment line with pip install for first time
3. Receive book_list.csv after running the script

## Format Google Sheet

Reference: https://docs.google.com/spreadsheets/d/e/2PACX-1vQkkaYq5lx-X8G4SiMboM7IMY9hjJgYFOfACZv6KhuZHrzx5m63rBxhG37pR_H2VygBedSf6KVWr1n7/pubhtml

1. Insert book_list.csv into the google sheet
2. Paste this in cell H2: =MEDIAN(B:B). Label it Median Pages for clarity
3. Create a new column G "To Read Score" and paste this formula: =(C2 ^ LOG10(D2 + 1)) / IF(ISBLANK(VLOOKUP(A2, RealPages!A:B, 2, FALSE)), IF(B2="unknown", $H$2, B2), VLOOKUP(A2, RealPages!A:B, 2, FALSE)). Drag down.
4. Create a new sheet called RealPages
5. Copy the title column from book_list and paste it to RealPages column A
6. Create a new column called "real_num_pages" in column B
7. Manually fill in any values that appear to be false in the original num_pages column.
