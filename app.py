import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Calculadora de Punto de Equilibrio")

# 1. Entradas de datos
cf = st.number_input("Costos fijos totales (€)", min_value=0.0, value=1200.0)
precio = st.number_input(
    "Precio de venta unitario (€)", min_value=0.01, value=50.0
)
cv = st.number_input("Costo variable unitario (€)", min_value=0.0, value=20.0)

# 2. Cálculo y validación
margen = precio - cv

if margen <= 0:
  st.error(
      "El precio de venta debe ser mayor que el costo variable para alcanzar el"
      " equilibrio."
  )
else:
  pe_unidades = cf / margen
  pe_dinero = pe_unidades * precio

  st.success(
      f"**Punto de equilibrio:** {pe_unidades:.2f} unidades ({pe_dinero:.2f} €)"
  )

  # 3. Generación del gráfico
  max_x = int(pe_unidades * 2) if pe_unidades > 0 else 50
  x = np.linspace(0, max_x, 100)
  ingresos = precio * x
  costos_totales = cf + (cv * x)

  fig, ax = plt.subplots()
  ax.plot(x, ingresos, label="Ingresos Totales", color="green")
  ax.plot(x, costos_totales, label="Costos Totales", color="red")
  ax.axhline(cf, color="gray", linestyle="--", label="Costos Fijos")
  ax.plot(
      pe_unidades, pe_dinero, "bo", markersize=8, label="Punto de Equilibrio"
  )

  ax.annotate(
      f"PE: {pe_unidades:.1f} uds\n({pe_dinero:.0f} €)",
      xy=(pe_unidades, pe_dinero),
      xytext=(pe_unidades * 1.1, pe_dinero * 0.85),
      arrowprops=dict(arrowstyle="->", color="black"),
  )

  ax.set_xlabel("Unidades vendidas")
  ax.set_ylabel("Monto (€)")
  ax.set_title("Gráfico de Punto de Equilibrio")
  ax.legend()
  ax.grid(True, alpha=0.3)

  st.pyplot(fig)
