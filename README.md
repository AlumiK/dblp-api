# Paper Scraper

[![license-MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/AlumiK/paper-scraper/blob/main/LICENSE)

A helper script to get information of scholarly articles from [DBLP](https://dblp.uni-trier.de/).

## Usage

Simply put the keywords you want to search in `query.txt`. Each line of `query.txt` is an independent search for one article.

### Example

#### Input

```text
Anomaly Detection in Streams with Extreme Value Theory
Intelligent Detection of Large-Scale KPI Streams Anomaly Based on Transfer Learning
Unsupervised Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in Web Applications
Robust and Unsupervised KPI Anomaly Detection Based on Conditional Variational Autoencoder
Advances in Cryptography and Secure Hardware for Data Outsourcing
``` 

#### Output

| Query | Title | Year | Venue | CCF Class | DOI | URL | BibTeX |
| - | - | - | - | - | - | - | - |
| Anomaly Detection in Streams with Extreme Value Theory | Anomaly Detection in Streams with Extreme Value Theory. | 2017 | KDD | A | 10.1145/3097983.3098144 | https://doi.org/10.1145/3097983.3098144 | https://dblp.org/rec/conf/kdd/SifferFTL17?view=bibtex |
| Intelligent Detection of Large-Scale KPI Streams Anomaly Based on Transfer Learning | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| Unsupervised Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in Web Applications | Unsupervised Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in Web Applications. | 2018 | WWW | A | 10.1145/3178876.3185996 | https://doi.org/10.1145/3178876.3185996 | https://dblp.org/rec/conf/www/XuCZLBLLZPFCWQ18?view=bibtex |
| Robust and Unsupervised KPI Anomaly Detection Based on Conditional Variational Autoencoder | Robust and Unsupervised KPI Anomaly Detection Based on Conditional Variational Autoencoder. | 2018 | IPCCC | C | 10.1109/PCCC.2018.8710885 | https://doi.org/10.1109/PCCC.2018.8710885 | https://dblp.org/rec/conf/ipccc/LiCP18?view=bibtex |
| Advances in Cryptography and Secure Hardware for Data Outsourcing | Advances in Cryptography and Secure Hardware for Data Outsourcing. | 2020 | ICDE | A | 10.1109/ICDE48307.2020.00173 | https://doi.org/10.1109/ICDE48307.2020.00173 | https://dblp.org/rec/conf/icde/0001BM20?view=bibtex |
