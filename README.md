# YouTube Life History

mini version of https://github.com/menggatot/youtube-watch-history-to-csv.git
This project allows you to convert your YouTube watch history HTML file from Google Takeout into a CSV file that can be used by the universalscrobbler.com to Scrobble manually in bulk.

## Getting your YouTube Watch History

Follow these steps to download your YouTube watch history from Google Takeout:

1. Go to [Google Takeout](https://takeout.google.com/settings/takeout).
2. Click `Create new export`.
3. Click `Deselect all`.
4. Scroll down and find YouTube, then check mark it.
5. Click `All YouTube data included`.
6. Click `Deselect all`.
7. Only select `History`.
8. Click `Ok`.
9. Click `Next step`.
10. Select `Send the download link via email`.
11. Select `Export once`.
12. For file type, choose `.zip`.
13. Choose the maximum size of 1GB (the history file is less than 100MB).
14. Click `Create export`.

You will receive a `.zip` file named `takeout-xxxxx-xxx.zip` in your email. Extract the file named `watch-history.html` located in the `Takeout/Youtube and YouTube Music/history/` directory from the zip file.

## Formatting the HTML File

install required packages
```
pip install -r requirements.txt
```

```bash
python history-to-csv.py watch-history.html watch-history.csv
```