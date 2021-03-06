import entro_py as entropy
from io import BufferedReader 
class FileClassifier:
    def __init__(self, file, threshold):
        self.file = str(file.read())
        self.threshold = threshold

    def check_mean(self):
        bytes_array = bytes(self.file, 'utf-8')
        res = entropy.compute_arithmetic_mean(bytes_array)
        return res

    def shallow_check(self):
        f = str(self.file)
        bytes_array = bytes(f, 'utf-8')
        res = entropy.compute_shannon(bytes_array)
        return res >= self.threshold

    def deep_check(self):
        f = str(self.file)
        bytes_array = bytes(f, 'utf-8')  
        mcp_res = entropy.compute_monte_carlo_pi(bytes_array)
        pi_dev = entropy.get_pi_deviation(mcp_res)
        cs_res = entropy.compute_chi_squared(bytes_array)
        return pi_dev, cs_res

    def infer(pi_dev, cs_res, mean):
        pass
    
    def classify(self):
        if self.shallow_check() is False:
            return "Not Encrupted"
        else:
            pi_dev, cs_res = self.deep_check()
            mean = self.check_mean()

            print(pi_dev, cs_res, mean)




    