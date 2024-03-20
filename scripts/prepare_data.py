import pandas as pd

if __name__ == "__main__":

    raw_df = pd.read_csv("data/signalisation_stationnement-backup.csv")

    # Keep only selected columns
    df = raw_df[['DESCRIPTION_RPA','CODE_RPA','FLECHE_PAN','DATE_CONCEPTION_POT','DESCRIPTION_REP','Longitude','Latitude','NOM_ARROND']]
    # Drop archived and removed signs
    df = df.drop(df[df.DESCRIPTION_REP != 'Réel'].index)
    # Drop 'DESCRIPTION_REP' column
    df = df.drop('DESCRIPTION_REP', axis=1)
    # Rename columns
    df = df.set_axis(['Description','CODE_RPA','FLECHE_PAN','Depuis/Since','Longitude','Latitude','Quartier'], axis=1)

    #TODO: add string mapping for '\P', \A, and P: Stationnement interdit, Arrêt interdit, Stationnement permis, respectively.

    df.to_csv("data/signalisation_stationnement_tmp.csv", index=False)

