# TP3 - Ejercicio 2: cálculo de impuestos
# Patrón: Singleton

class CalculadorImpuestos:
    _instance = None

    IVA          = 0.21
    IIBB         = 0.05
    CONTRIB_MUN  = 0.012

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("[Singleton] Instancia de CalculadorImpuestos creada.")
        else:
            print("[Singleton] Reutilizando instancia de CalculadorImpuestos.")
        return cls._instance

    def calcular(self, base_imponible: float) -> dict:
        iva         = base_imponible * self.IVA
        iibb        = base_imponible * self.IIBB
        contrib_mun = base_imponible * self.CONTRIB_MUN
        total       = iva + iibb + contrib_mun
        return {
            "base_imponible":          base_imponible,
            "IVA (21%)":               round(iva, 2),
            "IIBB (5%)":               round(iibb, 2),
            "Contrib. Municipales (1.2%)": round(contrib_mun, 2),
            "total_impuestos":         round(total, 2),
            "total_con_impuestos":     round(base_imponible + total, 2),
        }


# --- Demostración ---
if __name__ == "__main__":
    calc_a = CalculadorImpuestos()
    calc_b = CalculadorImpuestos()

    print(f"\n¿calc_a y calc_b son la misma instancia? {calc_a is calc_b}")

    base = 1000.0
    resultado = calc_a.calcular(base)

    print(f"\nCálculo de impuestos para base imponible: ${base:.2f}")
    for concepto, valor in resultado.items():
        print(f"  {concepto}: ${valor}")