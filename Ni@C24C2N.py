import matplotlib.pyplot as plt  
import numpy as np  

# Global font settings  
plt.rcParams["font.family"] = "Times New Roman"  
plt.rcParams["font.size"] = 16  
plt.rcParams["font.weight"] = "bold"  
plt.rcParams["axes.labelweight"] = "bold"  
plt.rcParams["axes.titleweight"] = "bold"

# Make mathematical text use Times New Roman
plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "Times New Roman"
plt.rcParams["mathtext.it"] = "Times New Roman:italic"
plt.rcParams["mathtext.bf"] = "Times New Roman:bold"
  
file_paths = ["rmsd.xvg"]  
labels = [r"$\mathbf{\mathrm{Ni}@\mathrm{C}_{24}\mathrm{C}_{2}\mathrm{N}}$"] 
colors = ["maroon"]
 
def read_xvg(file_path): 
    x_data = [] 
    y_data = [] 
 
    with open(file_path, "r") as file: 
        for line in file: 
            if line.startswith(("#", "@")): 
                continue 
            parts = line.split() 
            if len(parts) >= 2: 
                x_data.append(float(parts[0])) 
                y_data.append(float(parts[1])) 
 
    return np.array(x_data), np.array(y_data) 
 
plt.figure(figsize=(10,6)) 
 
for i, file_path in enumerate(file_paths): 
    x_data, y_data = read_xvg(file_path) 
    plt.plot(x_data, y_data, 
             color=colors[i], 
             linewidth=2.5, 
             label=labels[i]) 
 
# Title and labels 
plt.title("RMS Deviation (RMSD)", 
          fontsize=18, 
          fontweight='bold', 
          fontname='Times New Roman') 
 
plt.xlabel("Time (ns)", 
           fontsize=18, 
           fontweight='bold', 
           fontname='Times New Roman') 
 
plt.ylabel("RMSD (nm)", 
           fontsize=18, 
           fontweight='bold', 
           fontname='Times New Roman') 
 
# Axis limits 
plt.xlim(0,100) 
plt.ylim(0.00,0.04) 
 
plt.xticks(np.arange(0,101,20), 
           fontsize=16, 
           fontname='Times New Roman') 
 
plt.yticks(np.arange(0.00,0.041,0.01), 
           fontsize=16, 
           fontname='Times New Roman') 
 
# Remove extra margins 
plt.margins(x=0) 
 
# Thicker border 
ax = plt.gca() 
for spine in ax.spines.values(): 
    spine.set_linewidth(2) 
 
# Bold tick marks 
plt.tick_params(axis='both', width=2, length=6) 
 
# Make tick labels bold 
for label in ax.get_xticklabels(): 
    label.set_fontweight('bold') 
    label.set_fontname('Times New Roman') 
 
for label in ax.get_yticklabels(): 
    label.set_fontweight('bold') 
    label.set_fontname('Times New Roman') 
 
# Legend 
legend = plt.legend(prop={ 
    'family': 'Times New Roman', 
    'weight': 'bold', 
    'size': 16 
}) 
legend.get_frame().set_linewidth(1.5) 
 
plt.tight_layout() 
 
plt.savefig("RMSD_vs_Time.png", dpi=600, bbox_inches='tight') 
 
plt.show()