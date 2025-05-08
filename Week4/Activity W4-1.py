import pandas as pd

class CityTemperature:
    def __init__(self, name, filepath):
        self.name = name
        self.filepath = filepath
        self.df = pd.read_csv(filepath)

    def get_monthly_temps(self):
        self.df = self.df.drop_duplicates(subset='PERIOD') 
        return self.df.set_index('PERIOD')['STATS_VALUE']

def compare_temperatures(city1, city2):
    df = pd.concat([city1.get_monthly_temps(), city2.get_monthly_temps()], axis=1)
    df.columns = [city1.name, city2.name]
    print("\nMonthly Average Temperature Comparison:\n")
    print(df)

# --- USAGE ---
# Ensure your CSVs have "Month" and "AvgTemperature" columns.

auckland = CityTemperature("Auckland", "Yoobee_College_SE_Python_Demo\Week4\Auckland.csv")
christchurch = CityTemperature("Christchurch", "Yoobee_College_SE_Python_Demo\Week4\Christchurch.csv")

# auckland.load_data()
# christchurch.load_data()

compare_temperatures(auckland, christchurch)
