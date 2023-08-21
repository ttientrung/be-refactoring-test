## Requirements overview

### Project Overview

- Investigate given code.
- Develop API Endpoint of Campaign / Ad sets / Creatives data

## Project Structure

```
.
├── src                               # Main source code directory
│   ├── base                          # Project's settings
│   ├── core                          # Core models
│   ├── data                          # Data Application
│   │   ├── data_creation.py          # Creating dummy data
│   ├── manage.py
│   ├── db.sqlite3
├── .gitignore
├── README.md                         # Project Document
├── requirements.txt
```

# DB

- Use the provided SQLite database (db.sqlite3) for development.
- Campaigns contain Ad sets; Ad sets contain Creatives.

# Questions ( 2 mandatory + 1 optional )

## Mandatory Questions:

> 1. Nested Data API Implementation:
>
> - Update /api/data/campaigns/ which should return a list of campaigns with all nested Adsets & Creatives.
> - Update /api/data/adsets/ to return a list of adsets with all nested Creatives.

> 2. Prevent spaming API (Rate limit)
>
> - Implement rate limiting based on IP address for the above endpoints.
> - Limit each IP to a maximum of 10 requests per minute to the endpoints.
> - Exceeding the limit should return a 429 status code with an appropriate warning message.

## Optional Question:

> 1.  (Optional) Base Authentication Change:
>
> - Change the base authentication field from username to user_id on the base user model.

## Note

- Multiple solutions may be valid.
- Share your refactoring ideas.
- Suggest performance optimization methods.
