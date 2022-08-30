fig, ax = plt.subplots(figsize=(30, 16), nrows=4, ncols=1, frameon=False)
fig.subplots_adjust(hspace=0)
ax[0].spines["bottom"].set_visible(False)
ax[1].spines["top"].set_visible(False)
ax[1].spines["bottom"].set_visible(False)
ax[2].spines["top"].set_visible(False)
ax[2].spines["bottom"].set_visible(False)
ax[3].spines["top"].set_visible(False)

# plot 1
# plot 2
# plot 3
# plot 4

for i in range(4):
    ax[i].legend(loc=1, prop={"size": 12})

plt.xticks(rotation=0)
