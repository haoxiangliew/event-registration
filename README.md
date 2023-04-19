- [[event-registration](https://github.com/haoxiangliew/event-registration)](#orga3e6efe)
  - [Installation](#org297cbfd)
    - [Linux](#org2476f01)
    - [Windows](#org1207e19)
  - [Specifications](#orga453deb)
    - [Scanner](#orge7a11fe)
    - [IDs](#orgba042f3)
    - [Application](#org6abaf4e)



<a id="orga3e6efe"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.

App was made specifically for [IEEE@VT](https://ieee.vt.edu)'s Happy Hour, hello there!


<a id="org297cbfd"></a>

## Installation


<a id="org2476f01"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate<.fish>
pip3 install -r requirements.txt
python3 main.py
```


<a id="org1207e19"></a>

### Windows

Using Python's shell, the Linux instructions should work perfectly


<a id="orga453deb"></a>

## Specifications


<a id="orge7a11fe"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;["9-digit ID"]=0249?
            ["\n"]
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="orgba042f3"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="org6abaf4e"></a>

### Application

1.  Dependencies

    ```sh
    openpyxl
    pandas
    tk
    ```
    
    -   Takes in `input.xlsx`, with the first-row as categories.
        -   Should have no duplicate ID and names.
    -   Filter input for scanner and manual input automatically.
    -   `tkinter` popups can be dismissed quickly with `<RET>`.