Gap Bot with django
====================

Generate a random secret key and replace it with that text in ```settings.py```

Now you only must edit ```bot/views.py``` 
Replace your token with YOUT_TOKEN in line 9
and in ```send_request``` function, write ```send_text(chat_id,text,"TEXT THAT THE BOT REACTS TO.","BOT REACT")```
