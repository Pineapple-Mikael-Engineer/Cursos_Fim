"""Cartas psicrométricas (aire húmedo). Estilo Ocean Forest.
Eje x: T bulbo seco [°C]; eje y: humedad específica omega [kg/kg]."""
import numpy as np
import ocean_forest as of
of.setup()

P = 101.325
TDB = np.linspace(0, 50, 300)


def Pg(T):
    return 0.61094 * np.exp(17.625 * T / (T + 243.04))    # kPa, sat. del agua


def wsat(T):
    pg = Pg(T)
    return 0.622 * pg / (P - pg)


def w_phi(T, phi):
    pv = phi * Pg(T)
    return 0.622 * pv / (P - pv)


def base(ax, titulo, fill=True):
    of.style_axes(ax)
    ws = wsat(TDB)
    ax.plot(TDB, ws, color=of.CURVE, lw=2.6)
    if fill:
        ax.fill_between(TDB, ws, 0, color=of.CURVE, alpha=0.06)
    ax.annotate(r'$\phi=100\%$ (saturación)', (33, wsat(33)), (18, 0.027),
                color=of.CURVE, fontsize=8.5,
                arrowprops=dict(arrowstyle='->', color=of.CURVE, lw=1))
    of.labels(ax, x=r'temperatura de bulbo seco  $T$ [°C]', y=r'humedad específica  $\omega$ [kg/kg]')
    of.title(ax, titulo)
    ax.set_xlim(0, 50); ax.set_ylim(0, 0.030)


def lineas_phi(ax, etiqueta=True):
    for phi, col in zip([0.2, 0.4, 0.6, 0.8], ['#9a7030', of.ACCENT, of.BROWN, '#6a8858']):
        w = np.clip(w_phi(TDB, phi), 0, 0.03)
        ax.plot(TDB, w, color=col, lw=1.4, ls='--', dashes=(5, 3))
        if etiqueta:
            ax.annotate(f'{int(phi*100)}%', (44, w_phi(44, phi)), color=col, fontsize=8)


def lineas_h(ax):
    for h in [20, 40, 60, 80, 100]:
        w = (h - 1.005 * TDB) / (2501 + 1.86 * TDB)
        m = (w >= 0) & (w <= wsat(TDB))
        ax.plot(TDB[m], w[m], color=of.ACCENT, lw=1.2, ls=':')


def lineas_twb(ax):
    for Twb in [10, 15, 20, 25, 30]:
        h = 1.005 * Twb + wsat(Twb) * (2501 + 1.86 * Twb)
        w = (h - 1.005 * TDB) / (2501 + 1.86 * TDB)
        m = (TDB >= Twb) & (w >= 0) & (w <= wsat(TDB) + 1e-6)
        ax.plot(TDB[m], w[m], color=of.BROWN, lw=1.2, ls='-.')


# 1) Diagrama psicrométrico (principal): saturación + phi
fig, ax = of.new_fig(figsize=(6.6, 4.6)); base(ax, 'Carta psicrométrica')
lineas_phi(ax)
ax.text(40, 0.004, 'líneas de\n$\\phi$ constante', color=of.ACCENT, fontsize=8.5, ha='center')
of.save(fig, 'diagrama_psicrometrico')

# 2) Estructura: las 5 familias juntas
fig, ax = of.new_fig(figsize=(6.6, 4.6)); base(ax, 'Anatomía de la carta psicrométrica', fill=False)
lineas_phi(ax, etiqueta=False); lineas_h(ax); lineas_twb(ax)
ax.plot([], [], color=of.CURVE, lw=2.2, label=r'$\phi=100\%$ saturación')
ax.plot([], [], color=of.ACCENT, lw=1.4, ls='--', label=r'$\phi$ const.')
ax.plot([], [], color=of.ACCENT, lw=1.2, ls=':', label=r'$h$ const.')
ax.plot([], [], color=of.BROWN, lw=1.2, ls='-.', label=r'$T_{bh}$ const.')
of.legend(ax, loc='upper left', fontsize=7.5)
of.save(fig, 'carta_psicrometrica_estructura')

# 3) Familia phi
fig, ax = of.new_fig(figsize=(6.4, 4.6)); base(ax, r'Familia de humedad relativa  $\phi$ constante')
lineas_phi(ax)
of.save(fig, 'carta_curvas_phi')

# 4) Familia entalpia
fig, ax = of.new_fig(figsize=(6.4, 4.6)); base(ax, r'Familia de entalpía  $h$ constante')
lineas_h(ax)
ax.annotate(r'$h=1.005\,T+\omega(2501+1.86\,T)$', (10, 0.026), color=of.ACCENT, fontsize=8.5)
for h, Tlab in [(40, 22), (60, 32), (80, 39)]:
    w = (h - 1.005 * Tlab) / (2501 + 1.86 * Tlab)
    ax.annotate(f'{h}', (Tlab, w), color=of.ACCENT, fontsize=8)
