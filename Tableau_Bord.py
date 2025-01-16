import streamlit as st

#Conserver l'état de la connexion.
if 'logged_in' not in st.session_state:
	st.session_state['logged_in'] = False


#Fonction pour générer des fausses données de migration.
def generate_data():
	data = pd.DataFrame({
		'Service':['Compute','Storage','Database','Network','Security'],
		'Completion': np.random.rand(5) *100
	})
	return data

#Fonction pour dessiner un graphique à barre.
#Utilisation des données "FAKE"
def plot_progress(data):
	fig,ax = plt.subplots()
	ax.barh(data['Service'], data['Completion'],color='skyblue')
	ax.set_xlabel('Complété %')
	ax.set_title('Évolution de la migration vers le cloud')
	for i,v in enumerate(data['Completion']):
		ax.text(v + 3, i, str(round(v,2)) + '%', color='blue', va='center')
	return fig


#Authentification simple
#TODO : Authentification lié à un gestionnaire d'identité.
def check_password(username, password):
	if username == "admin" and password == "admin":
		st.session_state['logged_in'] = True
		return True
	return False

# Présentation des métriques dans la pages d'accueil une fois l'authentification réussie.
def presentation_evolution():
	st.title("Évolution de la migration")
	a,b = st.columns(2)
	c,d = st.columns(2)

	a.metric("Serveur dans le cloud","100","+20", border=True)
	b.metric("Incidents cloud","3","-10%", border=True)
	c.metric("Serveur sur site","200","-22%", border=True)
	d.metric("Incidents sur site","144","+22%", border=True)
	'''Dernière actualisation : Le 16 janvier 2025'''


def main():
	if st.session_state['logged_in']:
		# Affiche les informations si le login a fonctionner.
		st.write("## Tableau de bord migration 25")
		st.write("État actuelle de la migration")

		st.write("\nLABORATOIRE\n")
		a,b,c = st.columns(3)

		a.metric("Progrès","70%","0")
		b.metric("État des incidents","Résolu","-")
		c.metric("État retour arrière","En cours","-")

		st.write("Développement")
		d,e,f = st.columns(3)

		d.metric("Progrès","50%","4%",border=True)
		e.metric("État des incidents","Résolu","-",border=True)
		f.metric("État retour arrière"," "," ",border=True)


		g,h,i = st.columns(3)
		st.write("Acceptation")
		st.write("Production")

#		data = generate_data()
#		st.dataframe(data)

#		fig=plot_progress(data)
#		st.pyplot(fig)

		st.success("Autorisé - Affichage des données sécurisé.")
	else:
		with st.sidebar:
			form=st.form("login_form")
			username = form.text_input("Nom utilisateur")
			password = form.text_input("Mot de passe", type="password")
			login_button = form.form_submit_button("Accès")

		if login_button:
			if check_password(username,password):
				st.success("Accès autorisé!")
				presentation_evolution()
			else:
				st.error("Accès refusé. Vérifier vos informations.")

if __name__ == "__main__":
	main()
