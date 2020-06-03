fig, ax1 = plt.subplots()

ax1.set_xlabel('Team')
ax1.set_ylabel('count')
# plot 1

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('count', color=color)
# plot 2
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()