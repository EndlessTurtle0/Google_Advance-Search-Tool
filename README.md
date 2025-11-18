
# Google-Advance-Search-Tool

A small desktop utility to help you build Google advanced search queries quickly, with optional filetype filtering and convenient clipboard/browser actions.

**Highlights**
- Simple, focused UI for composing advanced Google queries
- File type selection to add `filetype:` filters
- Copy to clipboard and open query in browser

**Repository Files**
- `google_advance_search_tool.py`: main app entry
- `recent_queries.json`: stores a short list of recent queries
- `requirements.txt`: Python dependencies

**Requirements**
- Python 3.8+
- See `requirements.txt` for runtime packages

Quick install (virtualenv recommended):
```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

Run the app:
```powershell
python .\google_advance_search_tool.py
```

Usage
- Type your search terms in the input field.
- Optionally pick a filetype (e.g. `pdf`, `docx`, `png`).
- Click `GENERATE QUERY` to compose the query (adds `filetype:` when selected).
- Use `COPY QUERY` to copy to clipboard or `SEARCH QUERY` to open the query in your default browser.

Examples
- Query: `machine learning`, Filetype: `pdf` → `machine learning filetype:pdf`

recent_queries.json
- The app persists a short array of recent query strings in `recent_queries.json`. You can edit or clear it manually; it must remain valid JSON (an array of strings).

Troubleshooting
- If GUI doesn't start on Windows, ensure `PyQt5` installed into the active environment.
- If `pyperclip` copy fails, check clipboard permissions or try running the app from an elevated prompt.

Contributing
- Bug reports and small fixes welcome via issues or pull requests.

License
- MIT

