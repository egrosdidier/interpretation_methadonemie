import streamlit as st
import matplotlib.pyplot as plt

# Configuration de l'interface Streamlit
st.title("Interprétation de la Méthadonémie")

# Saisie des valeurs
methadonemie = st.number_input("Méthadonémie (ng/mL)", min_value=0, max_value=2000, value=200)
eddp = st.number_input("EDDP (ng/mL)", min_value=0, max_value=2000, value=100)

# Création du graphe
fig, ax = plt.subplots()
ax.scatter(methadonemie, eddp, color='red', label='Valeur mesurée')

# Définition des zones normales et anormales
ax.axhspan(30, 300, color='green', alpha=0.2, label='Zone normale EDDP')
ax.axvspan(100, 400, color='blue', alpha=0.2, label='Zone normale Méthadonémie')

# Zones anormales
ax.axhspan(0, 30, color='red', alpha=0.2, label='EDDP trop bas')
ax.axhspan(300, 2000, color='red', alpha=0.2, label='EDDP trop haut')
ax.axvspan(0, 100, color='red', alpha=0.2, label='Méthadonémie trop basse')
ax.axvspan(400, 600, color='orange', alpha=0.2, label='Méthadonémie élevée (risque accru)')
ax.axvspan(600, 2000, color='red', alpha=0.2, label='Méthadonémie trop haute (risque toxicité)')

# Paramètres du graphe
ax.set_xlabel("Méthadonémie (ng/mL)")
ax.set_ylabel("EDDP (ng/mL)")
ax.set_title("Interprétation des valeurs de Méthadonémie et EDDP")
ax.legend()
ax.grid(True)

# Affichage du graphe dans Streamlit
st.pyplot(fig)

# Tableau d'interprétation
st.write("## Tableau de classification du métabolisme")
st.write("| Situation clinique | Méthadone plasmatique | EDDP | Interprétation |")
st.write("|-------------------|----------------------|------|----------------|")
st.write("| **Réponse normale** | 100-400 ng/mL | 30-300 ng/mL | Métabolisation standard |")
st.write("| **Métabolisation rapide** | < 100 ng/mL | > 300 ng/mL | Fort métabolisme hépatique → risque de manque en fin de journée → besoin de dose fractionnée |")
st.write("| **Méthadonémie élevée** | 400-600 ng/mL | Variable | Surveillance recommandée (risque accru) |")
st.write("| **Métabolisation lente** | > 600 ng/mL | < 30 ng/mL | Accumulation de méthadone → risque de sédation et QT long → réduire la dose |")
