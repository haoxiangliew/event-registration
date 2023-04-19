- [[event-registration](https://github.com/haoxiangliew/event-registration)](#org6ad0b10)
  - [Installation](#orgcf64d09)
    - [Linux](#org5f0fb51)
    - [Windows](#orgb99b6ca)
  - [Specifications](#org259e4ae)
    - [Scanner](#orgf4410ef)
    - [IDs](#org7533e05)
    - [Application](#orga36d72b)



<a id="org6ad0b10"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered. App was made specifically for [IEEE@VT](https://ieee.vt.edu)'s Happy Hour, hello there!


<a id="orgcf64d09"></a>

## Installation


<a id="org5f0fb51"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate<.fish>
pip3 install -r requirements.txt
python3 main.py
```


<a id="orgb99b6ca"></a>

### Windows

-   TODO
-   Or use WSL


<a id="org259e4ae"></a>

## Specifications


<a id="orgf4410ef"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;<"9-digit ID">=0249?
            
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="org7533e05"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="orga36d72b"></a>

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