import streamlit as st

# Conserver l'état de la connexion.
if 'logged_in' not in st.session_state:
	st.session_state['logged_in'] = False

def introduction():
	st.title("Performance migration")

	a, b = st.columns(2)
	c, d = st.columns(2)
	e, f = st.columns(2)

	a.metric("Taux de réussite de la migration", "98%", "-2%", border=True)
	b.metric("Temps moyen de migration par serveur", "2:33:00", "+4 min", border=True)

	c.metric("Coût de la migration", "20 022$", "+2%", border=True)
	d.metric("Nombre d'incident migration", "20", "-2", border=True)

	e.metric("Network Throughput moyen consommé par la migration","330 mbps", "--", border=True)
	f.metric("Appels aux SAC", "1","+1", border=True)
	'''Dernière actualisation : Le 16 janvier 2025'''

def main():
	# Vérifiez l'état de la connexion
	if st.session_state['logged_in']:
		introduction()
	else:
		pass

if __name__ == "__main__":
	main()
