from django.shortcuts import render

def categoria_imc(imc: float) -> str:
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def calculadora_imc(request):
    resultado = None
    categoria = None
    tips = None

    if request.method == "POST":
        try:
            peso = float(request.POST.get("peso"))
            altura_m = float(request.POST.get("altura")) / 100.0  # altura en cm → metros
            imc = peso / (altura_m ** 2)
            resultado = round(imc, 2)
            categoria = categoria_imc(imc)

            tips_map = {
                "Bajo peso": "Prioriza densidad nutricional y consulta profesional si es persistente.",
                "Peso normal": "Mantén hábitos estables y variedad en el plato.",
                "Sobrepeso": "Revisa porciones y suma actividad moderada.",
                "Obesidad": "Busca enfoque integral: alimentación, movimiento y apoyo profesional."
            }
            tips = tips_map.get(categoria)
        except (TypeError, ValueError):
            resultado = None
            categoria = "Error en los datos ingresados"

    return render(request, "calculadora/calculadora_imc.html", {
        "resultado": resultado,
        "categoria": categoria,
        "tips": tips,
    })
