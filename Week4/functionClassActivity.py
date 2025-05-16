import pandas as pd

class DataFileFormat_Processor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.parquet'):
            self.data = pd.read_parquet(self.file_path)
        elif self.file_path.endswith('.txt'):
            self.data = pd.read_csv(self.file_path, delimiter=',')
        else:
            raise ValueError("Unsupported file format. Please use CSV, Parquet, or TXT.")
        print(f"Data loaded successfully from: {self.file_path}")

    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")
        
        print("\nInitial Data Summary:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nDescriptive Statistics:")
        print(self.data.describe(include='all', datetime_is_numeric=True))


def main():
    print("Starting file processing...")
    file_path_csv = r'C:\Users\hp\Desktop\Assignments\Yoobee_College_SE_Python_Demo\Week4\sample_junk_mail.csv' 
    file_path_txt = r'C:\Users\hp\Desktop\Assignments\Yoobee_College_SE_Python_Demo\Week4\sample_text.txt'
    file_path_parquet = r'C:\Users\hp\Desktop\Assignments\Yoobee_College_SE_Python_Demo\Week4\Sample_data_2.parquet'
    
    for path in [file_path_csv, file_path_parquet, file_path_txt]:
        print(f'\nProcessing file: {path}')
        processor = DataFileFormat_Processor(path)
        processor.load_data()
        processor.initial_processing()

if __name__ == "__main__":
    main()
