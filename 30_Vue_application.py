# Création d'un fichier dynamique d'une page de la plateforme.

def generer_fichier():
	# Indicateurs dynamique et saisies
	repository_name= input("\nEntrez le nom du répertoire de votre projet : ")
	#project_description = input("\nEntrez une brève description du projet : ")
	project_description = "MonProjetA"
	#contributors = input("\nEntrez le nom des contributeurs séparé par des virgules : ")
	contributors = "Philippe Blouin, Paul Coupal, Ester Ittée"
	installation_instructions = "Tourner et viser"
	usage_instructions= "Usage domestique seulement"
	#licence = selection_licence()

	# Générer les badges à mettre en place

	markdown_file_name = f"{repository_name}_README.md"

	# Générer le contenu du fichier Markdown
	markdown_content = f"""
	# {repository_name}
	
	{project_description}
	
	## Table des matières
	- [Installation](#installation)
	- [Utilisation](#usage)
	- [Contributeurs](#contributor)
	- [Licences](#licenses)
	- [Badges](#badges)
	- [GitHub Repository](#github-repository)
	
	## Installation
	'''{installation_instructions}'''

	## Utilisation
	'''{usage_instructions}'''
	
	## Contributeurs
	'''{contributors}'''
	
	## Licences
	
	## Badges
	
	## GitHub Repository
	"""
	markdown_file_name = f"{repository_name}_README.md"
	with open(markdown_file_name,"w")as markdown_file:
		markdown_file.write(markdown_content)
	print(f"Le fichier en format markdown {markdown_file_name} a été générée.")



def selection_licence():
	licenses = {
		"MIT":"MIT License",
		"Apache":"Apache License 2.0",
		"GPL":"GNU General Public License v3.0"
	}
	print("Sélectionnez la licence associé à votre projet : ")
	for key, value in licenses.items():
		print(f"{key}: {value}")
	while True:
		selected_license = input("Entrez le numéro correspondant au type de licence: ")
		if selected_license in licences:
			return licenses[selected_license]
		else:
			print("Entrée invalide. SVP entrez un numéro valide.")


def main():
	generer_fichier()

if __name__ == "__main__":
	main()
