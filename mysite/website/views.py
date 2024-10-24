from django.shortcuts import render

# Página de aterrizaje
def landing_page(request):
    return render(request, 'website/index.html')

# Página de retos
def retos(request):
    return render(request, 'website/retos.html')

# Página del formulario de huella de carbono
def calcula_huella(request):
    return render(request, 'website/huella.html')

# Cálculo de la huella de carbono
def calcular_huella(request):
    if request.method == 'POST':
        electricidad = float(request.POST.get('electricidad', 0))
        transporte = float(request.POST.get('transporte', 0))
        alimentos = float(request.POST.get('alimentos', 0))
        viajes = int(request.POST.get('viajes', 0))

        # Fórmulas simplificadas de cálculo (puedes mejorar las fórmulas)
        huella_total = (electricidad * 0.233) + (transporte * 0.12) + (alimentos * 5) + (viajes * 0.3)

        # Definir los parámetros según los rangos establecidos
        if huella_total < 5:
            color = 'green'
            mensaje = "¡Felicitaciones! Tu huella de carbono es baja. Sigue así y continúa tomando medidas para reducir tu impacto."
        elif 5 <= huella_total <= 10:
            color = 'yellow'
            mensaje = "Tu huella de carbono es moderada. Considera reducir tu consumo de carne y viajar menos en avión para disminuir tu huella."
        else:
            color = 'red'
            mensaje = "Tu huella de carbono es alta. Opta por energías renovables, usa transporte público y consume menos productos de origen animal para mejorar."

        return render(request, 'website/huella.html', {
            'huella_total': huella_total,
            'color': color,
            'mensaje': mensaje
        })
    return render(request, 'website/huella.html')
