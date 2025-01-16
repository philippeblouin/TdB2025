import streamlit as st

# Conserver l'état de la connexion.
if 'logged_in' not in st.session_state:
	st.session_state['logged_in'] = False

def introduction():
	st.title("Performance après")

	a, b = st.columns(2)
	c, d = st.columns(2)
	e, f = st.columns(2)

	a.metric("Moyenne de l'utilisation du CPU", "30%", "-9%", border=True)
	b.metric("Moyenne de l'utilisation de la mémoire", "45%", "2%", border=True)

	c.metric("Moyenne de l'utilisation du stockage", "60%", "2%", border=True)
	d.metric("Latence moyenne", "20ms", "-2 ms", border=True)

	e.metric("Network Throughput", "100 mbps", "--", border=True)
	f.metric("Nombre de serveur cloud", "102", "+4", border=True)

	'''Dernière actualisation : Le 16 janvier 2025'''


def main():
	# Vérifiez l'état de la connexion
	if st.session_state['logged_in']:
		introduction()
	else:
		pass


if __name__ == "__main__":
	main()
