"""Diagramas de fase y cúpula de saturación (sustancias puras). Estilo Ocean Forest."""
import numpy as np
import ocean_forest as of
of.setup()


def dome(n=240, vc=1.0, Tc=1.0):
    """Cúpula de saturación esquemática en (v, T) por ley de diámetro rectilíneo.
    Devuelve (v_f, v_g, T) con v_f<v_c<v_g y T de 0.45 Tc al punto crítico."""
    t = np.linspace(0.999, 0.45, n)          # T/Tc de arriba (crítico) hacia abajo
    d = (1 - t) ** 0.35                       # parámetro de orden ~ (Tc-T)^beta
    rho_avg = 1 + 0.55 * (1 - t)              # diámetro rectilíneo
    drho = 2.05 * d                           # diferencia de densidades
    rho_l = rho_avg + drho / 2
    rho_v = rho_avg - drho / 2
    return vc / rho_l, vc / rho_v, t * Tc


VF, VG, TT = dome()
VC, TC = 1.0, 1.0


def cupula(ax, logx=False):
    """Dibuja la campana líquido-vapor en (v, T)."""
    ax.plot(VF, TT, color=of.CURVE, lw=2.4)
    ax.plot(VG, TT, color=of.CURVE, lw=2.4)
    ax.plot(VC, TC, 'o', color=of.ACCENT, ms=9, mec='white', mew=1.2, zorder=6)
    ax.annotate('punto crítico', (VC, TC), (VC + 0.15, TC + 0.02),
                color=of.TEXT, fontsize=9)
    if logx:
        ax.set_xscale('log')


# ---------- 1) Cúpula T-v con regiones ----------
fig, ax = of.new_fig(figsize=(6.4, 4.6)); of.style_axes(ax)
cupula(ax)
ax.fill_betweenx(TT, VF, VG, color=of.CURVE, alpha=0.10)
ax.text(0.30, 0.62, 'líquido\ncomprimido', color=of.BROWN, fontsize=9, ha='center')
ax.text(0.95, 0.60, 'líquido + vapor\n(saturación)', color=of.CURVE, fontsize=8.5, ha='center')
ax.text(3.4, 0.70, 'vapor\nsobrecalentado', color=of.BROWN, fontsize=9, ha='center')
ax.text(0.46, 1.16, 'región\nsupercrítica', color=of.ACCENT, fontsize=8.5, ha='center')
ax.text(0.40, 0.50, r'$v_f$', color=of.CURVE, fontsize=11)
ax.text(2.7, 0.50, r'$v_g$', color=of.CURVE, fontsize=11)
of.labels(ax, x=r'volumen específico  $v$  (log)', y=r'temperatura  $T$')
of.title(ax, r'Cúpula de saturación en el plano $T$–$v$')
ax.set_xscale('log'); ax.set_xlim(0.22, 6); ax.set_ylim(0.43, 1.32)
of.save(fig, 'diagrama_tv_cupula')

# ---------- 2) Cúpula P-v con isotermas ----------
fig, ax = of.new_fig(figsize=(6.4, 4.6)); of.style_axes(ax)
# P de saturación ~ creciente con T: usa Clausius-Clapeyron esquemático
Psat = np.exp(3.2 * (1 - 1 / np.clip(TT, 0.3, None)))
Pc = 1.0
ax.plot(VF, Psat, color=of.CURVE, lw=2.4)
ax.plot(VG, Psat, color=of.CURVE, lw=2.4)
ax.plot(VC, Pc, 'o', color=of.ACCENT, ms=9, mec='white', mew=1.2, zorder=6)
ax.annotate('punto crítico', (VC, Pc), (VC + 0.25, Pc * 1.25), color=of.TEXT, fontsize=9)
ax.fill_betweenx(Psat, VF, VG, color=of.CURVE, alpha=0.10)
# subcrítica T<Tc: rama vapor (P~1/v) -> plateau de saturación -> rama líquida empinada
i = int(np.argmin(np.abs(TT - 0.72)))
Pf, vfi, vgi = Psat[i], VF[i], VG[i]
vvap = np.linspace(vgi, 6, 120); Pvap = Pf * (vgi / vvap)
vpl = np.linspace(vfi, vgi, 30); Ppl = np.full_like(vpl, Pf)
vliq = np.linspace(0.27, vfi, 40); Pliq = Pf * (vfi / vliq) ** 7
ax.plot(np.r_[vliq, vpl, vvap], np.r_[Pliq, Ppl, Pvap], color=of.BROWN, lw=1.9, label=r'$T<T_c$')
# crítica T=Tc: monótona con inflexión en el punto crítico
vcr = np.linspace(0.27, 6, 300)
ax.plot(vcr, Pc * (VC / vcr) ** 1.15, color=of.ACCENT, lw=1.9, label=r'$T=T_c$')
# supercrítica T>Tc: monótona suave, sin plateau
vsup = np.linspace(0.27, 6, 300)
ax.plot(vsup, 1.7 * Pc * (VC / vsup), color='#6a8858', lw=1.7, label=r'$T>T_c$')
of.labels(ax, x=r'volumen específico  $v$  (log)', y=r'presión  $P$  (log)')
of.title(ax, r'Isotermas en el plano $P$–$v$')
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(0.25, 6); ax.set_ylim(0.15, 16)
of.legend(ax, loc='upper right', fontsize=8.5)
of.save(fig, 'diagrama_pv_isotermas')

