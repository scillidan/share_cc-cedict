## share_cc-cedict

[![Create Releases](https://github.com/scillidan/share_cc-cedict/actions/workflows/releases.yml/badge.svg)](https://github.com/scillidan/share_cc-cedict/actions/workflows/releases.yml)

Data from [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cedict) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). See more on [CC-CEDICT Wiki](https://cc-cedict.org/wiki/).

## Usage

Download `.zip` from [Releases](https://github.com/scillidan/share_cc-cedict/releases):
- For GoldenDict/SilverDict, use `*--stardict-mergesyns-html.zip`.
- For sdcv, use `*-stardict-mergesyns-html2ansi.zip`.
- For Yomitan, recommend [MarvNC/cc-cedict-yomitan](https://github.com/MarvNC/cc-cedict-yomitan).

See preview screenshot [here](asset/).

### sdcv

```sh
export STARDICT_DATA_DIR="<path_to_dictionaries>"
chmod +x ./sdcv-awk.sh
# Install
ln -sfn $(pwd)/sdcv-awk.sh ~/.local/bin/sdcv-awk
# Usage
sdcv --use-dict CC-CEDICT -n <word> | sdcv-awk
# Uninstall
rm ~/.local/bin/sdcv-awk
```
