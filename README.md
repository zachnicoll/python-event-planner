# python-event-planner
Python app for grabbing the latest books, movies, and concerts. Results are exported to both a database file and HTML page that can be viewed and printed.

# Usage
This app can be used in both offline and online modes. Offline mode grabs data from pre-downloaded webpages (found in the /database folder). Online mode attempts to grab data from three separate websites. If any of these have changed their formatting since initial development, the app may fail to grab data and not function properly.

By clicking the desired category, you can then select up to 10 events from each category that you'd like to export. Turning "Database Export" off does not export the data as an additional .db file. The HTML file can be viewed via planner.html.

# Notes
- If you happen to select the same event twice, only 1 will be exported.
- If there are images missing in the HTML planner, it's because the source either had no image, or the image link is broken/protected.