of.save(fig, 'carta_curvas_h')

# 5) Familia bulbo humedo
fig, ax = of.new_fig(figsize=(6.4, 4.6)); base(ax, r'Familia de temperatura de bulbo húmedo  $T_{bh}$')
lineas_twb(ax)
for Twb in [15, 20, 25]:
    ax.plot(Twb, wsat(Twb), 'o', color=of.BROWN, ms=5, zorder=6)
    ax.annotate(f'{Twb}°C', (Twb, wsat(Twb)), (Twb - 4, wsat(Twb) + 0.001), color=of.BROWN, fontsize=8)
of.save(fig, 'carta_curvas_Tbh')

# 6) Lectura: dado (T, phi) -> omega, h, T rocio
fig, ax = of.new_fig(figsize=(6.6, 4.6)); base(ax, r'Lectura de un estado:  dado $(T,\phi)$')
lineas_phi(ax)
T0, phi0 = 30, 0.5
w0 = w_phi(T0, phi0)
ax.plot(T0, w0, 'o', color=of.ACCENT, ms=10, mec='white', mew=1.2, zorder=8)
ax.plot([T0, T0], [0, w0], color=of.ACCENT, lw=1, ls=':')
ax.plot([0, T0], [w0, w0], color=of.ACCENT, lw=1, ls=':')
# temperatura de rocio: T donde wsat(Tdp)=w0
Tdp = TDB[np.argmin(np.abs(wsat(TDB) - w0))]
ax.plot([Tdp, T0], [w0, w0], color=of.BROWN, lw=1.4)
ax.plot(Tdp, w0, 's', color=of.BROWN, ms=7, zorder=8)
ax.annotate('estado\n$(30°C, 50\\%)$', (T0, w0), (T0 + 1.5, w0 + 0.002), color=of.ACCENT, fontsize=8.5)
ax.annotate(r'$\omega$', (0.5, w0), (1, w0 + 0.0008), color=of.ACCENT, fontsize=9)
ax.annotate(r'$T_{rocío}$', (Tdp, w0), (Tdp - 2, w0 - 0.003), color=of.BROWN, fontsize=8.5)
of.save(fig, 'carta_lectura_T_phi')

# 7) Mezcla de dos corrientes
fig, ax = of.new_fig(figsize=(6.4, 4.6)); base(ax, r'Mezcla adiabática de dos corrientes de aire')
lineas_phi(ax, etiqueta=False)
A = (12, w_phi(12, 0.8)); B = (38, w_phi(38, 0.3))
M = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
ax.plot([A[0], B[0]], [A[1], B[1]], color=of.ACCENT, lw=1.8)
for pt, lab, c in [(A, '1 (frío húmedo)', of.CURVE), (B, '2 (caliente seco)', of.BROWN), (M, 'mezcla', of.ACCENT)]:
    ax.plot(*pt, 'o', color=c, ms=8, zorder=8)
    ax.annotate(lab, pt, (pt[0] - 2, pt[1] + 0.0015), color=c, fontsize=8.5)
of.save(fig, 'mezcla_corrientes_psicrometrico')

# 8) Enfriamiento con deshumidificación
fig, ax = of.new_fig(figsize=(6.4, 4.6)); base(ax, r'Enfriamiento con deshumidificación')
lineas_phi(ax, etiqueta=False)
E = (32, w_phi(32, 0.6))                          # entrada
# enfría a omega cte hasta saturación (punto de rocío), luego sigue la saturación
Tr = TDB[np.argmin(np.abs(wsat(TDB) - E[1]))]
S = (12, wsat(12))                                # salida (saturada, fría)
ax.plot([E[0], Tr], [E[1], E[1]], color=of.ACCENT, lw=2.0)        # sensible (ω cte)
Tpath = np.linspace(Tr, 12, 50)
ax.plot(Tpath, wsat(Tpath), color=of.BROWN, lw=2.0)              # sobre saturación
for pt, lab, c in [(E, 'entrada', of.ACCENT), ((Tr, E[1]), 'rocío', of.TEXT), (S, 'salida', of.BROWN)]:
    ax.plot(*pt, 'o', color=c, ms=7, zorder=8)
    ax.annotate(lab, pt, (pt[0] + 0.5, pt[1] + 0.0012), color=c, fontsize=8.5)
ax.annotate('condensa agua', (Tr - 8, wsat(Tr - 8)), (5, 0.020), color=of.BROWN, fontsize=8.5,
            arrowprops=dict(arrowstyle='->', color=of.BROWN, lw=1))
of.save(fig, 'proceso_enfriamiento_deshumidificacion')

print('OK psicro: 8 figuras')
