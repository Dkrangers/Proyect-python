import streamlit as st

st.title("Calculadora de Punto de Equilibrio")

costos_fijos = st.number_input("Costos Fijos ($)", min_value=0.0, step=100.0)
precio_venta = st.number_input("Precio de Venta Unitario ($)", min_value=0.0, step=1.0)
costo_variable = st.number_input("Costo Variable Unitario ($)", min_value=0.0, step=1.0)

if st.button("Calcular"):
    if precio_venta > costo_variable:
        pe_unidades = costos_fijos / (precio_venta - costo_variable)
        pe_dinero = pe_unidades * precio_venta
        st.success(f"Punto de equilibrio: {pe_unidades:,.2f} unidades")
        st.info(f"Ventas necesarias: ${pe_dinero:,.2f}")
    else:
        st.error("El precio de venta debe ser mayor al costo variable.")
