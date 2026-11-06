#!/usr/bin/env bash
# S08 ham veri indirme (2026-11-02, finans-dogrulayici). Tümü kamu malı / açık veri:
#  - U.S. Treasury Fiscal Data (MTS Table 1/9, Debt to the Penny, Average Interest Rates) — public domain, https://fiscaldata.treasury.gov
#  - FRED (St. Louis Fed) seriler; kaynak kurumlar BEA/Treasury/OMB/Fed — https://fred.stlouisfed.org (atıf: "Source: FRED")
#  - OMB Historical Table 7.1 (FY2025 Budget) — public domain, govinfo.gov
#  - Shiller ie_data.xls (CPI 1871+) — http://www.econ.yale.edu/~shiller/data.htm (akademik, atıfla)
set -euo pipefail; cd "$(dirname "$0")"
B=https://api.fiscaldata.treasury.gov/services/api/fiscal_service
curl -sg "$B/v1/accounting/mts/mts_table_1?filter=record_date:eq:2026-09-30&page[size]=100" -o mts1.json
curl -sg "$B/v1/accounting/mts/mts_table_9?filter=record_date:eq:2026-09-30&page[size]=100" -o mts9.json
: > mts9_net_interest_hist.jsonl; : > mts9_defense_total_hist.jsonl
for y in 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025; do
  curl -sg "$B/v1/accounting/mts/mts_table_9?filter=record_date:eq:$y-09-30,classification_desc:eq:Net%20Interest&fields=record_date,classification_desc,current_fytd_rcpt_outly_amt" >> mts9_net_interest_hist.jsonl; echo >> mts9_net_interest_hist.jsonl
  for c in "National%20Defense" "Total"; do
    curl -sg "$B/v1/accounting/mts/mts_table_9?filter=record_date:eq:$y-09-30,classification_desc:eq:$c&fields=record_date,classification_desc,current_fytd_rcpt_outly_amt,sequence_number_cd" >> mts9_defense_total_hist.jsonl; echo >> mts9_defense_total_hist.jsonl
  done
done
curl -sg "$B/v2/accounting/od/debt_to_penny?filter=record_date:gte:2025-09-25&sort=-record_date&page[size]=400" -o debt_to_penny.json
curl -sg "$B/v2/accounting/od/avg_interest_rates?filter=record_date:gte:2019-12-31&sort=-record_date&page[size]=2000" -o avg_interest_rates.json
for id in GFDEGDQ188S FYGFGDQ188S A091RC1Q027SBEA GDP DGS10 DTB3 DFEDTARU; do curl -s -o $id.csv "https://fred.stlouisfed.org/graph/fredgraph.csv?id=$id"; done
curl -sL -o omb_t7_1_fy2025.xlsx https://www.govinfo.gov/content/pkg/BUDGET-2025-TAB/xls/BUDGET-2025-TAB-8-1.xlsx
curl -sL -o shiller_ie_data.xls http://www.econ.yale.edu/~shiller/data/ie_data.xls
sha256sum * | cut -c1-12,65- > SHA256.txt
