# Github Profile View Notifier

Telegram bot which notifies when someone looks at your GitHub profile

## Demo
<img src="https://github.com/nishanb/Github-Profile-View-Telegram-Notifier/blob/main/demo.gif?raw=true" alt="drawing" width="100%"/>

## Usage

-

## Setup with Docker

You can run Profile Watcher from docker, you can build your own image using

```bash
docker build -t github-view-notifier:latest .
```

To depoly a Profile Watcher instance using docker container you can run the following:

```
docker run -d -p 80:5000 -e USER_CHAT_ID=<id> -e BOT_TOKEN=<token> github-view-notifier:latest
```

Now to access the webhook go to browser or postman and paste url http://localhost/github


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

![](https://github-profile-view.herokuapp.com/github)
