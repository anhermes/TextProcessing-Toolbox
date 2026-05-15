class ProcessMemoqTerminology: #create class
    def __init__(self, file_paths):
        self.terminology_merged = None
    def check_file(self): #check if file is .xlsx or .csv
        self.file_paths = os.path.splitext(self.file_paths)
        if self.file_paths[-1] != ".xlsx"|".csv":
            print("Error: File needs to be a .xlsx or .csv")
    def import_xlsx(self): #import .xlsx file if .xlsx
        self.file_paths = os.path.splitext(self.file_paths)
        if self.file_paths[-1] == ".xlsx":
            pd.read_excel(self.file_paths)
    def import_csv(self): #import .csv file if .csv
        self.file_paths = os.path.splitext(self.file_paths)
        if self.file_paths[-1] == ".csv":
            pd.read_excel(self.file_paths)
    def merge_terminology(self): #merge files
        self.file_paths = os.path.splitext(self.file_paths)
        if self.file_paths[-1] == ".xlsx":
            import_xlsx(self)
        elif self.file_paths[-1] == ".csv":
            import_csv(self)
        terminology_merged = pd.concat([item])
    def export_merged_terminology_as_xlsx(self): #save merged files as one .xlsx file
        if not terminology_merged:
            merge_terminology(self)
        terminology_merged.to_excel("sample_files/tb_merged.xlsx", index=False)
