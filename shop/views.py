from django.shortcuts import render,redirect
from .models import Livre


def accueil(request):
    livres = Livre.objects.all()
    panier = request.session.get('panier', [])
    nombre = len(panier)

    return render(request, 'index.html', {
        'livres': livres,
        'nombre_panier': nombre
    })

def detail(request, id):
    livre = Livre.objects.get(id=id)
    panier = request.session.get('panier', [])
    nombre = len(panier)
    return render(request, 'detail.html', {'livre': livre})
          

def ajouter_panier(request, id):
    panier = request.session.get('panier', {})

    id_str = str(id)

    if id_str in panier:
        panier[id_str] += 1
    else:
        panier[id_str] = 1

    request.session['panier'] = panier
    return redirect('accueil')

def panier(request):
    panier = request.session.get('panier', {})

    livres = []
    total = 0
    message = "Bonjour je veux commander :%0A%0A"

    for id_str, quantite in panier.items():
        livre = Livre.objects.get(id=int(id_str))
        livre.quantite = quantite
        livre.sous_total = livre.prix * quantite

        total += livre.sous_total
        livres.append(livre)

        message += f"- {livre.titre} x {quantite} = {livre.sous_total} FCFA%0A"

    message += f"%0ATotal : {total} FCFA"

    return render(request, 'panier.html', {
        'livres': livres,
        'total': total,
        'message': message
    })
    

def supprimer_panier(request, id):
    panier = request.session.get('panier', {})

    id_str = str(id)

    if id_str in panier:
        del panier[id_str]

    request.session['panier'] = panier
    return redirect('panier')


def commander(request):
    request.session['panier'] = {}
    return redirect('accueil')
