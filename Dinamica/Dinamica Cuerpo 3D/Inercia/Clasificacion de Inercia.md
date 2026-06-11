# 📚 CATÁLOGO DEFINITIVO DE MOMENTOS DE INERCIA

## 🔴 1. TENSOR DE INERCIA DE MASA [kg·m²]

### 1.1 Componentes del Tensor (siempre se integra sobre **dm**)
| Componente | Fórmula Integral | Significado Físico |
|------------|------------------|-------------------|
| **Diagonal** | $$I_{xx} = \int (y^2 + z^2) \, dm$$ | Resistencia a rotar alrededor del eje X |
| **Diagonal** | $$I_{yy} = \int (x^2 + z^2) \, dm$$ | Resistencia a rotar alrededor del eje Y |
| **Diagonal** | $$I_{zz} = \int (x^2 + y^2) \, dm$$ | Resistencia a rotar alrededor del eje Z |
| **No diagonal** | $$I_{xy} = -\int xy \, dm$$ | Acoplamiento entre rotaciones X-Y |
| **No diagonal** | $$I_{xz} = -\int xz \, dm$$ | Acoplamiento entre rotaciones X-Z |
| **No diagonal** | $$I_{yz} = -\int yz \, dm$$ | Acoplamiento entre rotaciones Y-Z |

**⚠️ NOTA CRUCIAL:** Los componentes no diagonales ya incluyen el signo negativo en su definición.

### 1.2 Representación Matricial
$$
\mathbf{I}_{\text{masa}} = 
\begin{pmatrix}
I_{xx} & I_{xy} & I_{xz} \\
I_{xy} & I_{yy} & I_{yz} \\
I_{xz} & I_{yz} & I_{zz}
\end{pmatrix}
$$

**✅ CORRECTO:** La matriz se escribe directamente con los componentes \(I_{ij}\) definidos arriba.

### 1.3 Momentos Escalares Relacionados
| Nombre | Símbolo | Fórmula | Relación |
|--------|---------|---------|----------|
| **Momento polar de masa** | $$J_m$$ | $$\int r^2 \, dm = \int (x^2+y^2+z^2) dm$$ | $$J_m = \frac{1}{2}(I_{xx}+I_{yy}+I_{zz})$$ |
| **Traza del tensor** | $$\text{Tr}(\mathbf{I})$$ | $$I_{xx}+I_{yy}+I_{zz}$$ | $$= 2J_m$$ |

---

## 🔵 2. MOMENTOS DE INERCIA DE ÁREA [m⁴]

### 2.1 Componentes Planares (siempre se integra sobre **dA**)
| Componente | Fórmula Integral | Uso en Resistencia |
|------------|------------------|-------------------|
| **Momento de inercia** | $$I_x = \int y^2 \, dA$$ | Flexión alrededor del eje X |
| **Momento de inercia** | $$I_y = \int x^2 \, dA$$ | Flexión alrededor del eje Y |
| **Producto de inercia** | $$I_{xy} = -\int xy \, dA$$ | Se anula en ejes principales |

### 2.2 Momentos Polares de Área
| Nombre | Símbolo | Fórmula | Uso |
|--------|---------|---------|-----|
| **Momento polar** | $$J_a$$ | $$\int r^2 \, dA = \int (x^2+y^2) dA$$ | Torsión en secciones circulares |
| **Momento polar** | $$I_p$$ | (alternativo para \(J_a\)) | $$\tau = \frac{T \cdot r}{J_a}$$ |

**Relación fundamental:** $$J_a = I_x + I_y$$

---

## 🟡 3. TEOREMAS FUNDAMENTALES

### 3.1 Teorema de Steiner (Ejes Paralelos)
| Para masa              | Para área           |
| ---------------------- | ------------------- |
| $$I = I_{cm} + M d^2$$ | $$I = I_c + A d^2$$ |
| **dm → M**             | **dA → A**          |

**Ejemplo concreto:**  
Para una varilla de longitud \(L\):  
- Centro: $I_{xx}^{\text{centro}} = \frac{1}{12}ML^2$  
- Extremo: $I_{xx}^{\text{extremo}} = \frac{1}{12}ML^2 + M\left(\frac{L}{2}\right)^2 = \frac{1}{3}ML^2$

