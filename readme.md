# Django server для будильников
## Installation

`pip install -r requirements.txt`

`sudo apt-get install redis-server`

## Launch server
```
cd BasicRestAPI
python manage.py runserver
```

## API Requests available
`http://127.0.0.1:8000/api/alarm_clocks` - [GET] lists all alarm clocks available, 
[POST] adds new alarm clock (e.g.{
    "title": "Wake up",
    "description": "I'll take a nafsd fad fasfd asd fsad fp",
    "alarm_time": "17:20:00"
})

`http://127.0.0.1:8000/api/active_clocks` - lists all alarm clocks which time don't past 

`http://127.0.0.1:8000/alarm/` - lists all beeping alarms at the current time 
(current time might be calculated different than local timezone, depends on OS setup)
