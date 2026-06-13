import numpy as np
import ocean_forest as of

of.setup()
fig, (ax1, ax2) = of.new_fig(ncols=2, figsize=(8.4, 4.0))

# --- Couette: perfil lineal u = U y/h (placa superior movil) ---
of.style_axes(ax1)
h = 1.0; U = 1.0
y = np.linspace(0, h, 50)
u = U*y/h
ax1.plot(u, y, color=of.CURVE, lw=2.4)
for yy in np.linspace(0.1, 0.9, 5):
    ax1.annotate('', xy=(U*yy/h, yy), xytext=(0, yy),
                 arrowprops=dict(arrowstyle='->', color=of.CURVE, lw=1.1))
ax1.axhline(h, color=of.BROWN, lw=2.2); ax1.axhline(0, color=of.BROWN, lw=2.2)
ax1.annotate('placa móvil $U$', xy=(0.5, h), xytext=(0.18, 1.12),
             color=of.TEXT, fontsize=9)
of.labels(ax1, x='$u(y)$', y='$y$')
of.title(ax1, 'Couette: $u=U\\,y/h$')
ax1.set_xlim(-0.05, 1.25); ax1.set_ylim(-0.08, 1.25)

# --- Poiseuille: perfil parabolico entre placas fijas ---
of.style_axes(ax2)
yp = np.linspace(-1, 1, 80)
up = 1 - yp**2
ax2.plot(up, yp, color=of.ACCENT, lw=2.4)
for yy in np.linspace(-0.8, 0.8, 7):
    ax2.annotate('', xy=(1-yy**2, yy), xytext=(0, yy),
                 arrowprops=dict(arrowstyle='->', color=of.ACCENT, lw=1.1))
ax2.axhline(1, color=of.BROWN, lw=2.2); ax2.axhline(-1, color=of.BROWN, lw=2.2)
of.labels(ax2, x='$u(y)$', y='$y$')
of.title(ax2, 'Poiseuille: $u\\propto(h^2/4-y^2)$')
ax2.set_xlim(-0.08, 1.25); ax2.set_ylim(-1.2, 1.2)

fig.tight_layout()
of.save(fig, 'perfiles_couette_poiseuille')
