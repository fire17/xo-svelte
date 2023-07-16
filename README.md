# xo-svelte

## Showcasing the powers of XO (python) + SVELTE

dynamic bindings
server to client updates
xo.js

## Run Backend

``` zsh
python3.11 -m pip install -r requirements.txt
python3.11 app.py
```

## Run Frontend

``` zsh
nvm use 18
npm install
npm run dev -- --open
```

## Run Side Service

inside python3.11 interpreter

``` python3.11
from xo.redis import xoRedis
redis = xoRedis("svelte")
redis.trigger("Hello from Server!") #Send msg to last session
redis.count(1710) #Update counter on last session
```
