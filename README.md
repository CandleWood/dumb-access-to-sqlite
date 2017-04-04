# Access to SQLite

A really dumb way of doing Access to SQLite using [mdbtools](https://github.com/brianb/mdbtools) and a simple Python script wrapper.

So in my database class, I was given an Access database but I'm on macOS. Let's be honest, I don't want to boot up a VM on a MacBook Air to drain my battery *just* to use Access. I found [mdbviewer](https://eggerapps.at/mdbviewer/) but it was $19 and as much as I would like to support its creator, I don't work with Access databases at all outside of a school environment.

Here's a stupid simple python script to call mdbtools to convert Access to SQLite.

**macOS**

Be sure to install mdbtools. This script simply uses Python's subprocess to call the respective binaries.

```bash
brew install mdbtools
```

## Usage

Requires Python 3.4+

```bash
python access_reader.py <file>.mdb
```

## License

Public Domain