
import pandas as pd
df = pd.read_excel("1.xlsx", sheet_name="Sheet2") 
data = df["V"].to_numpy()
n = 90
slopes = [] 
for i in range(0, len(data),n): 
    if len(data)-i >90:
        segment = data[i:i+n] 
        from scipy.fftpack import fft, fftfreq
        y = fft(segment) 
        y_abs = abs(y) 
        y_abs2 = y_abs ** 2 
        ps = y_abs2 / n 
        f = fftfreq(n) 
        import matplotlib.pyplot as plt
        plt.loglog(f[1:n//2], ps[1:n//2]) 
        plt.xlabel("Frequency")
        plt.ylabel("Power spectrum")
        plt.title(f"Segment {i+1}") 
        import numpy as np
        x = np.log(f[1:n//2]) 
        y = np.log(ps[1:n//2]) 
        slope, intercept = np.polyfit(x, y, 1) 
        print(f"The slope of segment {i+1} is{slope}") 
        slopes.append(slope) 
    else:
        break
df_result = pd.DataFrame({"segment": range(1, len(data)-90, n), "slope": slopes}) 
df_result.to_csv("1.csv", index=False) 
