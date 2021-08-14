import pandas as pd


def _format_test_results(
    result: pd.DataFrame, test: str, test_name: str
) -> pd.DataFrame:
    """Formats the results of a test into a multiindex dataframe with first
    level = "test" and second level = "name". The final dataframe has a column
    called value corresponding to the "name"

    Parameters
    ----------
    result : pd.DataFrame
        The unformatted result dataframe that has to be formatted.
        Must contain
          - a column called "index" corresponding to the
            values (test statistic) to be used for the second level.
          - a column called "value" which contains the
            value of the test statistic.
        Optionally
          - a column called "Setting" which can contain information
            such as alpha value used, or number of lags used

    test_name : str
        The name of the test. Used as the value for the first level

    Returns
    -------
    pd.DataFrame
        [description]
    """
    result.rename(columns={"index": "Property"}, inplace=True)
    result["Test"] = test
    result["Test Name"] = test_name
    if "Setting" in result.columns:
        result.set_index(["Test", "Test Name", "Property", "Setting"], inplace=True)
    else:
        result.set_index(["Test", "Test Name", "Property"], inplace=True)
    return result
