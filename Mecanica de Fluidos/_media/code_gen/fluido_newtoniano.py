import numpy as np
import ocean_forest as of

fig, ax = of.new_fig(figsize=(6.2, 4.3))
of.style_axes(ax)

g = np.linspace(0, 4, 300)          # rapidez de corte (shear rate) du/dy
mu = 1.0

# Newtoniano: tau = mu * gamma_dot  (destacado)
ax.plot(g, mu*g, color=of.CURVE, lw=2.6, label='Newtoniano  $\\tau=\\mu\\,\\dot\\gamma$', zorder=5)

# Contexto (otros fluidos), mas tenues
tau0 = 1.2
ax.plot(g, tau0 + 0.85*g, color=of.ACCENT, lw=1.7, ls='--',
        label='Bingham  $\\tau=\\tau_0+\\mu\\dot\\gamma$')
ax.plot(g, 1.6*g**0.55, color=of.BROWN, lw=1.7, ls='-.',
        label='Pseudoplástico  ($n<1$)')
ax.plot(g, 0.42*g**1.5, color='#6a8858', lw=1.7, ls=':',
        label='Dilatante  ($n>1$)')

# pendiente = viscosidad (anotacion)
ax.annotate('pendiente $=\\mu$', xy=(2.6, mu*2.6), xytext=(2.7, 1.15),
            color=of.TEXT, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=of.CURVE, lw=1.2))

of.labels(ax, x='rapidez de corte  $\\dot\\gamma=\\partial u/\\partial y$',
          y='esfuerzo cortante  $\\tau$')
of.title(ax, 'Reología: el fluido newtoniano es lineal')
ax.set_xlim(0, 4); ax.set_ylim(0, 4.2)
of.legend(ax, loc='upper left', fontsize=9)
of.save(fig, 'fluido_newtoniano')
