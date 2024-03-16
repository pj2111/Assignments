
class File:
    def __init__(self, filename):  # public attribute if listed here
        self.filename = filename
        self.temp_list = []        # private attribute here
        # self.size=0

    def file_process(self):
        with open(self.filename, mode='r', encoding='utf-8') as f:
            #encoding detection library chardet to detect file code before input to method
            f1=f.read()
            # convert file data to list of list
            # implement a check for csv or not
            f_list = f1.split("\n")
            # new_list = []
            for i in f_list:
                # new_list.append(i.split(","))
                self.temp_list.append(i.split(","))
            # self.size = len(self.temp_list)
        print(self.temp_list)
        # return new_list

    def __repr__(self) -> str:
        return f"Data of file --> {self.filename}"
                
    def file_shape(self):
        try:
            return(len(self.temp_list),len(self.temp_list[0]))
        except Exception as e:
            print(e, "Probably need to run file_process method")
        # return len(file_process(self)),len(file_process(self)[0])
        
    def col_names(self):
        return self.temp_list[0]
    
    def unq_vals(self, col_name):
        #unique value in a column --> take in column name, create a list/set of all 
        #values in that col
        a = self.temp_list[0].index(col_name)
        # s = set()
        l1 = set([i[a] for i in self.temp_list])
        return l1
    
    def inst(self,row):
        return self.temp_list[row]
    
    def __getitem__(self, row):
        return self.temp_list[row]
    def __len__(self):
        return len(self.temp_list)
print(__name__)
if __name__ == '__main__':
    print('Executing script')
