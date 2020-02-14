# coptic-tsv ⳨

TSV files of the Coptic New Testament to be used with [clb](https://github.com/tumut/clb), generated from files in the UnboundBible format found in [coptic-nt](https://github.com/tumut/coptic-nt). Includes the scripts used to do the generation.

## Contents

| File | UnboundBible Name |
| --- | --- |
| `boh.tsv` | Coptic: Bohairic NT |
| `cop.tsv` | Coptic: New Testament |
| `sah.tsv` | Coptic: Sahidic NT |

The scripts used can be found in `tools/`.

## Building

If you want to build the files yourself, first initialize the submodules and change directory to `tools/` if you haven't already.

```
git submodule update --init
cd tools
```

After cloning the submodules, you can use any one of either:

 *  ```
    make
    ```
 *  ```
    make build
    ```
 *  ```
    make build-coptic_nt
    make build-coptic_nt_bohairic
    make build-coptic_nt_sahidic
    ```

The appropriate `.tsv` files will be generated with automatically-determined names in `bin/`.

You can also clean everything in `bin/` or clean builds individually.

 *  ```
    make clean
    ```
 *  ```
    make clean-boh
    make clean-cop
    make clean-sah
    ```

## License

MIT
