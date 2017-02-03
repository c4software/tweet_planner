# Tweet planner

The goal of this python script is to tweet automatically a queue of « message » to your twitter Account.

### Installation

- Clone this repo.
- Install dependancy ```pip install -r requirements.py```
- Add your API keys in the *secrets.py* file.


### Usage

#### First usage

```sh
python3 main.py --init
```

#### Add tweet to queue

```sh
python3 main.py -a "Ceci est un test"
```

#### Connect and Tweet (randomly)

Randomly send (or not) a tweet present in the queue.

```sh
python3 main.py
```
