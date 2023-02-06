# Loading database with csv data
__author__ = "Matteo Golin"

# Imports
import pandas as pd

# Constants
USELESS_COLUMNS: list[str] = ["GEO_UPT_DT", "EFF_DATE", "OGF_ID", "MOH_PRO_ID", "EN_ALT", "FR_ALT", "ADDR_DESCR"]


# Main
def main():
    data = pd.read_csv("./Health_data.csv")

    # Remove useless data
    for column in USELESS_COLUMNS:
        data.drop(column, inplace=True, axis=1)

    data.rename(columns={"X": "LONGITUDE", "Y": "LATITUDE"})  # Rename lat and long for clarity

    service_types: pd.Series = data.get("SERV_TYPE")
    department_types: pd.Series = data.get("SERV_DET")

    print(service_types.unique())
    print(department_types.nunique())
    print(len(department_types))


if __name__ == '__main__':
    main()
