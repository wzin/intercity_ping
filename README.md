# intercity_ping

Simple script that will save the 1.1.1.1 ping response times while traveling thru the country on the train.

It supports recording and plotting of ping repsonses.

## Installation

```bash
pip3 install matplotlib numpy
```

## Usage

Run and record:

```bash
python3 intercity.py --interval 10 --timeout 10 --address 1.1.1.1
```

Plot the results:

```bash
python3 intercity.py --plot
```


