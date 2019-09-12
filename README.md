# Zawgyi To Unicode Database Converter Tool

This repo is zawgyi to unicode font converter for database tool. Currently available database are **Postgresql** and **Mysql**.

## Usage
Clone this repo to your machine
```sh
git clone https://github.com/ChesterDenn/zg2uni_db_converter.git
```

### Run with python virtual environment
And then check your machine is installed **pipenv**. If you don't install yet, please install the **pipenv**. If your machine os is Ubuntu 18.04, you can install from https://gist.github.com/planetceres/8adb62494717c71e93c96d8adad26f5c.

After installed pipenv, go to the repo and please type
```sh
$ pipenv install
$ pipenv shell
```

And run with

```sh
python convert.py
```

### Run with pip
And then check your machine is installed **pip**. If you don't install yet, please install the **pip**.

After installed pipenv, go to the repo and please type
```sh
$ pip install -r requirements.txt
```

And run with

```sh
python convert.py
```
 > Special thanks to SatanGod for Rabbit JS font converter.
