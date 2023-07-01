# zokrada
ZK-SNARK Proof Verifiers on Cardano

This repository contains the code, [pitch-deck](./pitch-deck.pdf) and [whitepaper](./whitepaper.pdf) for the tool `zokrada`.

`zokrada` extends the tool `zokrates` to generate zero-knowledge proofs from abstract and high level descriptions of zero-knowledge challenges.

### Installation

In order to run the example code in this repository, install [`zokrates`](https://zokrates.github.io/gettingstarted.html).
Moreover, install python3.10 and `poetry` to fetch all other dependencies:

```bash
pip install poetry
poetry install
```

### Running

The sample code in this repository, building a contract using OpShin and emulated builtins can be run like this:

```bash
bash make.sh
```

### Testing

The correctness and runtime of the approach can be tested by executing the run script

```bash
python3 test.py
```