## share_cc-cedict

[![Create Releases](https://github.com/scillidan/share_cc-cedict/actions/workflows/releases.yml/badge.svg)](https://github.com/scillidan/share_cc-cedict/actions/workflows/releases.yml)

Data from [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cedict) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). See more on [CC-CEDICT Wiki](https://cc-cedict.org/wiki/).

## Usage

1. Download files from [Releases](https://github.com/scillidan/share_cc-cedict/releases).
2. Use them in GoldenDict (StarDict format), sdcv, dictd.
3. See preview screenshot [here](asset/).

### GoldenDict

Not recommended used with dictionaries `Simplified to traditional Chinese` or `Traditional to simplified Chinese`. If you do, The word entry will be displayed repeatedly once.

### sdcv

```sh
export STARDICT_DATA_DIR="<path_to_dictionaries>"
chmod +x ./sdcv-awk.sh
# Install
ln -sfn $(pwd)/sdcv-awk.sh ~/.local/bin/sdcv-awk
# Usage
sdcv --color --use-dict CC-CEDICT -n <word> | sdcv-awk
# Uninstall
rm ~/.local/bin/sdcv-awk
```

### dictd

```sh
# Arch
unzip cc-cedict-<version>-dictd.zip
sudo cp cc-cedict-<version>-dictd.{index,dict.dz} /usr/share/dictd/
sudo vim /etc/dict/dictd.conf
```

```
# Add database
database cc-cedict {
	data /usr/share/dictd/cc-cedict-<version>-dictd.dict.dz
	index /usr/share/dictd/cc-cedict-<version>-dictd.index
}
```

```sh
sudo systemctl restart dictd.service
```

```sh
chmod +x ./dictd-awk.sh
# Install
ln -sfn $(pwd)/dictd-awk.sh ~/.local/bin/dictd-awk
# Usage
dict --host localhost --port 2528 --database cc-cedict -n <word> | dictd-awk
```
