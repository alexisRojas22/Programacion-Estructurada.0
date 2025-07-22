import os
import random

# Listas globales para guardar los datos
tiempos = []
distancias = []

DISTANCIA_PREDETERMINADA = 800

def borrarpantalla():
    os.system("cls")

def esperatecla():
    input("\nPresiona cualquier tecla para continuar...")

def calcular_mejora_ritmo(ritmo_anterior, ritmo_nuevo):
    if ritmo_anterior == 0:
        return 0
    mejora = ((ritmo_anterior - ritmo_nuevo) / ritmo_anterior) * 100
    return round(mejora, 2)

def tiempodatos():
    borrarpantalla()
    print(":: Agregar nuevo tiempo y distancia ::\n")
    try:
        usar_predet = input(f"¿Quieres usar la distancia predeterminada de {DISTANCIA_PREDETERMINADA} metros? (s/n): ").strip().lower()
        if usar_predet == "s":
            nueva_distancia = DISTANCIA_PREDETERMINADA
        else:
            nueva_distancia = float(input("Ingresa la distancia recorrida en metros: "))
            if nueva_distancia <= 0:
                print("⚠️ La distancia debe ser mayor a cero.")
                return

        nuevo_tiempo = float(input("Ingresa tu tiempo en minutos para la carrera: "))
        if nuevo_tiempo <= 0:
            print("⚠️ El tiempo debe ser mayor a cero.")
            return

        if len(tiempos) > 0:
            anterior_tiempo = tiempos[-1]
            anterior_distancia = distancias[-1]
            ritmo_anterior = anterior_tiempo / anterior_distancia
            ritmo_nuevo = nuevo_tiempo / nueva_distancia
            print(f"\n🏁 Tiempo anterior: {anterior_tiempo} m | Distancia anterior: {anterior_distancia} m | Ritmo: {round(ritmo_anterior,2)} m/m")
            print(f"🏃‍♂️ Tiempo actual: {nuevo_tiempo} m | Distancia actual: {nueva_distancia} m | Ritmo: {round(ritmo_nuevo,2)} m/m")
            mejora = calcular_mejora_ritmo(ritmo_anterior, ritmo_nuevo)
            if mejora > 0:
                print(f"✅ ¡Mejoraste tu ritmo un {mejora}% respecto a la carrera anterior!")
            elif mejora < 0:
                print(f"🔻 Tu ritmo fue {abs(mejora)}% más lento que la vez anterior.")
            else:
                print("😐 Ritmo igual al anterior.")
        else:
            print("🆕 Primer tiempo y distancia registrados.")
        tiempos.append(nuevo_tiempo)
        distancias.append(nueva_distancia)
    except ValueError:
        print("❌ Ingresa un valor numérico válido.")

def historialdatos():
    borrarpantalla()
    print(":: Historial de Tiempos ::\n")
    if len(tiempos) == 0:
        print("Aún no hay tiempos registrados.")
    else:
        for i, (t, d) in enumerate(zip(tiempos, distancias)):
            print(f"Carrera #{i + 1}: {t} minutos, {d} metros")

def editardatos():
    borrarpantalla()
    print(":: Editar Tiempo o Distancia Existente ::\n")
    if len(tiempos) == 0:
        print("No hay tiempos para editar.")
    else:
        historialdatos()
        try:
            index = int(input("\nIngresa el número de carrera que deseas editar: ")) - 1
            if 0 <= index < len(tiempos):
                print("¿Qué deseas editar?")
                print("1. Solo tiempo")
                print("2. Solo distancia")
                print("3. Ambos")
                opcion = input("Selecciona una opción (1/2/3): ").strip()
                if opcion == "1":
                    nuevo_valor = float(input("Ingresa el nuevo tiempo (en minutos): "))
                    tiempos[index] = nuevo_valor
                    print("✅ Tiempo actualizado correctamente.")
                elif opcion == "2":
                    nueva_dist = float(input("Ingresa la nueva distancia (en metros): "))
                    distancias[index] = nueva_dist
                    print("✅ Distancia actualizada correctamente.")
                elif opcion == "3":
                    nuevo_valor = float(input("Ingresa el nuevo tiempo (en minutos): "))
                    nueva_dist = float(input("Ingresa la nueva distancia (en metros): "))
                    tiempos[index] = nuevo_valor
                    distancias[index] = nueva_dist
                    print("✅ Tiempo y distancia actualizados correctamente.")
                else:
                    print("❌ Opción no válida.")
            else:
                print("❌ Número de carrera no válido.")
        except ValueError:
            print("❌ Entrada inválida.")


def retosdatos():
    borrarpantalla()
    print(":: Retos Semanales ::\n")
    retos = [
        "Completa 5 carreras de 800m esta semana.",
        "Haz una carrera de 800m cada día durante 4 días seguidos.",
        "Mejora tu mejor tiempo en 800m al menos un 2%.",
        "Corre 3 veces 800m y suma los tiempos, intenta bajar el total la próxima vez.",
        "Haz una carrera de 800m con cambios de ritmo cada 200m.",
        "Corre 800m y luego haz 20 sentadillas, repite 3 veces.",
        "Invita a un amigo y compitan en 800m, ¡quien pierda invita el agua!"
    ]
    reto = random.choice(retos)
    print(f"Tu reto semanal es: {reto}")

def resumendatos():
    borrarpantalla()
    print(":: Resumen del Entrenamiento ::\n")
    if len(tiempos) == 0 and len(distancias) == 0:
        print("No hay datos para mostrar.")
    else:
        resumen = []
        for i, (tiempo, distancia) in enumerate(zip(tiempos, distancias)):
            ritmo = round(tiempo / distancia, 2)
            item = {"Carrera": i + 1, "Tiempo (m)": tiempo, "Distancia (m)": distancia, "Ritmo (m/m)": ritmo}
            if i > 0:
                ritmo_anterior = tiempos[i-1] / distancias[i-1]
                mejora = calcular_mejora_ritmo(ritmo_anterior, ritmo)
                item["Mejora ritmo (%)"] = mejora
            else:
                item["Mejora ritmo (%)"] = "N/A"
            resumen.append(item)
        for item in resumen:
            print(item)

def vaciardatos():
    borrarpantalla()
    tiempos.clear()
    distancias.clear()
    print("✅ Todos los datos han sido eliminados.")