import azure.functions as func
import logging

def main(req: func.HttpRequest, doc: func.Out[func.Document], documents: func.DocumentList) -> func.HttpResponse:

    # Vérifie si l'entrée est présente dans la db
    if documents:
        logging.info('Entrée trouvée')
        data = documents[0].to_dict()  # Convertir le document existant en dictionnaire
        data['count'] += 1  # Incrémenter le champs "count"
    else:
        logging.info('Entrée non trouvée')
        data = {"id": "Visitors", "count": 1} #Création de l'entrée
    
    #Ecriture dans la CosmosDB
    doc.set(func.Document.from_dict(data))

    # Retourner une réponse HTTP 200 avec un message
    return func.HttpResponse(f'CosmosDB mis à jour', status_code=200) 
