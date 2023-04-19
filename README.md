- [[event-registration](https://github.com/haoxiangliew/event-registration)](#org5409ef8)
  - [Installation](#org0aa5542)
    - [Linux](#orgc0b492f)
    - [Windows](#orge60430b)
  - [Specifications](#org00b3f20)
    - [Scanner](#org1e4a6a9)
    - [IDs](#org1942b1d)
    - [Application](#orgad7bc43)



<a id="org5409ef8"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.


<a id="org0aa5542"></a>

## Installation


<a id="orgc0b492f"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate<.fish>
pip3 install -r requirements.txt
python3 main.py
```


<a id="orge60430b"></a>

### Windows

-   TODO
-   Or use WSL


<a id="org00b3f20"></a>

## Specifications


<a id="org1e4a6a9"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;<"9-digit ID">=0249?
            
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="org1942b1d"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="orgad7bc43"></a>

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