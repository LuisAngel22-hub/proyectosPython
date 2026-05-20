import pyAgrum as gum
import pyAgrum.lib.notebook as gnb

# 1. Crear la red
bn = gum.BayesNet('TiendaAves')

# 2. Agregar nodos
# Cada nodo tendrá dos valores posibles
t = bn.add(gum.LabelizedVariable('Temperatura', 'Temperatura', 2))
h = bn.add(gum.LabelizedVariable('Humedad', 'Humedad', 2))
e = bn.add(gum.LabelizedVariable('Enfermedades', 'Enfermedades', 2))
ae = bn.add(gum.LabelizedVariable('Aves_Enfermas', 'Aves_Enfermas', 2))
m = bn.add(gum.LabelizedVariable('Mortalidad', 'Mortalidad', 2))

# 3. Definir conexiones
bn.addArc(t, e)
bn.addArc(h, e)
bn.addArc(e, ae)
bn.addArc(ae, m)

# 4. Especificar CPDs

# Temperatura y Humedad (sin padres)
bn.cpt(t).fillWith([0.5, 0.5])  # Alta, Baja
bn.cpt(h).fillWith([0.5, 0.5])  # Alta, Baja

# Enfermedades dado Temperatura y Humedad
# Orden: T=Alta,H=Alta | T=Alta,H=Baja | T=Baja,H=Alta | T=Baja,H=Baja
bn.cpt(e)[{'Temperatura': 0, 'Humedad': 0}] = [0.9, 0.1]
bn.cpt(e)[{'Temperatura': 0, 'Humedad': 1}] = [0.7, 0.3]
bn.cpt(e)[{'Temperatura': 1, 'Humedad': 0}] = [0.6, 0.4]
bn.cpt(e)[{'Temperatura': 1, 'Humedad': 1}] = [0.1, 0.9]

# Aves_Enfermas dado Enfermedades
bn.cpt(ae)[{'Enfermedades': 0}] = [0.85, 0.15]  # Sí
bn.cpt(ae)[{'Enfermedades': 1}] = [0.1, 0.9]    # No

# Mortalidad dado Aves_Enfermas
bn.cpt(m)[{'Aves_Enfermas': 0}] = [0.8, 0.2]  # Alta
bn.cpt(m)[{'Aves_Enfermas': 1}] = [0.1, 0.9]  # Baja

# 5. Hacer inferencias
ie = gum.LazyPropagation(bn)
ie.makeInference()

# Ejemplo: ¿Cuál es la probabilidad de mortalidad si Temp=Alta y Humedad=Alta?
ie.setEvidence({'Temperatura': 0, 'Humedad': 0})  # 0 = Alta
ie.makeInference()

print("Probabilidades de Mortalidad (Alta/Baja):")
print(ie.posterior('Mortalidad'))
