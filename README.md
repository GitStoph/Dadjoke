# dadjoke.py
This is a slight variation off of Joe Kaufeld's dadjoke script.
I added some color with `rich` and grabbed more than just 50 jokes for the random choice to reduce duplicates.

## Installation:
```
git clone git@github.com:GitStoph/Dadjoke.git
cd dadjoke
python3 -m pip install -r requirements.txt # OR python3 -m pip install requests rich
cp dadjoke.py /usr/local/bin/dadjoke
chmod +x /usr/local/bin/dadjoke
dadjoke
```

For added effect:
- `sudo apt install cowsay`
- `dadjoke | cowsay -f budfrogs`

I regret nothing.