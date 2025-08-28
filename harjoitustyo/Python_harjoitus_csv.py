#Tehdään ohjelma, jolla voidaan analysoida yrityksen vakavaraisuutta ja kannattavuutta sekä luokitellaan yrtitykset paremmuusjärjetykseen score-mittarin avulla:
import csv
# Haetaan aineisto
file_path = input("Anna CSV-tiedoston polku: ").strip()
# Luodaan listat sarakkeille
industry = []
revenue = []
variable_costs = []
fixed_costs = []
equity = []
liabilities = []
companyID = []

#siivotaan pois numeroista mahdolliset virheen aiheuttavat merkit ja tallennetaan aineisto kaikki arvo desimaaliluvuksi jatkokäsittelyä varten
def clean_float(value):
    try:
        return float(value.replace('\xa0', '').replace(' ', '').replace(',', ''))
    except:
        return 0.0

# Score -funktio -yritysten järjestys scorearvon mukaan 0-100 ja värikoodit selkeyttämään tulosta
def rating_score(value):
    if value >= 0.71:
        return "\033[92mErinomainen\033[0m"   # Vihreä
    elif value >= 0.51:
        return "\033[94mHyvä\033[0m"          # Vaaleansininen
    elif value >= 0.39:
        return "\033[93mKohtalainen\033[0m"   # Keltainen
    else:
        return "\033[91mHeikko\033[0m"         # Punainen

# Avataan CSV-tiedosto
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    reader.fieldnames = [name.strip() for name in reader.fieldnames if name.strip()]

    for row in reader:
        industry.append(row["Industry"].strip().lower())
        revenue.append(clean_float(row["Revenue"]))
        variable_costs.append(clean_float(row["Variable_costs"]))
        fixed_costs.append(clean_float(row["Fixed_costs"]))
        equity.append(clean_float(row["Equity"]))
        liabilities.append(clean_float(row["Liabilities"]))
        try:
            companyID.append(int(row["CompanyID"].strip()))
        except:
            companyID.append(None)

# Toimialakohtaiset koodit käyttäjän valintaa varten (myöhemmin koodissa)
industry_codes = {
    'S': 'service',
    'M': 'manufacturing',
    'E': 'e_commerce',
    'K': 'kaikki'
}

# Käyttäjän syöte toimialoista
while True:
    user_input = input("\nMitkä toimialat otetaan mukaan (Service = S,Manufacturing = M, E-commerce = E, Kaikki toimialat = K)? ").upper().replace(" ", "")
    selections = set(user_input.split(','))
    if selections.issubset(industry_codes.keys()):
        break
    print("Virheellinen syöte! Käytä S, M, E, K tai yhdistelmiä kuten S,M,E.")

# Valitaan toimialat
selected_industries = (
    [industry_codes[code] for code in industry_codes if code != 'K']
    if 'K' in selections else
    [industry_codes[code] for code in selections]
)

# Lasketaan kannattavuus ja vakavaraisuus
company_analysis = []

for i in range(len(industry)):
    if industry[i] in selected_industries:
        profit = revenue[i] - variable_costs[i] - fixed_costs[i] # Voitto -> tarvitaan kannattavuuden laskennassa seuravassa kohdassa
        profitability = profit / revenue[i] if revenue[i] else 0 # Kannattavuus
        solvency = equity[i] / (equity[i] + liabilities[i]) if (equity[i] + liabilities[i]) else 0 # Vakavaraisuus

        company_analysis.append({
            "CompanyID": companyID[i],
            "Industry": industry[i].capitalize(),
            "Profitability": round(profitability, 2),
            "Solvency": round(solvency, 2)
        })

# Tulostetaan yritysten kannattavuus ja vakavaraisuus
print("\nYritysten kannattavuus ja vakavaraisuus:")
print(f"{'CompanyID':<12} {'Industry':<15} {'Profitability':<15} {'Solvency':<10}")
print("-" * 55)
for company in company_analysis:
    print(f"{str(company['CompanyID']):<12} {company['Industry']:<15} {company['Profitability']:<15} {company['Solvency']:<10}")

# Kysytään haluaako käyttäjä sijoituskohdejärjestelyn
while True:
    score = input("\nHaluatko nähdä yritykset kannattavuuden ja vakavaraisuuden painotettuna arvona (Score) paremmuusjärjestyksessä? (K = kyllä, E = ei): ").upper().strip()
    if score in ['K', 'E']:
        break
    print("Virheellinen syöte! Vastaa K (kyllä) tai E (ei).")

if score == 'E':
    print("Ohjelma suljetaan. Ei sijoituskohdejärjestelyä.")
    exit()

# Lasketaan sijoitusarvo ja luokitus
profitability_weight = 0.6
solvency_weight = 0.4

for company in company_analysis:
    profitability = company["Profitability"]
    solvency = company["Solvency"]
    score_value = (profitability_weight * profitability) + ( solvency_weight * solvency)
    company["Score"] = round(score_value, 2)
    company["Rating"] = rating_score(score_value)

# Lajitellaan score-arvon mukaan (suurin ensin)
company_analysis.sort(key=lambda x: x["Score"], reverse=True)

# Tulostetaan sijoituskohteet paremmuusjärjestyksessä
print("\n Yritykset paremmuusjärjestyksessä score-arvon mukaan sekä niiden luokitukset (Score = 0.6 * kannattavuus + 0.4 * vakavaraisuus):")
print(f"{'CompanyID':<12} {'Industry':<15} {'Profitability':<15} {'Solvency':<10} {'Score':<10} {'Rating':<12}")
print("-" * 85)
for company in company_analysis:
    print(f"{str(company['CompanyID']):<12} {company['Industry']:<15} {company['Profitability']:<15} {company['Solvency']:<10} {company['Score']:<10} {company['Rating']:<12}")