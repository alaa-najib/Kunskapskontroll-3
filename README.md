# Kunskapskontroll-3

# Projekt: SQL Dataanalys och Visualisering med Pandas och Streamlit
# Name: Alaa Almoayed
## Översikt
Detta projekt är utformat för att:

1. Ladda data från en SQL-databas.
2. Transformera data med Pandas, vid behov.
3. Genomföra dataanalys med Pandas.
4. Presentera analyserad data i en interaktiv webbapp med Streamlit.

---

## Innehållsförteckning

1. [Förutsättningar](#förutsättningar)
2. [Användning](#användning)
3. [Mappstruktur](#mappstruktur)
4. [Funktioner](#funktioner)

---

## Förutsättningar och Installation

Se till att du har följande installerat:

- Python och SQL-databas

Nödvändiga Python-paket:

- `pandas`
- `sqlalchemy`
- `streamlit`
- `matplotlib` (valfritt för ytterligare visualiseringar)

---

. Konfigurera din databasanslutning:
   - Uppdatera filen `config.py` med dina databasuppgifter.
   - Exempel:
     ```python
     DATABASE_URI = "postgresql://användare:lösenord@host:port/databasnamn"
     ```

---

## Användning

1. Kör skriptet för att analysera data:
   ```bash
   python main.py
   ```

2. Starta Streamlit-appen:
   ```bash
   streamlit run app.py
   ```
---

## Mappstruktur

```
project/
├── src/app.py               # Streamlit-appens skript
├── src/main.py              # Skript för att ladda och transformera data
├── config.py            # Konfigurationsfil för databasinloggning
├── README.md            # Projektets dokumentation
└── data/                # Valfri mapp för att lagra exempeldata eller output
```

---

## Funktioner

- **SQL-integration:** Ladda data direkt från en SQL-databas.
- **Datatransformation:** Använd Pandas för att städa och transformera data.
- **Analys:** Utför avancerad dataanalys med Pandas.
- **Visualisering:** Visa resultat interaktivt med Streamlit.

