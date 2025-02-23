import streamlit as st
import matplotlib.pyplot as plt

# Configuration de l'interface Streamlit
st.title("Interprétation de la Méthadonémie")

# Saisie des valeurs
methadonemie = st.number_input("Méthadonémie (ng/mL)", min_value=0, max_value=1500, value=200)
eddp = st.number_input("EDDP (ng/mL)", min_value=0, max_value=800, value=100)

# Ajustement des limites du graphique
max_methadonemie = max(500, methadonemie * 1.2)
max_eddp = max(300, eddp * 1.2)

# Création du graphe
fig, ax = plt.subplots()
ax.scatter(methadonemie, eddp, color='red', label='Valeur mesurée')

# Définition des zones de référence
ax.axhspan(30, 300, xmin=0.1, xmax=0.8, color='green', alpha=0.3, label='Zone normale Méthadonémie & EDDP')
ax.axhspan(0, 30, xmin=0.1, xmax=0.8, color='lightblue', alpha=0.3, label='Méthadonémie normale & EDDP bas')
ax.axhspan(300, max_eddp, xmin=0.1, xmax=0.8, color='darkblue', alpha=0.3, label='Méthadonémie normale & EDDP haut')
ax.axvspan(100, 400, color='green', alpha=0.3, label='Méthadonémie normale (100-400 ng/mL)')
ax.axvspan(0, 100, color='purple', alpha=0.3, label='Méthadonémie trop basse (<100 ng/mL)')
ax.axvspan(400, 600, color='orange', alpha=0.3, label='Méthadonémie élevée (400-600 ng/mL)')
ax.axvspan(600, max_methadonemie, color='red', alpha=0.3, label='Méthadonémie très élevée (>600 ng/mL)')

# Paramètres du graphe
ax.set_xlim(0, max_methadonemie)
ax.set_ylim(0, max_eddp)
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
st.write("| **Méthadonémie trop basse** | < 100 ng/mL | Variable | Métabolisme rapide ou sous-dosage possible |")
st.write("| **Méthadonémie normale & EDDP bas** | 100-400 ng/mL | < 30 ng/mL | Métabolisme faible ou induction enzymatique possible |")
st.write("| **Méthadonémie normale & EDDP haut** | 100-400 ng/mL | > 300 ng/mL | Métabolisme rapide → risque de manque |")
st.write("| **Méthadonémie élevée** | 400-600 ng/mL | Variable | Surveillance recommandée (risque accru) |")
st.write("| **Méthadonémie très élevée** | > 600 ng/mL | Variable | Accumulation de méthadone → risque de sédation et QT long → réduire la dose |")
