# NotPixel AutoFarm Bot

AutoFarm bot for NotPixel MiniApp (@notpixel)

## Functionality of the bot:
- Shows user status (balance, pixels, energy)
- Draws pixels on the game map
- Claim rewards

## Setup
### Before get started
You need to have installed:
- Python3 interpreter 
- Python modules: asyncio, aiohttp
- Git (if you are going to download a script via git command)

### Download the script via git clone or github interface
git clone:

```
git clone https://github.com/fhw12/not-pixel-autofarm-bot.git
```

or
- Click at "Code" button on top of this page
- Choose "HTTPS" section
- Click at "Download ZIP" button
- Unzip the archive

### Create a config file
- Create a file "config.py" within src folder
- Open the created config (src/config.py)
- Put this text in the file:

```python3
TELEGRAM_MINI_APP_INIT_DATA=''
USER_AGENT=''
```

- Set TELEGRAM_MINI_APP_INIT_DATA and USER AGENT

### Edit the config
#### Mini app init data
- Open telegram desktop version
- Go to "Advanced" -> "Experimental settings"
- Enable webview inspecting
- Close settings and open NotPixel mini app
- Right click at any element inside mini app
- Choose "Inspect Element" from the dropdown menu
- Open console tab
- Write this text in the console:

```
console.log(window.Telegram.WebView.initParams.tgWebAppData)
```

- Press enter in your keyboard
- Copy the text (without empty symbols in the end)
- Put copied text in the config file (src/config.py):

```
...
TELEGRAM_MINI_APP_INIT_DATA='user=...&hash=?...123'
...
```


#### User agent
You can use this user agent (or any other):

```
Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0
```

src/config.py:

```
...
USER_AGENT='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
...
```

### Run a script
- Open a terminal in your operations system (WIN+R and CMD in Windows. In Linux I hope you know how to do this. In MacOS open a launch menu and open a terminal)
- Write cd command, move folder with a script to the terminal and add /src to the end:

```
cd your/other/folders/not-pixel-autofarm-bot/src
```

- Finally run a python script (Windows):

```
python main.py
```

- or python3 (in Linux):

```
python3 main.py
```

- Try python or python3 in mac os

If successfully, you will see the information from the script.