# ---------- 3) Diagrama P-T de fases ----------
fig, ax = of.new_fig(figsize=(6.2, 4.6)); of.style_axes(ax)
Tt, Pt = 0.35, 0.05          # punto triple
Tcr, Pcr = 1.0, 1.0          # punto crítico
# vaporización (triple -> crítico), tipo Clausius-Clapeyron
Tv = np.linspace(Tt, Tcr, 200)
Pv = Pt * np.exp(6.0 * (1 / Tt - 1 / Tv) / (1 / Tt - 1 / Tcr) * (1 / Tt - 1 / Tcr))
Pv = Pt * (Pcr / Pt) ** ((1 / Tt - 1 / Tv) / (1 / Tt - 1 / Tcr))
ax.plot(Tv, Pv, color=of.CURVE, lw=2.4, label='vaporización')
# sublimación (debajo del triple, más empinada)
Ts = np.linspace(0.18, Tt, 120)
Ps = Pt * (Pt / 0.004) ** ((1 / Tt - 1 / Ts) / (1 / Tt - 1 / 0.18) * -1 + 0) * 0 + \
     Pt * np.exp(-9.0 * (1 / Ts - 1 / Tt))
ax.plot(Ts, Ps, color=of.BROWN, lw=2.4, label='sublimación')
# fusión (casi vertical desde el triple)
Pf = np.linspace(Pt, 9, 50)
Tf = Tt + 0.02 * (Pf - Pt)
ax.plot(Tf, Pf, color=of.ACCENT, lw=2.4, label='fusión')
# puntos
ax.plot(Tt, Pt, 'o', color=of.TEXT, ms=8, zorder=6)
ax.annotate('punto triple', (Tt, Pt), (Tt + 0.04, Pt * 2.2), color=of.TEXT, fontsize=9)
ax.plot(Tcr, Pcr, 'o', color=of.ACCENT, ms=9, mec='white', mew=1.2, zorder=6)
ax.annotate('punto crítico', (Tcr, Pcr), (Tcr - 0.40, Pcr * 1.5), color=of.TEXT, fontsize=9)
ax.text(0.24, 2.0, 'SÓLIDO', color=of.TEXT, fontsize=10, weight='bold')
ax.text(0.62, 3.0, 'LÍQUIDO', color=of.TEXT, fontsize=10, weight='bold')
ax.text(0.78, 0.18, 'VAPOR', color=of.TEXT, fontsize=10, weight='bold')
of.labels(ax, x=r'temperatura  $T$', y=r'presión  $P$  (log)')
of.title(ax, r'Diagrama de fases $P$–$T$')
ax.set_yscale('log'); ax.set_xlim(0.16, 1.25); ax.set_ylim(0.01, 12)
of.legend(ax, loc='lower right', fontsize=8.5)
of.save(fig, 'diagrama_pt_fases')

# ---------- 4) Regla de la palanca (T-v) ----------
fig, ax = of.new_fig(figsize=(6.4, 4.6)); of.style_axes(ax)
cupula(ax)
i = int(np.argmin(np.abs(TT - 0.72)))
vf, vg, Tline = VF[i], VG[i], TT[i]
x = 0.4
vx = vf + x * (vg - vf)
ax.plot([vf, vg], [Tline, Tline], color=of.BROWN, lw=2.0, ls='-')
ax.plot([vf, vg], [Tline, Tline], 'o', color=of.CURVE, ms=7, zorder=6)
ax.plot(vx, Tline, 'o', color=of.ACCENT, ms=10, mec='white', mew=1.2, zorder=7)
ax.annotate(r'$f$ ($x{=}0$)', (vf, Tline), (vf - 0.05, Tline + 0.05), color=of.CURVE, fontsize=9, ha='right')
ax.annotate(r'$g$ ($x{=}1$)', (vg, Tline), (vg + 0.05, Tline + 0.05), color=of.CURVE, fontsize=9)
ax.annotate('estado\n$(T,v)$', (vx, Tline), (vx, Tline - 0.13), color=of.ACCENT, fontsize=9, ha='center')
ax.annotate('', (vx, Tline + 0.03), (vf, Tline + 0.03),
            arrowprops=dict(arrowstyle='<->', color=of.ACCENT, lw=1.3))