### 3.2 Rotación de Ejes (Solo para área)
Para una rotación de ángulo $\theta$:
$$
\begin{aligned}
I_{x'} &= \frac{I_x + I_y}{2} + \frac{I_x - I_y}{2}\cos 2\theta - I_{xy}\sin 2\theta \\
I_{y'} &= \frac{I_x + I_y}{2} - \frac{I_x - I_y}{2}\cos 2\theta + I_{xy}\sin 2\theta \\
I_{x'y'} &= \frac{I_x - I_y}{2}\sin 2\theta + I_{xy}\cos 2\theta
\end{aligned}
$$

---

## 📊 4. TABLA DE CORRESPONDENCIAS SIN AMBIGÜEDAD

| Concepto | Variable | Símbolo | Ejemplo Típico |
|----------|----------|---------|----------------|
| **Tensor de inercia (masa)** | $$dm$$ | $$I_{xx}, I_{xy}, \mathbf{I}$$ | $$I_{xx} = \int (y^2+z^2) dm$$ |
| **Momento de inercia (área)** | $$dA$$ | $$I_x, I_y, I_{xy}$$ | $$I_x = \int y^2 dA$$ |
| **Momento polar (masa)** | $$dm$$ | $$J_m$$ | $$J_m = \int r^2 dm$$ |
| **Momento polar (área)** | $$dA$$ | $$J_a$$ | $$J_a = \int r^2 dA$$ |

**Regla mnemotécnica infalible:**  
**"Mirar la diferencial"**:  
- Si ves **dm** → **MASA** (dinámica, rotación)  
- Si ves **dA** → **ÁREA** (resistencia, flexión)

---

## 🎯 5. VALORES PARA FIGURAS COMUNES

### 5.1 Figuras con masa (dm = ρdV)

| Figura | Eje | Momento de Inercia |
|--------|-----|-------------------|
| **Partícula puntual** | Perpendicular a r | $$I = mr^2$$ |
| **Varilla delgada** (L) | Por centro, ⊥ varilla | $$\frac{1}{12}mL^2$$ |
| **Varilla delgada** (L) | Por extremo, ⊥ varilla | $$\frac{1}{3}mL^2$$ |
| **Anillo delgado** (R) | Por centro, ⊥ plano | $$mR^2$$ |
| **Disco/cilindro** (R) | Por centro, ⊥ plano | $$\frac{1}{2}mR^2$$ |
| **Esfera sólida** (R) | Por centro | $$\frac{2}{5}mR^2$$ |

### 5.2 Secciones de área (dA)

| Sección | Eje | Momento de Inercia |
|---------|-----|-------------------|
| **Rectángulo** (b×h) | Por centro, ∥ base | $$I_x = \frac{bh^3}{12}$$ |
| **Rectángulo** (b×h) | Por centro, ∥ altura | $$I_y = \frac{hb^3}{12}$$ |
| **Círculo** (R) | Por centro | $$I_x = I_y = \frac{\pi R^4}{4}$$ |
| **Círculo** (R) | Polar | $$J_a = \frac{\pi R^4}{2}$$ |
| **Triángulo** (b×h) | Por base | $$I_{base} = \frac{bh^3}{12}$$ |

---

## 🏷️ 6. NOTACIÓN 100% CLARA - PROTOCOLO

### 6.1 Para Evitar Confusión
1. **Tensor de inercia de masa**: Siempre **doble subíndice**, siempre integra **dm**
   $$I_{xx}, I_{xy}, I_{zz}$$
   
2. **Momento de inercia de área**: Siempre **subíndice simple**, siempre integra **dA**
   $$I_x, I_y, I_{xy}$$

3. **Momento polar**: Especificar contexto
   - Masa: $$J_m = \int r^2 dm$$
   - Área: $$J_a = \int r^2 dA$$

### 6.2 Ejemplo de Uso Correcto
> "Para analizar la rotación del volante, uso el **tensor de inercia** \(I_{xx}\) con **dm**.  
> Para calcular la deflexión de la viga, uso el **momento de inercia** \(I_x\) con **dA**."

---

## 🔍 7. GUÍA DE DECISIÓN RÁPIDA

```
¿Qué tipo de problema?
├── Dinámica/Rotación de cuerpos? → Usar TENSOR DE INERCIA (Iₓₓ, Iₓᵧ con dm)
├── Resistencia/Flexión de vigas? → Usar MOMENTO DE ÁREA (Iₓ, Iᵧ con dA)
└── Torsión?
    ├── ¿Sección circular? → Sí: Jₐ = ∫r² dA
    └── ¿No circular? → Tensor completo
```

---

## ✅ CHECKLIST ANTICONFUSIÓN

Antes de escribir cualquier fórmula:
- [ ] **¿Variable de integración?** → dm (masa) o dA (área)
- [ ] **¿Subíndices?** → Dobles (xx) para masa, simples (x) para área
- [ ] **¿Signo en productos?** → $I_{xy} = -\int xy \, d(\text{algo})$ ya incluye el negativo
- [ ] **¿Matriz?** → Se escribe con componentes directos, sin signos extra

---

## 📝 8. RESUMEN MNEMOTÉCNICO

```
"DOS ÍNDICES → DOS dm → MASA
UN ÍNDICE  → UN dA   → ÁREA

El signo MENOS ya vive dentro de Iₓᵧ
No pongas otro en la matriz, ¡por favor!"
```

**Última regla:**  
> Cuando veas **Iₓₓ**, piensa inmediatamente: "ah, eso integra **dm**, es para rotación".  
> Cuando veas **Iₓ**, piensa inmediatamente: "ah, eso integra **dA**, es para flexión".

---
*Documento corregido y libre de ambigüedades • Última actualización: $(date)*
