- [[event-registration](https://github.com/haoxiangliew/event-registration)](#orgc383025)
  - [Specifications](#org7ce0dfb)
    - [Scanner](#org6b34bd4)
    - [IDs](#orge6896e0)
    - [Application](#orgc4d60fa)
  - [Installation](#org2f54580)
    - [Linux](#org89b8988)
    - [Windows](#org89582fe)



<a id="orgc383025"></a>

# [event-registration](https://github.com/haoxiangliew/event-registration)

This is a custom app for Virgnia Tech student organizations to take in a spreadsheet and confirm the scanned individual is registered.


<a id="org7ce0dfb"></a>

## Specifications


<a id="org6b34bd4"></a>

### Scanner

-   The scanner is sourced from thesource@vt.edu
    -   [Scan Technology Inc. 4000M-DBU6](https://store-scantec.com/Search/ProductView.aspx?partid=222567983)
        -   Scanning an ID results with the following as USB keyboard input:
            
            ```sh
            ;<"9-digit ID">=0249?
            
            ```
        -   Scanner can be inaccurate at times, note scanning speed can't be too fast or too slow.


<a id="orge6896e0"></a>

### IDs

-   9-digits.
-   Presume the last 4-digits are unique.
    -   If for some edge case, there are duplicate IDs, prompt for a name search of those entries.


<a id="orgc4d60fa"></a>

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


<a id="org2f54580"></a>

## Installation


<a id="org89b8988"></a>

### Linux

```sh
python3 -m venv ./venv
source ./venv/bin/activate<.fish>
pip3 install -r requirements.txt
python3 main.py
```


<a id="org89582fe"></a>

### Windows

-   TODO
-   Or use WSL