ax.text((vf + vx) / 2, Tline + 0.06, r'$x\,v_{fg}$', color=of.ACCENT, fontsize=9, ha='center')
ax.annotate('', (vg, Tline - 0.03), (vx, Tline - 0.03),
            arrowprops=dict(arrowstyle='<->', color=of.BROWN, lw=1.3))
ax.text((vx + vg) / 2, Tline - 0.06, r'$(1-x)\,v_{fg}$', color=of.BROWN, fontsize=8.5, ha='center')
of.labels(ax, x=r'volumen específico  $v$  (log)', y=r'temperatura  $T$')
of.title(ax, r'Regla de la palanca:  $v=v_f+x\,v_{fg}$')
ax.set_xscale('log'); ax.set_xlim(0.22, 6); ax.set_ylim(0.43, 1.2)
of.save(fig, 'region_bifasica_palanca')

# ---------- 5) Líneas de calidad constante (T-v) ----------
fig, ax = of.new_fig(figsize=(6.4, 4.6)); of.style_axes(ax)
cupula(ax)
for x, col in [(0.2, '#9a7030'), (0.4, of.ACCENT), (0.6, of.BROWN), (0.8, '#6a8858')]:
    vx = VF + x * (VG - VF)
    ax.plot(vx, TT, color=col, lw=1.5, ls='--', dashes=(5, 3))
    ax.annotate(f'$x={x}$', (vx[185], TT[185]), color=col, fontsize=8.5,
                ha='center', va='top')
ax.fill_betweenx(TT, VF, VG, color=of.CURVE, alpha=0.07)
of.labels(ax, x=r'volumen específico  $v$  (log)', y=r'temperatura  $T$')
of.title(ax, r'Líneas de calidad constante bajo la cúpula')
ax.set_xscale('log'); ax.set_xlim(0.22, 6); ax.set_ylim(0.43, 1.32)
of.save(fig, 'calidad_region_bifasica')

# ---------- 6) Campana P-v escala log (volumen específico) ----------
fig, ax = of.new_fig(figsize=(6.4, 4.6)); of.style_axes(ax)
ax.plot(VF, Psat, color=of.CURVE, lw=2.4)
ax.plot(VG, Psat, color=of.CURVE, lw=2.4)
ax.plot(VC, Pc, 'o', color=of.ACCENT, ms=9, mec='white', mew=1.2, zorder=6)
ax.fill_betweenx(Psat, VF, VG, color=of.CURVE, alpha=0.10)
ax.text(0.33, 0.5, 'líq.', color=of.BROWN, fontsize=9)
ax.text(0.95, 0.30, 'líq.+vapor', color=of.CURVE, fontsize=8.5, ha='center')
ax.text(3.2, 0.5, 'vapor', color=of.BROWN, fontsize=9)
ax.annotate(r'$v_g/v_f\sim10^3$ a baja $P$', (2.0, 0.18), color=of.TEXT, fontsize=8.5, ha='center')
of.labels(ax, x=r'volumen específico  $v$  (log)', y=r'presión  $P$  (log)')
of.title(ax, r'Campana de saturación  $P$–$v$  (escala log)')
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(0.25, 6); ax.set_ylim(0.12, 3)
of.save(fig, 'volumen_especifico_campana_Pv')

# ---------- 7) Región de vapor sobrecalentado ----------
fig, ax = of.new_fig(figsize=(6.4, 4.6)); of.style_axes(ax)
cupula(ax)
# isobaras en la región de vapor (a la derecha de v_g)
for Piso, col in [(0.3, of.BROWN), (0.6, of.ACCENT)]:
    vv = np.linspace(0.9, 6, 200)
    T = Piso * vv * 1.0 + 0.2     # T ~ Pv/R recta (gas ideal)
    ax.plot(vv, T, color=col, lw=1.5, ls=':')
ax.fill_betweenx(TT, VG, 6, color=of.BROWN, alpha=0.06)
ax.text(3.4, 0.65, 'vapor\nsobrecalentado\n$T>T_{sat}(P)$', color=of.BROWN, fontsize=9, ha='center')
ax.annotate('línea de\nvapor saturado', (VG[120], TT[120]), (1.4, 0.95),
            color=of.CURVE, fontsize=8.5,
            arrowprops=dict(arrowstyle='->', color=of.CURVE, lw=1))
