- [[event-registration](https://github.com/haoxiangliew/event-registration)](#org80f8914)
  - [Installation](#orgbf9574f)
    - [Linux](#orgbfc777e)
    - [Windows](#orgbc95af4)
  - [Specifications](#org83d82ae)
    - [Scanner](#org5590e46)
    - [IDs](#org83c0429)
    - [Application](#org1d24870)



<a id="org80f8914"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.

App was made specifically for [IEEE@VT](https://ieee.vt.edu)'s Happy Hour, hello there!


<a id="orgbf9574f"></a>

## Installation


<a id="orgbfc777e"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate<.fish>
pip3 install -r requirements.txt
python3 main.py
```


<a id="orgbc95af4"></a>

### Windows

-   TODO
-   Or use WSL


<a id="org83d82ae"></a>

## Specifications


<a id="org5590e46"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;<"9-digit ID">=0249?
            <"\n">
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="org83c0429"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="org1d24870"></a>

### Application

1.  Dependencies

    ```sh
    openpyxl
    pandas
    tkinter
    ```
    
    -   Takes in `input.xlsx`, with the first-row as categories.
        -   Should have no duplicate ID and names.
    -   Filter input for scanner and manual input automatically.
    -   `tkinter` popups can be dismissed quickly with `<RET>`.