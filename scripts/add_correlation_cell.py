import nbformat
from pathlib import Path

NOTEBOOK_PATH = Path(r"d:/Uni/TFG/Proyecto/notebooks/03_maps.ipynb")

# Correlation cell source code
CORRELATION_CODE = """# 2.5 Correlación entre densidad (Media) y velocidad media por tramo
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df_counts and df_speed exist in the notebook
df_merged = pd.merge(
    df_counts[['Media', 'Color']],
    df_speed[['Velocidad_media']],
    left_index=True,
    right_index=True,
    suffixes=('_ruido', '_vel')
)

# Pearson correlation coefficient
corr = df_merged['Media'].corr(df_merged['Velocidad_media'])
print(f"Pearson correlation: {corr:.3f}")

# Add a row summarizing the correlation (media column left NaN)
df_merged.loc['Correlación'] = [corr, np.nan]

# Display the merged table
display(df_merged)

# Scatter plot: velocidad vs. densidad, colored by noise quartile
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df_merged.drop('Correlación'),
    x='Velocidad_media',
    y='Media',
    hue='Color',
    palette={'green': '#2ecc71', 'yellow': '#f1c40f', 'orange': '#e67e22', 'red': '#e74c3c'},
    s=80,
    edgecolor='k'
)
plt.title('Velocidad media vs. Densidad (Media) por kilómetro')
plt.xlabel('Velocidad media')
plt.ylabel('Media de eventos acústicos')
plt.grid(True, ls='--', alpha=0.5)
plt.show()
"""

def main():
    nb = nbformat.read(NOTEBOOK_PATH, as_version=4)
    # Append the new code cell at the end of the notebook
    nb.cells.append(nbformat.v4.new_code_cell(CORRELATION_CODE))
    nbformat.write(nb, NOTEBOOK_PATH)
    print(f"Correlation cell added to {NOTEBOOK_PATH}")

if __name__ == "__main__":
    main()
