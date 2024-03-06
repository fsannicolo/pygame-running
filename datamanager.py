import os       # per operare con il sistema operativo
import pickle   # per gestire file json

class DataManager:
    def __init__(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename
        
    def save(self, data):
        with open(self.filepath+'/'+self.filename, 'wb') as f:
            pickle.dump(data, f) 
        
    def load(self, default=0):
        # se il file esiste
        if os.path.exists(self.filepath+'/'+self.filename):
            with open(self.filepath+'/'+self.filename, 'rb') as f:
                data = pickle.load(f) 
                return data
        else:
            return default    