of.labels(ax, x=r'volumen específico  $v$  (log)', y=r'temperatura  $T$')
of.title(ax, r'Región de vapor sobrecalentado')
ax.set_xscale('log'); ax.set_xlim(0.22, 6); ax.set_ylim(0.43, 1.32)
of.save(fig, 'vapor_sobrecalentado_region')

# ---------- 8) Región de líquido comprimido ----------
fig, ax = of.new_fig(figsize=(6.4, 4.6)); of.style_axes(ax)
cupula(ax)
ax.fill_betweenx(TT, 0.22, VF, color=of.BROWN, alpha=0.07)
for Piso, col in [(2.0, of.ACCENT), (5.0, of.BROWN)]:
    # isobaras altas: casi verticales en la zona de líquido (v~cte)
    Tl = np.linspace(0.45, 0.98, 50)
    vl = 0.30 + 0.04 * (Tl - 0.45) / 0.5      # v crece levemente con T
    ax.plot(vl, Tl, color=col, lw=1.4, ls=':')
ax.text(0.27, 0.75, 'líquido\ncomprimido\n$P>P_{sat}(T)$', color=of.BROWN, fontsize=9, ha='center')
ax.annotate('línea de\nlíquido saturado', (VF[120], TT[120]), (0.6, 0.55),
            color=of.CURVE, fontsize=8.5,
            arrowprops=dict(arrowstyle='->', color=of.CURVE, lw=1))
of.labels(ax, x=r'volumen específico  $v$  (log)', y=r'temperatura  $T$')
of.title(ax, r'Región de líquido comprimido (subenfriado)')
ax.set_xscale('log'); ax.set_xlim(0.22, 6); ax.set_ylim(0.43, 1.32)
of.save(fig, 'liquido_comprimido_region')

# ---------- 9) Diagrama P-v genérico (variables de estado) ----------
fig, ax = of.new_fig(figsize=(6.2, 4.4)); of.style_axes(ax)
ax.plot(VF, Psat, color=of.CURVE, lw=2.4)
ax.plot(VG, Psat, color=of.CURVE, lw=2.4)
ax.plot(VC, Pc, 'o', color=of.ACCENT, ms=8, mec='white', mew=1.2, zorder=6)
ax.fill_betweenx(Psat, VF, VG, color=of.CURVE, alpha=0.10)
# un punto de estado en cada región
for v, P, lab in [(0.30, 1.5, 'líquido'), (1.0, 0.42, 'bifásico'), (3.5, 0.7, 'vapor')]:
    ax.plot(v, P, 's', color=of.BROWN, ms=6, zorder=6)
    ax.annotate(lab, (v, P), (v, P * 1.4), color=of.TEXT, fontsize=8.5, ha='center')
of.labels(ax, x=r'volumen específico  $v$  (log)', y=r'presión  $P$  (log)')
of.title(ax, r'Estado fijado por dos propiedades en el plano $P$–$v$')
ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xlim(0.25, 6); ax.set_ylim(0.18, 4)
of.save(fig, 'variables_estado_diagrama_Pv')

# ---------- 10) Entalpía de vaporización h_fg(T) ----------
fig, ax = of.new_fig(figsize=(6.2, 4.2)); of.style_axes(ax)
Tw = np.linspace(0, 374.14, 300)        # °C, agua
Tr = (Tw + 273.15) / (374.14 + 273.15)
hfg = 2501 * (1 - Tr) ** 0.38           # correlación de Watson, hfg(0°C)=2501
ax.plot(Tw, hfg, color=of.CURVE, lw=2.6)
ax.fill_between(Tw, hfg, 0, color=of.CURVE, alpha=0.12)
ax.plot(374.14, 0, 'o', color=of.ACCENT, ms=9, mec='white', mew=1.2, zorder=6)
ax.annotate('punto crítico\n$h_{fg}\\to0$', (374.14, 0), (300, 400), color=of.TEXT, fontsize=9, ha='center')
ax.annotate('$2501$ kJ/kg', (0, 2501), (20, 2150), color=of.BROWN, fontsize=9)
of.labels(ax, x=r'temperatura de saturación  $T$ [°C]', y=r'$h_{fg}$ [kJ/kg]')
of.title(ax, r'Entalpía de vaporización del agua  $h_{fg}(T)$')
ax.set_xlim(0, 380); ax.set_ylim(0, 2750)
of.save(fig, 'hfg_vs_temperatura')

print('OK fases: 10 figuras')
